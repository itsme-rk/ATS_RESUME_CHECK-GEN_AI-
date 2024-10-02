from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr,format='JPEG')
        img_byte_arr=img_byte_arr.getvalue()

        pdf_parts=[
            {
                "mime_type":"image/jpeg",
                "data":base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("NO FILE FOUND/UPLOADED")


st.set_page_config(page_title="ATS RESUME CHECKER")
st.header("ATS TRACKING SYSTEM")
input_text=st.text_area("JOB DESCRIPTION:  ",key="input")
uploaded_file = st.file_uploader("UPLOAD YOUR RESUME in PDF..........",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF UPLOADED SUCCESSFULLY")


submit1 = st.button("TELL ME ABOUT MY RESUME.")

submit2 = st.button("HOW CAN I IMPROVE MY SKILLS AND WHAT ARE THE KEYWORDS THAT ARE MISSING?")

submit3 = st.button("WHAT ARE THE OTHER JOBS THAT THE PERSON CAN APPLY USING THIS RESUME?")

submit4 = st.button("PERCENTAGE MATCH.")




input_prompt1 ="""
Hey there. You are an experienced human research HR Recruiter with a tech experience in the field of data science. web development, 
which includes javascript node Express reactsjs and mongodb and other mern and mean stack also with java development and other fields 
 full stack. And also data engineering, big data engineering, devops ,data analyst and business analyst , ai engineer 
Your task is to review the provided resume against the job description for his profiles Please share your professional evaluation on
  whether The candidates provide profile alignment with the provided Resume  and job Description highlight the Strength and weakens
    of the applicant in realeation to the  specific job desription """

input_prompt2="""
you are an experienced hr recuiter in an reputed company who checks the resumne day in and day out with a tech experience
 in the field of data science. web development, which includes javascript node Express reactsjs and mongodb and other mern 
 and mean stack also with java development and other fields  full stack. And also data engineering, big data engineering, devops 
 ,data analyst and business analyst , ai engineer .Advice a person thinking him as your close releation what are the skill that are missing 
 in the resume according to the job description and how can he/she develop or add those skills . highlight the missing skills.

"""
input_prompt3="""
Hey there. You are an experienced human research HR Recruiter with a tech experience in the field of data science. web development, 
which includes javascript node Express reactsjs and mongodb and other mern and mean stack also with java development and other fields 
 full stack. And also data engineering, big data engineering, devops ,data analyst and business analyst , ai engineer . You are given a resume 
 and now based on the jd provided tell it can be used to get that job? also tell what are the other similar roles and jobs that this resume can be used to get a job and 
 what are the other some additional skills required .


"""


input_prompt4 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts

"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response =get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("THE RESPONSE IS ...")
        st.write(response)
    else:
        st.write("PLEASE UPLOAD THE PDF/resume FILE FIRST")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response =get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("THE RESPONSE IS ...")
        st.write(response)
    else:
        st.write("PLEASE UPLOAD THE PDF/resume FILE FIRST")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response =get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("THE RESPONSE IS ...")
        st.write(response)
    else:
        st.write("PLEASE UPLOAD THE PDF/resume FILE FIRST")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response =get_gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("THE RESPONSE IS ...")
        st.write(response)
    else:
        st.write("PLEASE UPLOAD THE PDF/resume FILE FIRST")