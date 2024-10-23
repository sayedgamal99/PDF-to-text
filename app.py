import streamlit as st
import pdfplumber

# App Title
st.title("PDF Text Extractor")

# Instructions
st.write("Upload a PDF file and extract its text content.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Display the uploaded file name
    st.write(f"Uploaded file: {uploaded_file.name}")
    
    # Extract text using pdfplumber
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    
    # Display extracted text
    st.subheader("Extracted Text:")
    st.text_area("Text Content", text, height=300)

