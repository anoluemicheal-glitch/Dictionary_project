import streamlit as st

st.set_page_config(page_title="Nigerian Languages Translator")
st.title("Nigerian Languages Translator")
st.write("Translate words from English to a Nigerian language.")

#=====by Matthew Folat======
yoruba_dictionary = {
    "good morning": "ẹ̀káàrọ̀",
    "good afternoon": "ẹ̀káàsán",
    "good evening": "ẹ̀káalẹ́",
    "how are you": "báwo ni",
    "i am fine": "dáadáa ni",
    "house": "ilé",
    "child": "ọmọ",
    "friend": "ọrẹ́",
    "husband": "ọkọ̀",
    "wife": "iyàwó",
    "water": "omi",
    "food": "oúnjẹ",
    "school": "ilé-ẹ̀kọ́",
    "student": "akẹ́kọ̀ọ́",
    "teacher": "olùkọ́",
    "day": "ọjọ́",
    "god": "ọlọ́run",
    "love": "ìfẹ́",
    "market": "ọjà",
    "car": "ọkọ̀ ayọ́kẹ́lẹ́"
}

# ================= Kamsi Divine =================
igala_dictionary = {
    "hello": "adoo",
    "goodbye": "o dabo",
    "thank you": "ojo",
    "please": "joo",
    "yes": "ehe",
    "no": "awo",
    "man": "ono",
    "woman": "iye",
    "child": "oma",
    "food": "eje",
    "water": "omi",
    "house": "ile",
    "road": "ona",
    "market": "oja",
    "money": "owo",
    "friend": "ore",
    "father": "ata",
    "mother": "iya",
    "morning": "ojo-ola",
    "night": "ojo-ane"
}

# ================= Micheal Nnamadi =================
hausa_dictionary = {
    "hello": "sannu",
    "thank you": "nagode",
    "yes": "eh",
    "no": "a'a",
    "good morning": "ina kwana",
    "good afternoon": "ina wuni",
    "good evening": "ina yini",
    "water": "ruwa",
    "food": "abinci",
    "house": "gida",
    "person": "mutum",
    "child": "yaro",
    "woman": "mace",
    "man": "namiji",
    "money": "kudi",
    "market": "kasuwa",
    "road": "hanya",
    "time": "lokaci",
    "work": "aiki",
    "health": "lafiya"
}

# ================= Chidi Emmanuel =================
igbo_dictionary = {
    "hello": "ndeewo",
    "how are you": "kedu",
    "please": "biko",
    "thank you": "daalu",
    "welcome": "nnoo",
    "water": "mmiri",
    "food": "nri",
    "house": "ulo",
    "wealth": "aku",
    "land": "ala",
    "money": "ego",
    "book": "akwukwo",
    "man": "nwoke",
    "woman": "nwanyi",
    "child": "nwa",
    "day": "ubochi",
    "night": "abali",
    "friend": "enyi",
    "fish": "azu",
    "eye": "anya"
}

# ================= God's word =================
efik_dictionary = {
    "good morning": "m̀bọ̀rọ̀ úyọ̀",
    "good afternoon": "m̀bọ̀rọ̀ ẹ̀títí",
    "good night": "m̀bọ̀rọ̀ úkúm",
    "mother": "ekame",
    "book": "akpa akwụkwọ",
    "phone": "fọn",
    "teacher": "nkọñọ",
    "car": "mọ́tò",
    "god": "abasi",
    "dog": "nkpọ́",
    "water": "mmi",
    "hand": "ikọ́",
    "leg": "ekpẹ́",
    "prayer": "nsọ́ọ̀fọ̀",
    "food": "ịdọ́ñ",
    "cloth": "uto",
    "family": "ufọk",
    "animal": "nkpọ̀ñ",
    "thanks": "ẹsé",
    "child": "ndịọ́bó"
}

# ================= LANGUAGE LINK =================
languages = {
    "Yoruba": yoruba_dictionary,
    "Igala": igala_dictionary,
    "Hausa": hausa_dictionary,
    "Igbo": igbo_dictionary,
    "Efik": efik_dictionary
}

# ================= STREAMLIT UI =================
target_language = st.selectbox("Select Target Language", list(languages.keys()))
dictionary = languages[target_language]

english_word = st.text_input("Enter an English word to translate")

if english_word:
    clean_word = english_word.strip().lower()

    if clean_word in dictionary:
        st.success(f"English: {clean_word} → {target_language}: {dictionary[clean_word]}")
    else:
        st.error("Word not found in dictionary")







