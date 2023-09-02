'''
Author: Georgio Feghali
Date: July 11 2023
'''

import streamlit as st
from streamlit_card import card
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

favicon = Image.open("admin/branding/logos/favicon-32x32.png")
st.set_page_config(
    page_title="solvr.ai",
    page_icon=favicon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("<h1 style='font-size:60px'><font color='#FF4B4B'>so\\vr.ai</font></h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
  pdf_summarizer = card(
    title="🤖",
    text="Chat Assistant",
    key=1,
    styles={
      "card": {
          "width": "200px",
          "height": "200px",
          "border-radius": "10px",
          "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
          "background-color": "#3e3e42"
      }
    },
    on_click=lambda: switch_page("Chat Assistant")
  )

  pdf_summarizer = card(
    title="🖼️",
    text="Image Generator",
    key=4,
    styles={
      "card": {
          "width": "200px",
          "height": "200px",
          "border-radius": "10px",
          "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
          "background-color": "#3e3e42",
          "border-color": "#FF4B4B",
          "border-width": "20px"
      }
    },
    on_click=lambda: switch_page("Image Generation")
  )



with col2:
  pdf_summarizer = card(
    title="📄",
    text="PDF Summarizer",
    key=2,
    styles={
      "card": {
          "width": "200px",
          "height": "200px",
          "border-radius": "10px",
          "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
          "background-color": "#3e3e42",
          "border-color": "#FF4B4B",
          "border-width": "20px"
      }
    },
    on_click=lambda: switch_page("Pdf Summarizer")
  )

with col3:
  pdf_summarizer = card(
    title="❓",
    text="PDF Q&A",
    key=3,
    styles={
      "card": {
          "width": "200px",
          "height": "200px",
          "border-radius": "10px",
          "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
          "background-color": "#3e3e42",
          "border-color": "#FF4B4B",
          "border-width": "20px"
      }
    },
    on_click=lambda: switch_page("PDF Q&A")
  )

# if pdf_summarizer:
    