import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

st.set_page_config(page_title="Circuit Whisperer")

st.title("🔌 Circuit Whisperer")
st.write("Upload a circuit diagram to get explanation and lab guidance.")

uploaded_file = st.file_uploader(
    "Upload Circuit Image",
    type=["png", "jpg", "jpeg"]
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    model = genai.GenerativeModel("models/gemini-1.5-flash")

    prompt = """
    You are an expert electronics lab assistant.
    Explain this circuit:
    1. What the circuit does
    2. Function of each component
    3. Common lab mistakes
    4. Step-by-step experimental procedure
    """

    with st.spinner("Analyzing circuit..."):
        response = model.generate_content([prompt, image])

    st.subheader("📘 Explanation")
    st.write(response.text)
