from googletrans import Translator
from googletrans import LANGUAGES
import streamlit as st

st.title("Language Translator")
source_text = st.text_input("Enter the text to translate")

#LANGUAGES is a dictionary that looks like {"fr": "french"}

#Switching key-value pairs and capitalizing new key, "French"
lang_dict = {v.capitalize(): k for k, v in LANGUAGES.items()} 
target_lang = st.selectbox("To:", options = lang_dict.keys())

translate = st.button("Translate")

if translate:
    translator = Translator()
    result = translator.translate(source_text, dest=lang_dict[target_lang])
    st.write(result.text)
