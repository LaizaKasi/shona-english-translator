# app.py

import streamlit as st
import os
from google.cloud import translate_v2 as translate

# Set up Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'abc.json'

# Define translation function
def translate_shona_to_english(text):
    if isinstance(text, str) and text.strip() != '':
        # Initialize the Google Translate client
        translate_client = translate.Client()
        result = translate_client.translate(text, source_language='sn', target_language='en')
        return result['translatedText']
    return ''

# Streamlit UI
st.title('Shona to English Translator')

# Input field for Shona text
shona_text = st.text_area("Enter Shona text here:")

# Translate button
if st.button('Translate'):
    if shona_text:
        translated_text = translate_shona_to_english(shona_text)
        st.write("English translation:", translated_text)
    else:
        st.warning("Please enter some Shona text.")
