# UI Dependencies.
import streamlit as st

# Logic Dependencies.
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="Solvr.ai - PDF Summarizer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="auto"
)

# Logic
# PDF Reader (Text Extractor).
def pdf_reader(pdf_file):
    reader = PdfReader(pdf_file)
    allPages = []

    for i in range(len(reader.pages)):
        allPages.append(reader.pages[i].extract_text())

    allPages = ' '.join(allPages)

    return allPages

# Setting up model for text summarization.
def summarizer(text):
    llm = OpenAI(openai_api_key='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', temperature=0.9)
    template = "You are a master in summarizing long texts. Summarize the following:\n{text}"
    prompt = PromptTemplate.from_template(template)
    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run(text)

    return summary

# UI
st.markdown("<h1 style='text-align: center;'>PDF Summarizer 📄</h1>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose a PDF file", "pdf")
if uploaded_file is not None:
    if st.button('Summmarize!'):
        with st.chat_message("assistant"):
            with st.spinner('Summarizing PDF...'):
                text = pdf_reader(uploaded_file)
                summary = summarizer(text)
            st.write("Here is the summary of the provided PDF!")
            st.markdown(summary)