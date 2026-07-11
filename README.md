# 📄 AI Resume Reviewer

An AI-powered resume analysis tool that reviews resumes and provides actionable feedback to improve ATS compatibility and job readiness.

## 🚀 Features

- Upload resume in PDF format
- Extract text automatically from the uploaded resume
- Analyze resume using AI
- ATS score breakdown
- Review resume format and structure
- Identify missing keywords
- Analyze technical and soft skills
- Evaluate projects and experience sections
- Download review results as a markdown file
- Optional target job role for personalized feedback

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

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Anweshabishue/ai-resume-reviewer.git
cd ai-resume-reviewer
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## 📸 Application Preview

Upload your resume and receive AI-generated feedback including:

- ATS Score
- Resume Format Analysis
- Missing Keywords
- Skills Evaluation
- Project Assessment
- Suggestions for Improvement

## 🔮 Future Improvements

- Support for DOCX resumes
- Job description matching
- Resume keyword optimization
- Multiple resume templates
- Resume rewriting suggestions
- Export review as PDF

## 👩‍💻 Author

**Anwesha Bishue**

MCA Student | Python Developer | AI Enthusiast

GitHub: https://github.com/Anweshabishue
