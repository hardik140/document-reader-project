# Contract Summarizer (AI Key Points)

This is a simple web application that summarizes key points from contract documents (PDF or TXT) using AI. It leverages the Hugging Face Transformers library and Streamlit for the user interface.

## Features
- Upload contract files in PDF or TXT format
- Extracts and summarizes key points using a pre-trained AI model (facebook/bart-large-cnn)
- View the summarized key points and optionally the full contract text

## Installation
1. Clone this repository or download the source code.
2. Install dependencies using pipenv or pip:
   
   ```bash
   pip install streamlit PyPDF2 transformers
   ```

## Usage
1. Run the Streamlit app:
   
   ```bash
   streamlit run contract_summarizer.py
   ```
2. Open the provided local URL in your browser.
3. Upload a contract file (PDF or TXT) and view the AI-generated summary.

## Notes
- The summarization model requires an internet connection to download the first time.
- Large contracts are split into smaller chunks for summarization.

## License
This project is for educational/demo purposes only. 