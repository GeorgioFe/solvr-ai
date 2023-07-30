# UI Dependencies
import streamlit as st
from PIL import Image

# Page Configuration.
favicon = Image.open("./admin/branding/logos/favicon-32x32.png")
st.set_page_config(
    page_title="Solvr.ai - Image Generation",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("<h1 style='text-align: center; vertical-align: middle;'>Stay Tuned! It's coming soon 👀 🏗️.</h1>", unsafe_allow_html=True)