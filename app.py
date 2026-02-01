import streamlit as st

st.set_page_config(page_title="Circuit Whisperer")

st.title("🔌 Circuit Whisperer")

st.success("App deployed successfully 🎉")

st.write("""
This is Circuit Whisperer — an AI-powered assistant
that explains electronic circuits and guides lab experiments.

⚡ Image + Gemini analysis was tested in Google AI Studio.
⚡ Deployment uses Streamlit Cloud.
""")

circuit = st.text_area("Describe your circuit:")

if st.button("Analyze"):
    st.write("🔍 Analyzing circuit...")
    st.write("✔️ Explanation will appear here.")

