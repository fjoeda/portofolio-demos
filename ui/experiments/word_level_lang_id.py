import streamlit as st
from annotated_text import annotated_text
from libs.shared.text.lang_id import LangIdCRF

tagger = LangIdCRF()


def word_level_lang_id_ui():
    st.title("Word Level Language Identification")
    # st.divider()
    # st.markdown("""

    # """)
    # st.divider()

    text_input = st.text_area("Input text")
    st.write("Tagged result")
    for item in text_input.split("\n"):
        tagged = tagger.tag(item)
        annotated_text(tagged)
