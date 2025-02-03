from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import io
import base64
from PIL import Image 
import pdf2image 
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, pdf_content, job_desc):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([input_prompt, pdf_content[0], job_desc])
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read()) 
        first_page = images[0] 

        img_byte_arr = io.BytesIO() 
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue() 

        pdf_parts = [{
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()
        }]

        return pdf_parts 
    else:
        return None

# Streamlit UI
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Resume Expert")
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("✅ PDF Uploaded Successfully!")

# Submit Buttons
submit1 = st.button("Tell Me About My Resume")
submit2 = st.button("How Can I Improve My Skills")
submit3 = st.button("What Keywords Am I Missing?")
submit4 = st.button("Percentage Match")
submit5 = st.button("Personalized Learning Path")

# **Corrected Input Prompts**
input_prompt1 = """
You are an experienced HR with technical expertise in Data Science, Full Stack, Web Development, Big Data Engineering, DevOps, or Data Analysis.
Your task is to review the provided resume against the job description.
Provide an evaluation on whether the candidate's profile aligns with the specified job role, highlighting strengths and weaknesses.
"""

input_prompt2 = """
You are a career advisor and technical expert. Your task is to analyze the resume and suggest areas where the candidate can improve their skills.
Provide a structured learning approach and recommend practical steps to enhance career growth.
"""

input_prompt3 = """
You are an advanced ATS (Applicant Tracking System) scanner.
Analyze the resume and **extract missing keywords and skills** that are present in the job description but absent in the resume.
Provide a detailed list of missing or weakly mentioned keywords.
"""

input_prompt4 = """
You are an ATS scanner and job match expert.
Evaluate the resume against the job description and provide:
1. **The percentage match** between the resume and job description.
2. **A short explanation** of why the resume matches or does not match.
3. **Key strengths and gaps** based on the job requirements.
"""

input_prompt5 = """
You are a career strategist and learning path expert.
Based on the resume and job description, create a **6-month personalized study plan** to improve the candidate’s chances of getting hired.
Include:
- Monthly skill development goals.
- Learning resources (books, courses, tutorials).
- Suggested hands-on projects.
- Milestones for tracking progress.
"""

# Handling Button Click Events
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Resume Evaluation")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Skill Improvement Suggestions")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Missing Keywords Analysis")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume.")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("Resume Percentage Match")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume.")

elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt5, pdf_content, input_text)
        st.subheader("Personalized Learning & Job Path")
        st.write(response)
    else:
        st.warning("⚠️ Please upload your resume.")