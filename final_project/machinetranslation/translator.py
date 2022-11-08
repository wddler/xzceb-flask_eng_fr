"""
This program contains functions to translate text using IBM Watson API.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def englishToFrench(englishText):
    """Translates text from English to French"""
    if len(englishText) == 0:
        return 'Error: No text provided for translation'
    response = LANGUAGE_TRANSLATOR.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = response["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    """Translates text from French to English"""
    if len(frenchText) == 0:
        return 'Error: No text provided for translation'
    response = LANGUAGE_TRANSLATOR.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = response["translations"][0]["translation"]
    return englishText
