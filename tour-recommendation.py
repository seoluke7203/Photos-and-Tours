import itertools

from numpy import empty, place
import pandas as pd
import folium
# from test_nlp import process_nlp

from sklearn.cluster import AffinityPropagation, DBSCAN


##### WORKING ON CATAGORIZING AMENTIES - Done #####
##### ANALYSING DATA -                   Done #####
##### USE DBSCAN TO MAP THE DATA -       Done #####
##### MAPPED THE DATA -                  Done #####
##### ADDED STATIONS -                   Done #####
##### FIND ROUTES -                      Done #####
##### FOOD DATA -                        Done #####

def extractString(row):
    # if 'cuisine' not in row.tags:
    #     return process_nlp(row['name'])
    if 'cuisine' not in row.tags:
        return 'N/A'
    return row.tags['cuisine'].lower().strip().split(';')

def marker(data, group, colour, radius = 4):
    group.add_child(
        folium.CircleMarker([data['lat'],data['lon']], radius = radius , color= colour, fill = True, fill_color = colour, fill_opacity = 1)
    )

def main():
    # just getting dataframes
    dataframeJSON = pd.read_json('amenities-vancouver.json.gz', lines = True)

    # dropping out unnecessary columns out
    del dataframeJSON['tags']
    del dataframeJSON['timestamp']

    # CATAGORIZING
    # categories - toursist attractions: arts_centre, cinema, college, theatre, university, spa, park, casino,
    art_center = dataframeJSON[dataframeJSON.amenity == 'art_center']
    cinema = dataframeJSON[dataframeJSON.amenity == 'cinema']
    college = dataframeJSON[dataframeJSON.amenity == 'college']
    theatre = dataframeJSON[dataframeJSON.amenity == 'theatre']
    university = dataframeJSON[dataframeJSON.amenity == 'university']
    spa = dataframeJSON[dataframeJSON.amenity == 'spa']
    park = dataframeJSON[dataframeJSON.amenity == 'park']
    casino = dataframeJSON[dataframeJSON.amenity == 'casino']
    shop = dataframeJSON[dataframeJSON.amenity == 'shop|clothes']


    place_attractions = pd.concat([art_center, cinema, college, theatre, university, spa, park, casino, shop])

    #filtered restaurant data
    asian_food_list = ['chinese', 'northern chinese', 'hong kong cafe', 'thai', 'ramen', 'indonesian',
                       'sushi_and_other_japanese_cuisine_including_bento_boxes_with_teriyaki_and_tempura.', 'korean',
                       'japanese', 'vietnamese', 'cambodian', 'burmese', 'vietnamese', 'poke', 'udon', 'vietnamese_subs',
                       'noodles', 'singaporean', 'indian', 'hong kong style cafe', 'noodle', 'asian', 'gyoza', 'curry',
                       'shanghainese', 'taiwanese', 'sushi', ' sushi', 'buddhist', 'rice', 'indian_vegetarian', 'pan asian'
                       ,'filipino', 'mongolian', 'thai', 'malaysian', 'sashimi', 'buddhist vegetarian']
    middle_eastern_food_list = ['afghan', 'falafel', 'lebanese', 'donair', 'turkish', 'middle_eastern', 'currypersian',
                                'cajun', 'kebab', 'arab', 'middle_eastern']
    european_food_list = ['french', 'dutch', 'ukranian', 'italian, pizza, pasta', 'irish', 'german', '_french-inspired_bistro',
                          'portuguese', 'acadian', 'italian', 'italian, pizza, pasta', 'pizza', 'czech']
    mediterranean_food_list = ['mediterranean', 'greek']
    north_american_food_list = ['steak_house', 'american', 'barbecue', 'cuban', 'fish_and_chips', 'poke',
                                'west_coast_food', 'wings', 'canadian', 'cuban', 'burger', 'buffet', 'southern']
    south_american_food_list = ['tapas', 'brazilian', 'taco', 'peruvian', 'salvadorian', 'mexican', 'brazilian', 'jamaican']
    african_food_list = ['moroccan', 'ethiopian']

    dataframe_with_tags = pd.read_json('amenities-vancouver.json.gz', lines=True)
    un_filtered_restaurants = dataframe_with_tags[dataframe_with_tags['amenity'] == 'restaurant']
    un_filtered_restaurants['tags'] = un_filtered_restaurants.apply(extractString, axis=1)
    # https://stackoverflow.com/questions/58528989/pandas-get-unique-values-from-column-of-lists
    # cusine_types = set(itertools.chain.from_iterable(un_filtered_restaurants.tags))
    # print(cusine_types)
    #List of lists check
    #https://stackoverflow.com/questions/43878397/filter-pandas-dataframe-with-nested-arrays
    asian_food_df = un_filtered_restaurants[un_filtered_restaurants['tags'].apply(lambda tag : any(ele in tag for ele in asian_food_list))]
    middle_eastern_food_df = un_filtered_restaurants[un_filtered_restaurants['tags'].apply(lambda tag : any(ele in tag for ele in middle_eastern_food_list))]
    european_food_df = un_filtered_restaurants[un_filtered_restaurants['tags'].apply(lambda tag : any(ele in tag for ele in european_food_list))]
    mediterranean_food_df = un_filtered_restaurants[
        un_filtered_restaurants['tags'].apply(lambda tag: any(ele in tag for ele in mediterranean_food_list))]
    north_american_food_df = un_filtered_restaurants[
        un_filtered_restaurants['tags'].apply(lambda tag: any(ele in tag for ele in north_american_food_list))]
    south_american_food_df = un_filtered_restaurants[
        un_filtered_restaurants['tags'].apply(lambda tag: any(ele in tag for ele in south_american_food_list))]
    african_food_df = un_filtered_restaurants[
        un_filtered_restaurants['tags'].apply(lambda tag: any(ele in tag for ele in african_food_list))]

    cusine_list = pd.concat([asian_food_df, middle_eastern_food_df, european_food_df, south_american_food_df,
                             south_american_food_df, south_american_food_df, african_food_df])
    # categories - restaurants: cafe, ice_cream, restaurants, pub, fast_food, bar, food_court,
    cafe = dataframeJSON[dataframeJSON.amenity == 'cafe']
    ice_cream = dataframeJSON[dataframeJSON.amenity == 'ice_cream']
    restaurants = dataframeJSON[dataframeJSON.amenity == 'restaurant']
    pub = dataframeJSON[dataframeJSON.amenity == 'pub']
    fast_food = dataframeJSON[dataframeJSON.amenity == 'fast_food']
    bar = dataframeJSON[dataframeJSON.amenity == 'bar']
    food_court = dataframeJSON[dataframeJSON.amenity == 'food_court']
    bistro = dataframeJSON[dataframeJSON.amenity == 'bistro']

    place_food = pd.concat([cafe, ice_cream, restaurants, pub, fast_food, bar, food_court, bistro])

    # print(place_food)

    # categories - transits: bicycle_parking, bicyle_rental, car_sharing, car_renting, parking, parking_space, bus_station, fuel, taxi,
    # # ------- bicycle
    # bicycle_parking = dataframeJSON[dataframeJSON.amenity == 'bicycle_parking']
    # bicyle_rental = dataframeJSON[dataframeJSON.amenity == 'bicyle_rental']

    # ------- car
    car_parking = dataframeJSON[dataframeJSON.amenity == 'parking']
    car_parking2 = dataframeJSON[dataframeJSON.amenity == 'parking_space']
    car_fuel = dataframeJSON[dataframeJSON.amenity == 'fuel']

    trans_car = pd.concat([car_parking,car_parking2,car_fuel])
    trans_car_parking = pd.concat([car_parking,car_parking2])
    trans_car_fuel = pd.concat([car_fuel])

    # -------- bus
    bus_station = dataframeJSON[dataframeJSON.amenity == 'bus_station']
    trans_bus = pd.concat([bus_station])

    # print(trans_bus)
    # -------- walk
    stations = pd.read_csv('csv/skytrain.csv')
    trans_walk = pd.concat([stations])


    # -------------------ML: using DBSCAN to groupby places
    db_places = pd.concat([place_food, place_attractions])
    X_train = db_places[['lat', 'lon']]
    model = DBSCAN(eps=0.003, min_samples=25).fit(X_train)
    db_places['data'] = model.labels_
    print('# clusters:', {max(model.labels_)})

    X_asian = asian_food_df[['lat', 'lon']]
    model_asian = DBSCAN(eps=0.003, min_samples=10).fit(X_asian)
    X_asian['data'] = model_asian.labels_

    X_european = european_food_df[['lat', 'lon']]
    model_european = DBSCAN(eps=0.003, min_samples=3).fit(X_european)
    X_european['data'] = model_european.labels_

    X_north_american = north_american_food_df[['lat', 'lon']]
    model_north_american = DBSCAN(eps=0.003, min_samples=3).fit(X_north_american)
    X_north_american['data'] = model_north_american.labels_
    #-------------------------Grouping
   
    group_transit = folium.FeatureGroup(name='transit')
    trans_car.apply(marker, axis = 1, group = group_transit, colour = 'magenta')
    trans_bus.apply(marker, axis = 1, group = group_transit, colour = 'blue')
    trans_walk.apply(marker, axis = 1, group = group_transit, colour = 'maroon')
    
    
    group_place = folium.FeatureGroup(name='place')
    place_attractions.apply(marker, axis = 1, group = group_place, colour = 'blue')
    place_food.apply(marker, axis = 1, group = group_place, colour = 'black')

    group_place_dbscan = folium.FeatureGroup(name='dbscan_place')
    for i in range(max(db_places.data)):
        db_places[db_places.data == i].apply(marker, axis = 1, group = group_place_dbscan, colour = 'red')

    route_car = folium.FeatureGroup(name='route_car')
    trans_car_parking.apply(marker, axis = 1, group = route_car, colour = 'red')
    trans_car_fuel.apply(marker, axis = 1, group = route_car, colour = 'blue', radius = 7)
    for i in range(max(db_places.data)):
        db_places[db_places.data == i].apply(marker, axis = 1, group = route_car, colour = 'grey')
    
    route_bus = folium.FeatureGroup(name='transit')
    trans_bus.apply(marker, axis = 1, group = route_bus, colour = 'red', radius = 7)
    for i in range(max(db_places.data)):
        db_places[db_places.data == i].apply(marker, axis = 1, group = route_bus, colour = 'grey')


    route_walk = folium.FeatureGroup(name='transit')
    trans_walk.apply(marker, axis = 1, group = route_walk, colour = 'red', radius = 7)
    for i in range(max(db_places.data)):
        db_places[db_places.data == i].apply(marker, axis = 1, group = route_walk, colour = 'grey')

    #---- Clustering for asian, european, north american food
    cluster_food = folium.FeatureGroup(name='asian_cluster')
    asian_food_df.apply(marker, axis=1, group=cluster_food, colour='green')
    for i in range(max(X_asian.data)):
        X_asian[X_asian.data == i].apply(marker, axis=1, group=cluster_food, colour='blue')

    cluster_food_two = folium.FeatureGroup(name='european_cluster')
    european_food_df.apply(marker, axis=1, group=cluster_food_two, colour='red')
    for i in range(max(X_european.data)):
        X_european[X_european.data == i].apply(marker, axis=1, group=cluster_food_two, colour='blue')

    cluster_food_three = folium.FeatureGroup(name='north_american_cluster')
    north_american_food_df.apply(marker, axis=1, group=cluster_food_three, colour='orange')
    for i in range(max(X_north_american.data)):
        X_north_american[X_north_american.data == i].apply(marker, axis=1, group=cluster_food_three, colour='blue')

    specific_food = folium.FeatureGroup(name='category_food')
    asian_food_df.apply(marker, axis=1, group=specific_food, colour='green')
    european_food_df.apply(marker, axis=1, group=specific_food, colour='red')
    north_american_food_df.apply(marker, axis=1, group=specific_food, colour='orange')

    middle_eastern_food_df.apply(marker, axis=1, group=specific_food, colour='blue')
    mediterranean_food_df.apply(marker, axis=1, group=specific_food, colour='black')
    south_american_food_df.apply(marker, axis=1, group=specific_food, colour='yellow')
    african_food_df.apply(marker, axis=1, group=specific_food, colour='purple')

    cluster_food_four = folium.FeatureGroup(name='middle_eastern_cluster')
    middle_eastern_food_df.apply(marker, axis=1, group=cluster_food_four, colour='blue')

    cluster_food_five = folium.FeatureGroup(name='mediterranean_cluster')
    mediterranean_food_df.apply(marker, axis=1, group=cluster_food_five, colour='black')

    cluster_food_six = folium.FeatureGroup(name='south_american_food')
    south_american_food_df.apply(marker, axis=1, group=cluster_food_six, colour='yellow')

    cluster_food_seven = folium.FeatureGroup(name='african_food')
    african_food_df.apply(marker, axis=1, group=cluster_food_seven, colour='purple')


    #-------------------------Mapping
    mapping_trans = folium.Map(location=[49.2048, -122.9061],zoom_start=11, tiles='OpenStreetMap')
    mapping_all_trans = mapping_trans.add_child(group_transit)
    mapping_all_trans.save('maps/transit(car,bus,walk).html')

    mapping_place = folium.Map(location=[49.2048, -122.9061],zoom_start=11, tiles='OpenStreetMap')
    mapping_all_place = mapping_place.add_child(group_place)
    mapping_all_place.save('maps/place(amenities,food).html')

    mapping_place_db = folium.Map(location=[49.2048, -122.9061],zoom_start=11, tiles='OpenStreetMap')
    mapping_all_place_db = mapping_place_db.add_child(group_place_dbscan)
    mapping_all_place_db.save('maps/DBSCAN-place(amenities,food).html')

    mapping_place_food = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_food= mapping_place_food.add_child(specific_food)
    mapping_all_food.save('maps/category_food.html')

    mapping_place_asian = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_place_asian = mapping_place_asian.add_child(cluster_food)
    mapping_all_place_asian.save('maps/DBSCAN-asian.html')

    mapping_place_euro = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_euro = mapping_place_euro.add_child(cluster_food_two)
    mapping_all_euro.save('maps/DBSCAN-european.html')

    mapping_place_american = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_american = mapping_place_american.add_child(cluster_food_three)
    mapping_all_american.save('maps/DBSCAN-american.html')

    mapping_place_middle_eastern = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_middle_eastern = mapping_place_middle_eastern.add_child(cluster_food_four)
    mapping_all_middle_eastern.save('maps/middle_eastern_food.html')

    mapping_place_mediterranean = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_mediterranean = mapping_place_mediterranean.add_child(cluster_food_five)
    mapping_all_mediterranean.save('maps/mediterranean_food.html')

    mapping_place_south_american = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_south_american = mapping_place_south_american.add_child(cluster_food_six)
    mapping_all_south_american.save('maps/south_american_food.html')

    mapping_place_african = folium.Map(location=[49.2048, -122.9061], zoom_start=11, tiles='OpenStreetMap')
    mapping_all_african = mapping_place_african.add_child(cluster_food_seven)
    mapping_all_african.save('maps/african_food.html')

    #----------------------Finding Routes

    # 1. Car
    mapping_route = folium.Map(location=[49.2048, -122.9061],zoom_start=11, tiles='OpenStreetMap')
    mapping_route_car = mapping_route.add_child(route_car)
    mapping_route_car.save('maps/route-car.html')

    # 2. Bus
    mapping_route_2 = folium.Map(location=[49.2048, -122.9061],zoom_start=11, tiles='OpenStreetMap')
    mapping_route_bus = mapping_route_2.add_child(route_bus)
    mapping_route_bus.save('maps/route-bus.html')

    # 3. Walk
    mapping_route_3 = folium.Map(location=[49.2048, -122.9061],zoom_start=11, tiles='OpenStreetMap')
    mapping_route_walk = mapping_route_3.add_child(route_walk)
    mapping_route_walk.save('maps/route-walk.html')


if __name__ == '__main__':
    main()
