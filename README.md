# AI Resume Reviewer & Improver

An intelligent resume review system built with the OpenAI Agents SDK. The system analyzes resumes, provides structured feedback, suggests improvements, and remembers past interactions to give personalized advice over time.

# Features
- **Resume Analysis** — scores your resume out of 10, identifies strengths, weaknesses, and missing keywords
- **ATS Compatibility Check** — evaluates how well your resume performs with Applicant Tracking Systems
- **Improvement Suggestions** — rewrites your summary, improves bullet points, and suggests skills to add
- **Conversation Memory** — remembers your past sessions and builds on previous feedback
- **Multi-Agent System** — Orchestrator, Resume Analyzer, and Improvement Agent working together
- **Gradio UI** — clean web interface with optional job description input

# Tech Stack

- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [Gradio](https://gradio.app/)
- [Pydantic](https://docs.pydantic.dev/)
- Python 3.11

---

# Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-reviewer.git
cd ai-resume-reviewer
```

### 2. Create and activate virtual environment
```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key
Create a `.env` file in the root folder:
OPENAI_API_KEY=your_openai_api_key_here

### 5. Run the app
```bash
python3 ui/app.py
```

Open the local URL shown in the terminal (e.g. `http://127.0.0.1:7860`)

---

## How to Use

1. Paste your resume text in the left panel
2. Optionally paste a job description for tailored feedback
3. Click **Review My Resume**
4. Get structured analysis and improvement suggestions on the right
5. Submit again to get feedback that builds on your previous session
6. Click **Clear Memory** to start a fresh session

---
