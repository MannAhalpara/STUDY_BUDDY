# AI Study Buddy

An AI-powered Study Buddy application built with Streamlit and Google Gemini API. This tool helps students understand topics, summarize notes, and generate quizzes or flashcards instantly.

## Features

1.  **Explain Topic**: Get simple, beginner-friendly explanations with examples.
2.  **Summarize Notes**: Condense long notes into clear bullet points.
3.  **Generate Quiz**: Create 5 quiz questions based on your study material.
4.  **Generate Flashcards**: Generate Q&A flashcards for quick revision.
5.  **PDF Support** : Upload lecture notes or study materials in PDF format to use as a source for any of the features.
6.  **Download Results** : Export the generated AI content as a .txt file for offline use.
## Setup Instructions

### 1. Prerequisities
- Python 3.8 or higher
- A Google Gemini API Key

### 2. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory and add your API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Running the App
Launch the Streamlit application:
```bash
streamlit run app.py
```

## Technology Stack
- **Frontend/Backend**: Python, Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **PDF Processing** : PyPDF2
- **Dependencies**: `google-generativeai`, `python-dotenv`, `PyPDF2`, `streamlit`
