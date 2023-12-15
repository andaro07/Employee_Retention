import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #0f0f0f;
}
</style

"""

st.markdown(page_bg_img, unsafe_allow_html=True)

from predict_page import show_predict_page
show_predict_page()

