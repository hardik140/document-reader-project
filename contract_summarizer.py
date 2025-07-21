import streamlit as st
import PyPDF2

def extract_text(file):
    if file.name.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')
    else:
        return ""

@st.cache_resource

def load_summarizer():
    from transformers.pipelines import pipeline
    return pipeline("summarization", model="facebook/bart-large-cnn")

st.title("\U0001F4DA Contract Summarizer (AI Key Points)")

uploaded_file = st.file_uploader("Upload a contract (PDF or TXT)", type=["pdf", "txt"])
if uploaded_file:
    text = extract_text(uploaded_file)
    if text:
        st.subheader("Key Points Summary (AI)")
        summarizer = load_summarizer()
        if summarizer is None:
            st.error("Failed to load summarizer model.")
            st.stop()
        import textwrap
        max_chunk = 1024
        chunks = textwrap.wrap(text, max_chunk)
        summary = ""
        for chunk in chunks:
            result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            # Ensure result is a list and contains dicts with 'summary_text'
            if isinstance(result, list) and result and isinstance(result[0], dict) and 'summary_text' in result[0]:
                summary_piece = result[0]['summary_text']
                if isinstance(summary_piece, str):
                    summary += summary_piece + "\n"
        st.write(summary)
        st.subheader("Full Text (optional)")
        with st.expander("Show full contract text"):
            st.write(text)
    else:
        st.error("Could not extract text from the file.") 