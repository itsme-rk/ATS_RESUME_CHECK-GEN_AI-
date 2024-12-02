ATS Resume Checker
An interactive web application that helps users analyze their resumes against job descriptions and provides actionable feedback using Google Gemini AI.

Features
Upload Resume: Upload a PDF version of your resume for analysis.
Job Description Matching: Input a job description to evaluate how well your resume aligns.
AI-Powered Insights: Get suggestions for improving skills, keywords, and formatting.
Resume Score Breakdown: View detailed scores for skills, experience, keywords, and formatting.
Job Recommendations: Receive tailored job suggestions based on your resume.
Interview Tips: Get AI-generated tips to improve your chances of success.
Dark Mode Toggle: Switch between light and dark themes for better readability (optional).
Technology Stack
Frontend: Streamlit for user interface.
Backend: Python (PIL, pdf2image) for processing.
AI: Google Gemini AI for content generation.
Deployment: GitHub for version control.
Installation
Clone the repository:


git clone https://github.com/your-username/ats-resume-checker.git  
cd ats-resume-checker  
Install dependencies:


pip install -r requirements.txt  
Set up environment variables:

Create a .env file in the root directory.
Add your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key  
Run the application:



streamlit run app.py  
Usage
Upload Your Resume: Click on the “Upload Resume” button and select a PDF file.
Enter Job Description: Paste the job description in the text area provided.
Select Analysis Option: Choose from Resume Breakdown, Job Recommendations, or Interview Tips.
View Results: AI-generated feedback and score breakdown will be displayed.
Prompts Used
Resume Breakdown: Focuses on strengths, weaknesses, and recommendations for improvement.
Job Recommendations: Highlights alternative job roles and skill gaps.
Interview Tips: Provides tailored advice for interview preparation.
Contributing
Feel free to submit issues or pull requests for improvements.

Acknowledgements
Streamlit for the web framework.
Google Gemini AI for content generation.
pdf2image for PDF processing.
