# UI Dependencies
import streamlit as st
from PIL import Image

# Logic Dependencies
import openai

# Page Configuration.
favicon = Image.open("./admin/branding/logos/favicon-32x32.png")
st.set_page_config(
    page_title="Solvr.ai - Image Generation",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("<h1 style='text-align: center; vertical-align: middle;'>Stay Tuned! It's coming soon 👀 🏗️.</h1>", unsafe_allow_html=True)

# ## Testing DALL-E
# def create_image(prompt):
#     openai.api_key = st.secrets['openai_api_key']
#     response = openai.Image.create(
#         prompt=prompt,
#         n=1,
#         size="1024x1024"
#     )

#     img_url = response['data'][0]['url']

#     return img_url

# print(create_image("A painting of a cat sitting on a chair."))



