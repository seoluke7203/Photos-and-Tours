# The whole purpose of this file is to use the Google Places API to generate a new column score for each of the places.
# Please do not publicly post the API key as I will be billed alot by maps. I will leave the API key upon assignment
# submission.
import pandas as pd
import requests
import numpy as np
import json
API_KEY = "AIzaSyCddj7Ybf3tJSEXyTwQa3FSNK1u4OyZFBM"

SKYTRAIN = ['29th Avenue', 'Broadway–City Hall', 'Burrard', 'Commercial–Broadway', 'Granville',
            'Joyce–Collingwood', 'King Edward', 'Langara–49th Avenue', 'Main Street–Science World'
            'Marine Drive', 'Nanaimo', 'Oakridge–41st Avenue', 'Olympic Village', 'Renfrew', 'Rupert',
            'Stadium–Chinatown', 'Vancouver City Centre', 'VCC–Clark', 'Waterfront', 'Yaletown–Roundhouse']


def find_basic_place(location, long, lat):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + "Starbucks" + \
          "&inputtype=textquery&fields=name,rating&locationbias=point:49.260812,-123.125736&key=" + API_KEY
    response = requests.get(url).json()
    print(response)


def generate_skytrain_csv():
    skytrain_long_lat = np.array([[]])

    for x in range(len(SKYTRAIN)):
        if x == 0:
            url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + SKYTRAIN[
                x] + "&Station&Vancouver" + \
                  "&inputtype=textquery&fields=geometry&key=" + API_KEY
            response = requests.get(url).json()
            station = SKYTRAIN[x] + " Station"
            skytrain_long_lat = np.array([[response['candidates'][0]['geometry']['location']['lat'],
                                           response['candidates'][0]['geometry']['location']['lng'],
                                           station]])
        else:
            url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + SKYTRAIN[
                x] + "&Station&Vancouver" + \
                  "&inputtype=textquery&fields=geometry&key=" + API_KEY
            response = requests.get(url).json()
            station = SKYTRAIN[x] + " Station"
            long_lat = np.array([[response['candidates'][0]['geometry']['location']['lat'],
                                           response['candidates'][0]['geometry']['location']['lng'],
                                           station]])
            skytrain_long_lat = np.concatenate((skytrain_long_lat, long_lat), axis=0)

    skytrain_df = pd.DataFrame(skytrain_long_lat, columns=['lat', 'long', 'name'])
    skytrain_df.to_csv('skytrain.csv', index=False)


if __name__ == '__main__':
    generate_skytrain_csv()
