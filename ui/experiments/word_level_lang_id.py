import streamlit as st
from annotated_text import annotated_text
from libs.shared.text.lang_id import LangIdCRF
import plotly.express as px

tagger = LangIdCRF()


def word_level_lang_id_ui():
    st.title("Word Level Language Identification")
    text_input = st.text_area("Input text")
    all_tagged = []
    lang_list = {}

    for item in text_input.split("\n"):
        tagged = tagger.tag(item)
        all_tagged.append(tagged)
        for tag in tagged:
            if tag[1] not in lang_list.keys():
                lang_list[tag[1]] = 1
            else:
                lang_list[tag[1]] += 1

    pie_plot = px.pie(names=lang_list.keys(), values=lang_list.values())

    st.write("#### Language composition")
    st.plotly_chart(pie_plot)

    st.write("#### Tagged result")
    for tagged in all_tagged:
        annotated_text(tagged)
