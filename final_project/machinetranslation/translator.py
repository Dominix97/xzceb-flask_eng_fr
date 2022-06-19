"""
Translator Service
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-06-19',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """EN - FR"""
    if len(english_text)==0:
        return "Blank text"
    try:
        translation = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()

        french_text = translation['translations'][0]['translation']
    except ApiException:
        french_text = "Error in translation"

    return french_text

def french_to_english(french_text):
    """FR - EN"""
    if len(french_text)==0:
        return "Blank text"
    try:
        translation = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()

        english_text = translation['translations'][0]['translation']
    except ApiException:
        english_text = "Error in translation"

    return english_text
