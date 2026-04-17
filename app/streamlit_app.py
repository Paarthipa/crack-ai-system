import streamlit as st
import random

from llm_module.data_loader import load_data
from llm_module.report_engine import generate_report
from llm_module.reasoning_engine import generate_reasoning
from llm_module.chatbot import chatbot_response

# ======================
# SIDEBAR
# ======================
st.sidebar.title("Project Info")
st.sidebar.write("AI Crack Detection System")
st.sidebar.write("Developed by Paarthipa & Kamlesh")

# ======================
# TITLE
# ======================
st.title("AI Crack Detection System")

# ======================
# IMAGE UPLOAD
# ======================
uploaded_file = st.file_uploader("Upload Crack Image", type=["jpg", "png"])

# ======================
# IF IMAGE UPLOADED → SHOW EVERYTHING
# ======================
if uploaded_file:

    st.image(uploaded_file, caption="Uploaded Image", width=500)
    st.success("Using uploaded image (simulated detection)")

    # Simulated detection
    data = {
        "crack_length": round(random.uniform(1.0, 3.0), 2),
        "crack_width": random.randint(1, 6),
        "location": "Detected from uploaded image"
    }

    # ======================
    # SHOW DATA
    # ======================
    st.subheader("Crack Details")
    st.write(f"Length: {data['crack_length']} m")
    st.write(f"Width: {data['crack_width']} mm")
    st.write(f"Location: {data['location']}")

    # ======================
    # REPORT
    # ======================
    if st.button("Generate Report"):
        st.subheader("Report Output")
        st.success(generate_report(data))

    # ======================
    # REASONING
    # ======================
    if st.button("Explain Crack"):
        st.subheader("Reasoning Output")
        st.info(generate_reasoning(data))

    # ======================
    # CHATBOT
    # ======================
    st.subheader("Ask Questions")

    question = st.text_input("Ask about the crack:")

    if question:
        with st.spinner("Thinking..."):
            response = chatbot_response(question, data)
        st.info(response)

# ======================
# IF NO IMAGE
# ======================
else:
    st.info("Upload an image to begin AI-based crack analysis.")