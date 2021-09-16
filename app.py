import streamlit as st
from nltk.corpus import words
import itertools
import time
import pandas as pd

english_dict = pd.read_json('https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json', orient="index").to_dict(orient="index")
english_words = set(english_dict.keys())
# english_words = set(words.words())

letters = None
_, col1, _ = st.sidebar.beta_columns(3)
l1 = col1.text_input('Letter 1')
col2, _, col3 = st.sidebar.beta_columns(3)
l2 = col2.text_input('Letter 2')
l3 = col3.text_input('Letter 3')
_, col4, _ = st.sidebar.beta_columns(3)
cl = col4.text_input('Center Letter')
col5, _, col6 = st.sidebar.beta_columns(3)
l4 = col5.text_input('Letter 4')
l5 = col6.text_input('Letter 5')
_, col7, _ = st.sidebar.beta_columns(3)
l6 = col7.text_input('Letter 6')
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(204, 49, 49);
    position: relative;
    left: 40%;
    width: 20%;
    border-radius: 20px;
}
</style>""", unsafe_allow_html=True)
if st.sidebar.button('Go'):
    letters = [l1, l2, l3, l4, l5, l6, cl]
    st.markdown('### Getting combinations and permutations...')
    viable_words = []
    t = st.empty()
    for i in range(4, len(letters)+2):
        for p in itertools.product(letters, repeat=i):
            if cl in p and ''.join(p).lower() in english_words:
                viable_words.append(''.join(p))
                t.markdown("#### %s..." % ", ".join(viable_words))
                time.sleep(0.15)