from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get AI response
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

# Function to process PDF and extract first page as image
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded. Please upload a PDF file.")

# Set up page configuration
st.set_page_config(page_title="ATS Resume Checker", page_icon="📄", layout="wide")

# Add header and introduction
st.title("📄 ATS Resume Checker")
st.write("""
Welcome to the **ATS Resume Checker**! This tool helps you analyze your resume against job descriptions 
and provides feedback on improvements, keyword suggestions, and more.
""")

# Dark mode toggle
# dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
# if dark_mode:
#     st.markdown(
#         """<style>body { background-color: #0e1117; color: white; }</style>""", unsafe_allow_html=True
#     )

# Layout: Job description and file upload in two columns
col1, col2 = st.columns(2)

with col1:
    input_text = st.text_area("💼 Enter Job Description:", height=250)

with col2:
    uploaded_file = st.file_uploader("📁 Upload Your Resume (PDF only):", type=["pdf"])

# Buttons for different analysis options
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

submit1 = col1.button("📊 Resume Breakdown")
submit2 = col2.button("💼 Job Recommendations")
submit3 = col3.button("📝 Interview Tips")
submit4 = col4.button("📋 ATS Match Analysis")  

# Scoring function for resume
def score_resume():
    return {"Skills": 85, "Experience": 90, "Keywords": 80, "Formatting": 75}

# Function to display AI response and score breakdown
def display_response(prompt):
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, prompt)
        st.subheader("🔍 AI Response")
        st.write(response)

        # Display score breakdown
        st.subheader("📊 Resume Score Breakdown")
        scores = score_resume()
        st.write(f"**Skills:** {scores['Skills']}%")
        st.write(f"**Experience:** {scores['Experience']}%")
        st.write(f"**Keywords:** {scores['Keywords']}%")
        st.write(f"**Formatting:** {scores['Formatting']}%")
    else:
        st.warning("⚠️ Please upload a resume file before proceeding.")

# Prompts for AI responses
input_prompt1 = """You are an experienced HR recruiter specializing in technical roles across data science, web development, and DevOps. Your task is to review a candidate's resume based on the provided job description.

Provide a detailed evaluation covering:
1. **Strengths**: Highlight areas where the candidate excels, including technical skills, relevant experience, and notable achievements.
2. **Weaknesses**: Identify gaps in skills, experience, or certifications, and suggest improvements.
3. **ATS Compatibility**: Assess how well the resume matches the job description in terms of keywords and format.
4. **Recommendations**: Offer actionable advice to improve the candidate's chances of being shortlisted, including specific skills to add, courses to take, or projects to showcase.
5. **Final Verdict**: Conclude with an overall rating and whether the candidate is a strong fit for the role.

Make sure to include both positive and constructive feedback while maintaining a professional and encouraging tone.
"""
input_prompt2 = """You are an experienced HR recruiter and career advisor specializing in evaluating technical resumes for roles in data science, software development, DevOps, and business analytics.

Your task is to review the candidate's resume against the provided job description and:
1. **Identify Skill Gaps**: Highlight any missing skills, certifications, or technical proficiencies essential for the job.
2. **Tailored Recommendations**: Suggest specific tools, technologies, or programming languages the candidate should learn, along with relevant online courses or certifications.
3. **Career Development Advice**: Offer practical advice on gaining hands-on experience through projects, internships, or contributions to open-source communities.
4. **Keyword Optimization**: List key terms and phrases that should be added to the resume to enhance ATS compatibility and improve the chances of being shortlisted.

Be detailed in your suggestions, and maintain an encouraging, supportive tone throughout the response.
"""
input_prompt3 = """You are an experienced HR recruiter and career consultant with expertise in evaluating resumes for roles in data science, web development, DevOps, and business analytics.

Your task is to:
1. **Assess Resume Fit**: Analyze the candidate's resume against the provided job description to determine suitability for the role.
2. **Suggest Alternative Roles**: Identify other job roles or positions that align with the candidate's skills and experience. These may include related fields or roles with transferable skills.
3. **Highlight Skill Enhancements**: Recommend additional skills, certifications, or experiences that could open up more job opportunities for the candidate.
4. **Provide Career Insights**: Share insights on the current job market, trends, and in-demand roles the candidate should explore.

Maintain a supportive and professional tone, ensuring your feedback is actionable and motivational.
"""
input_prompt4 = """You are a highly skilled ATS (Applicant Tracking System) evaluator with expertise in analyzing resumes for technical roles in data science, software engineering, and related fields.

Your task is to:
1. **Match Evaluation**: Analyze the resume against the provided job description and calculate the **percentage match** based on skills, keywords, and experience alignment.
2. **Keyword Analysis**: Identify missing or underutilized keywords that are critical for passing ATS screening.
3. **Feedback**: Provide actionable feedback on how to improve the resume's match percentage by adding relevant skills, rephrasing content, or improving formatting.
4. **Final Thoughts**: Share a concise summary of the candidate's overall fit for the role and whether their resume is likely to pass an ATS check.

Ensure the feedback is clear, detailed, and actionable to help the candidate improve their chances of being shortlisted.
"""

# Handle button clicks
if submit1:
    display_response(input_prompt1)
elif submit2:
    display_response(input_prompt2)
elif submit3:
    display_response(input_prompt3)
elif submit4:
    display_response(input_prompt4)