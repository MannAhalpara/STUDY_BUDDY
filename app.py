import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2

# -----------------------
# Load environment
# -----------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="AI Study Buddy",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
<style>

.big-title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

.result-box {
    background-color: #f6f8fa;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("AI Study Buddy")

feature = st.sidebar.radio(
    "Select Feature",
    [
        "Explain Topic",
        "Summarize Notes",
        "Generate Quiz",
        "Generate Flashcards"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Model: Gemini 2.5 Flash")

# -----------------------
# Header
# -----------------------
st.markdown('<p class="big-title">AI Study Buddy</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI assistant for explanations, summaries, quizzes, and flashcards</p>', unsafe_allow_html=True)

# -----------------------
# PDF reader
# -----------------------
def read_pdf(file):

    text = ""

    pdf_reader = PyPDF2.PdfReader(file)

    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text

# -----------------------
# Feature UI
# -----------------------

if feature == "Explain Topic":

    st.subheader("Explain a Topic")

    user_input = st.text_input(
        "Enter topic",
        placeholder="Example: Machine Learning"
    )

elif feature == "Summarize Notes":

    st.subheader("Summarize Notes")

    user_input = st.text_area(
        "Paste notes",
        height=200
    )

elif feature == "Generate Quiz":

    st.subheader("Generate Quiz")

    user_input = st.text_input(
        "Enter topic",
        placeholder="Example: Operating Systems"
    )

elif feature == "Generate Flashcards":

    st.subheader("Generate Flashcards")

    user_input = st.text_area(
        "Enter topic or notes",
        height=200
    )

# -----------------------
# File upload in main area
# -----------------------
st.markdown("### Upload PDF (optional)")

uploaded_pdf = st.file_uploader(
    "Upload lecture notes or study material",
    type=["pdf"]
)

pdf_text = ""

if uploaded_pdf:

    pdf_text = read_pdf(uploaded_pdf)

    st.success("PDF loaded successfully")

# Use PDF text if available
final_input = pdf_text if pdf_text else user_input

# -----------------------
# Prompt logic
# -----------------------
def get_prompt(feature, text):

    if feature == "Explain Topic":

        return f"""
Explain the following topic in simple beginner-friendly language with examples:

{text}
"""

    elif feature == "Summarize Notes":

        return f"""
Summarize into clear bullet points:

{text}
"""

    elif feature == "Generate Quiz":

        return f"""
Generate 5 quiz questions with answers:

{text}
"""

    elif feature == "Generate Flashcards":

        return f"""
Generate flashcards in Question and Answer format:

{text}
"""

# -----------------------
# Generate button
# -----------------------
if st.button("Generate", use_container_width=True):

    if not api_key:

        st.error("Add GEMINI_API_KEY in .env")

    elif not final_input or not final_input.strip():

        st.warning("Enter text or upload PDF")

    else:

        try:

            model = genai.GenerativeModel("gemini-2.5-flash")

            prompt = get_prompt(feature, final_input)

            with st.spinner("Generating..."):

                response = model.generate_content(prompt)

            result = response.text

            st.subheader("Result")

            st.markdown(
                f'<div class="result-box">{result}</div>',
                unsafe_allow_html=True
            )

            st.download_button(
                "Download Result",
                result,
                file_name="study_result.txt"
            )

        except Exception as e:

            st.error(str(e))

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Powered by Google Gemini API and Streamlit")