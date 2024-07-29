# Text Summarizer

## Overview

**Text Summarizer** is a web application built with Streamlit and Hugging Face Transformers that allows users to input or upload text and generate concise summaries. The app supports multiple summarization models and provides options to adjust the length of the summary.

## Features

- **Model Selection:** Choose from popular summarization models including BART, T5, and Pegasus.
- **Text Input:** Enter text directly or upload a text file for summarization.
- **Adjustable Summary Length:** Customize the summary length with minimum and maximum length settings.
- **Download Summary:** Download the generated summary as a text file.

## Installation

To run this app locally, follow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   
## Usage

1. Run the Streamlit app:

   ```sh
    streamlit run app.py
2. Open your web browser and navigate to http://localhost:8501.

3. Use the sidebar to select a summarization model and adjust summary settings. Enter text directly or upload a text file, then click on the "Summarize" button to generate the summary.

4. View and download the summary from the results section.

## Requirements

* Python 3.x
* Streamlit
* Transformers
* Torch
  
To ensure all dependencies are installed, check the requirements.txt file.

## Example
Here's how you can use the app:

1. Select the summarization model from the sidebar.
2. Enter your text or upload a .txt file.
3. Adjust the summary length using the provided sliders.
4. Click "Summarize" to generate and view the summary.
5. Optionally, download the summary as a .txt file.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Ensure that your contributions adhere to the coding style and add tests where appropriate.

## Contact
For any questions or feedback, please contact saidulchoudhury@gmail.com.



