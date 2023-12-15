import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {

background-image: url("https://media.istockphoto.com/id/1398608628/photo/futuristic-technology-wave-digital-cyberspace-abstract-wave-with-moving-particles-on.jpg?s=612x612&w=0&k=20&c=fGOs-wXs2TWPLao0G_aZVJNzsJhuaI9p2fl8p7IAfz8=");
background-size: cover;
}


"""

st.markdown(page_bg_img, unsafe_allow_html=True)

from predict_page import show_predict_page
show_predict_page()

