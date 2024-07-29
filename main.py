import streamlit as st
from transformers import pipeline
import time

# Available summarization models
model_options = {
    "BART (facebook/bart-large-cnn)": "facebook/bart-large-cnn",
    "T5 (t5-small)": "t5-small",
    "Pegasus (google/pegasus-xsum)": "google/pegasus-xsum"
}

# Cache the summarizer to avoid reloading it every time
@st.cache_data
def get_summarizer(model_name):
    start_time = time.time()
    summarizer = pipeline('summarization', model=model_name)
    load_time = time.time() - start_time
    st.write(f"Model load time: {load_time:.2f} seconds")
    return summarizer

# Streamlit app title and description
st.title('📝 Text Summarizer')
st.markdown("""
    **Welcome to the Text Summarizer app!**  
    Enter your text or upload a file to generate a concise summary. Choose from popular summarization models and adjust the summary length settings as needed.
""")

# Sidebar for model selection
st.sidebar.header('Model Selection')
selected_model = st.sidebar.selectbox("Select a summarization model:", list(model_options.keys()))

# Initialize the summarizer
model_name = model_options[selected_model]
summarizer = get_summarizer(model_name)

# Text input area
st.header('Text Input')
text = st.text_area("Enter the text to summarize:", height=200)

# File upload option
st.sidebar.header('Upload Text File')
uploaded_file = st.sidebar.file_uploader("Upload a text file:", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.info("Text File Uploaded")

if text:
    word_count = len(text.split())
    max_length = max(50, word_count // 2)  # Set max_length to half of the total words, minimum 50
    min_length_max = word_count  # min_length can go up to the number of words

    # Display word count and recommended max_length
    st.write(f"**Word count:** {word_count}")
    st.write(f"**Recommended max length for summary:** {max_length}")

    # Summary settings
    st.subheader('Summary Settings')
    min_length = st.slider("Select minimum summary length:", min_value=10, max_value=min_length_max, value=20)
    min_length = min(min_length, max_length)  # Ensure min_length is not greater than max_length
    st.write(f"**Maximum length for summary:** {max_length}")

    # Summarize button
    if st.button('Summarize'):
        with st.spinner('Generating summary...'):
            summarized_text = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']

            # Display original and summarized text side-by-side
            st.subheader("Results")
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Text")
                st.write(text)
            with col2:
                st.subheader("Summarized Text")
                st.write(summarized_text)

            # Download summarized text
            st.download_button("Download Summary", summarized_text, file_name="summary.txt")
else:
    st.info('Please enter some text to summarize or upload a text file.')
