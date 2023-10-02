import streamlit as st
from ui.experiments.food_absa import food_absa_ui
from ui.experiments.word_level_lang_id import word_level_lang_id_ui

params = st.experimental_get_query_params()

if params.get('page', [None])[0] == "food-absa":
    food_absa_ui()
elif params.get('page', [None])[0] == "word-level-lang-id":
    word_level_lang_id_ui()
else:
    st.write("")
