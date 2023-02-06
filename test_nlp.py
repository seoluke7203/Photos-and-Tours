from spacy_langdetect import LanguageDetector
from spacy.language import Language
import spacy
nlp = spacy.load('en_core_web_sm')  # 1

def create_lang_detector(nlp, name):
    return LanguageDetector()

Language.factory("language_detector", func=create_lang_detector)
nlp.add_pipe("language_detector", name='language_detector', last=True)  # 2

def process_nlp(name):
    if type(name) != str:
        return 'N/A'
    doc = nlp(name) #3
    detect_language = doc._.language #4

    return [detect_language['language']]


