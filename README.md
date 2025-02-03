# ATS Resume Expert

## Overview
**ATS Resume Expert** is a Streamlit-based application that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS). It utilizes Google's Gemini AI model to analyze resumes, compare them with job descriptions, and provide actionable feedback.

## Features
- **Resume Evaluation:** Assess resume alignment with the job description.
- **Skill Improvement Suggestions:** Get personalized recommendations for skill enhancement.
- **Keyword Optimization:** Identify missing keywords crucial for ATS.
- **Percentage Match:** Calculate how well a resume fits a job description.
- **Personalized Learning Path:** Receive a structured 6-month plan for career growth.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.10
- Streamlit
- Poppler (for PDF processing)

### Step 1: Clone the Repository
```sh
git https://github.com/poojasambhwani/ats-resume-expert.git
cd ats-resume-expert
```

### Step 2: Set Up a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file and add your **Google Gemini API Key**:
```sh
GOOGLE_API_KEY=your_api_key_here
```

### Step 5: Run the Application
```sh
streamlit run app.py
```

## Usage
1. **Upload your resume** in PDF format.
2. **Enter the job description** in the text area.
3. **Click the desired analysis button:**
   - "Tell Me About My Resume"
   - "How Can I Improve My Skills"
   - "What Keywords Am I Missing?"
   - "Percentage Match"
   - "Personalized Learning Path"
4. **View AI-generated insights** and optimize your resume accordingly.

## Dependencies
- `streamlit`
- `pdf2image`
- `Pillow`
- `google-generativeai`
- `python-dotenv`

## Troubleshooting
### Poppler Not Found Error
If you get an error related to Poppler, install it:
- **Windows:** Download from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases) and add to PATH.
- **Mac:** Install via Homebrew:
  ```sh
  brew install poppler
  ```
- **Linux:** Install via APT:
  ```sh
  sudo apt install poppler-utils
  ```

## License
This project is licensed under the MIT License. Feel free to modify and distribute it.

## Contributors
- **Your Name** ([@poojasambhwani](https://github.com/poojasambhwani))

## Future Enhancements
- Support for DOCX resume files.
- More AI-powered resume insights.
- Multilingual support for job descriptions.

## Acknowledgments
- Google's **Gemini AI** for content generation.
- Streamlit for making UI development seamless.

