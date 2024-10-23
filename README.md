
# PDF Text Extractor

A simple web application that allows users to upload a PDF document and extract its text content. Built with Streamlit and pdfplumber, this app provides an easy-to-use interface for reading and extracting text from PDF files.

## Table of Contents

- [Project Summary](#project-summary)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Summary

This project is designed to help users extract text from PDF files effortlessly. Whether you need to retrieve text for documentation, research, or any other purpose, this app provides a straightforward solution. Users can simply upload their PDF files, and the app will display the extracted text, making it accessible for copying or further analysis.

## Features

- **Upload PDF Files**: Users can easily upload their PDF documents.
- **Text Extraction**: The app extracts and displays the text from the uploaded PDF.
- **User-Friendly Interface**: Built using Streamlit, the app is intuitive and responsive.
- **Cross-Platform Compatibility**: Works on any platform that supports Streamlit.

## Technologies Used

- [Streamlit](https://streamlit.io/): A Python library for creating web apps.
- [pdfplumber](https://github.com/jsvine/pdfplumber): A Python library for extracting text and information from PDF files.
- Python 3.x

## Installation

To run the application locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your_username/PDF-to-text.git
   cd PDF-to-text
   ```

2. **Create a virtual environment (optional but recommended)**:

   - **Windows**:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **macOS/Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501` to access the app.

3. **Upload a PDF file** using the provided file uploader.

4. **View the extracted text** displayed on the screen for your convenience.

5. **Copy or save the extracted text** for your use as needed.

## Deployment

This application is also deployed on [Streamlit Cloud](https://streamlit.io/cloud). You can access the live version of the app at [your_deployed_app_link].

### Deploying on Streamlit Cloud

To deploy your app on Streamlit Cloud, follow these steps:

1. **Push your code to a GitHub repository**:
   - Make sure your app is working locally.
   - Commit your changes and push them to GitHub.

2. **Sign in to Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with your GitHub account.

3. **Create a New App**:
   - Click on "New App" in the Streamlit Cloud dashboard.
   - Select the GitHub repository you just pushed your code to.

4. **Select the branch** (usually `main`) and specify the file path to `app.py`.

5. **Click on "Deploy"** to publish your app.

---