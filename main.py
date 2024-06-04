import streamlit as st
import os
from google.cloud import translate_v2 as translate
import json

# Load Google Cloud credentials from Streamlit secrets
gcp_credentials = dict(st.secrets["gcp"])  # Convert AttrDict to a regular dictionary
gcp_credentials_path = "gcp_credentials.json"

# Write credentials to a temporary file
with open(gcp_credentials_path, "w") as f:
    json.dump(gcp_credentials, f)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = gcp_credentials_path

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

input_text = st.text_area("Enter Shona text to translate:")

if st.button("Translate"):
    translation = translate_shona_to_english(input_text)
    st.write("Translated text:", translation)
