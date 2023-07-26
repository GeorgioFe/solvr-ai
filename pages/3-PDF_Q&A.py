# UI Dependencies
import streamlit as st

st.set_page_config(
    page_title="Solvr.ai - PDF Q&A",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="auto"
)

st.markdown("<h1 style='text-align: center; vertical-align: middle;'>Stay Tuned! It's coming soon 👀 🏗️.</h1>", unsafe_allow_html=True)

# ## TEST ##
# from langchain.document_loaders import PyPDFLoader
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI

# OPENAI_API_KEY = st.secrets["openai_api_key"]
# llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# file = ""
# loader = PyPDFLoader(file)
# docs = loader.load()

# chain = load_qa_chain(llm=llm, chain_type="map_rerank", verbose=False, return_intermediate_steps=False)
# query = "some question"

# result = chain.run(input_documents=docs, question=query)
# print(result)