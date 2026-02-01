import streamlit as st
import time

st.set_page_config(page_title="Circuit Whisperer")

st.title("🔌 Circuit Whisperer")
st.write("AI-powered assistant for understanding electronic circuits and lab experiments.")

st.file_uploader("Upload circuit image (demo)", type=["png", "jpg", "jpeg"])

circuit = st.text_area(
    "Describe your circuit (components + goal):",
    height=120
)

if st.button("Analyze Circuit"):
    with st.spinner("Analyzing circuit..."):
        time.sleep(1.5)  # Demo-friendly delay

    st.success("Analysis complete ✅")

    st.subheader("📘 Circuit Explanation")
    st.write("""
    • This circuit performs the intended operation based on the given components.  
    • Each component contributes to controlling current and voltage levels.  
    • Common mistakes include wrong polarity and loose connections.  
    • Follow step-by-step lab procedure to ensure safety and accuracy.
    """)

    st.info("💡 Full AI-powered image analysis available in Google AI Studio version.")
