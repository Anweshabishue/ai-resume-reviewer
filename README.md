# 📄 AI Resume Reviewer

An AI-powered resume analysis tool that reviews resumes and provides actionable feedback to improve ATS compatibility and job readiness.

## 🚀 Features

- Upload resume in PDF format
- Extract text automatically from the uploaded resume
- Analyze resume using AI
- ATS score breakdown
- Review resume format and structure
- Resume Match Score with Job Description
- Matching Skills Identification
- Missing Skills & Keywords Detection
- Analyze technical and soft skills
- Evaluate projects and experience sections
- Download review results as a markdown file

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Llama Model
- PyPDF2
- python-dotenv
- Git & GitHub

## 📂 Project Structure

```text
resume_reviewer/
│
├── app.py
├── core.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── prompts/
│   └── review.txt
│
├── .env
└── venv/
```


## 📸 Application Preview

1. Upload a PDF resume.
2. Optionally enter a target job role.
3. Optionally paste a job description.
4. The application extracts the resume text.
5. The Groq LLM analyzes the resume.
6. The application generates:
   - ATS Score
   - Resume Match Score
   - Skills Analysis
   - Missing Keywords
   - Recruiter's Feedback
   - Interview Readiness Score
   - Resume Improvement Suggestions

## 🔮 Future Improvements

- Multiple resume templates
- Resume rewriting suggestions
- Export review as PDF

## 👩‍💻 Author

**Anwesha Bishue**


