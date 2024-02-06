import streamlit as st
import pandas as pd
import pdfplumber
import io

# Helper function to display PDF
def display_pdf(file):
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            st.write(page.extract_text())

# Title of the app
st.title('OpenAI Simulation')

# Header
st.header('Welcome to OpenAI')

# Introduction or Main Text
st.write('OpenAI is an AI research and deployment company. Our mission is to ensure that artificial general intelligence benefits all of humanity.')

# Image
st.image('SRIDEVI.jpg', caption='OpenAI Illustration')

# Research Section with File Uploader
st.subheader('Research')
uploaded_file_research = st.file_uploader("Upload Research Documents", type=['txt', 'pdf'], key='research')
if uploaded_file_research:
    if uploaded_file_research.type == "application/pdf":
        display_pdf(uploaded_file_research)
    else:
        st.text_area("Text Contents", uploaded_file_research.read().decode("utf-8"), height=300)

# API Section with File Uploader
st.subheader('API')
uploaded_file_api = st.file_uploader("Upload API Documents", type=['txt', 'pdf'], key='api')
if uploaded_file_api:
    if uploaded_file_api.type == "application/pdf":
        display_pdf(uploaded_file_api)
    else:
        st.text_area("Text Contents", uploaded_file_api.read().decode("utf-8"), height=300)

# ChatGPT Section with File Uploader
st.subheader('ChatGPT')
uploaded_file_chatgpt = st.file_uploader("Upload ChatGPT Documents", type=['txt', 'pdf'], key='chatgpt')
if uploaded_file_chatgpt:
    if uploaded_file_chatgpt.type == "application/pdf":
        display_pdf(uploaded_file_chatgpt)
    else:
        st.text_area("Text Contents", uploaded_file_chatgpt.read().decode("utf-8"), height=300)

# Contact Section
st.subheader('Contact')
st.write('For more information, please reach out to us at contact@openai.com.')
