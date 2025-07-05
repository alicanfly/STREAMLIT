import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon=":book:", layout="centered")

st.title("AI Resume Critiquer")

st.markdown("Upload yoour Resume and get an AI powerred feedback")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your PDF/ TXT Resume", type=["pdf", "txt"])

job_role = st.text_input("Enter the job role you're applying for", placeholder="e.g. Software Engineer, Data Scientist")

analyze = st.button("Analyze Resume")


def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    try:
        return uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        # Try a fallback encoding
        return uploaded_file.read().decode("latin-1")


if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("The uploaded file does not have any content")
            st.stop()

        prompt = f"""Please analyze this resume and provide a constructive feedback.
        Focus on the following aspects:
        1. Content Quality: Is the information relevant to the job role?
        2. Skills Presentation
        3. Experience Description: Are the experiences well described?
        4. Specifgic Improvements for {job_role if job_role else 'genera; job applications'}

        Resume Content:
        {file_content}

        Please provide your feedback in a clear and concise manner.
        """

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer with years in HR and Recruitment."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        st.markdown("### AI Feedback")
        st.markdown(response.choices[0].message.content)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.stop()