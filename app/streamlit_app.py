import streamlit as st
from llm_module.data_loader import load_data
from llm_module.report_engine import generate_report
from llm_module.reasoning_engine import generate_reasoning
from llm_module.chatbot import chatbot_response   # 👈 ADD THIS

st.title("AI Crack Detection System")

data = load_data()[0]

# Report
if st.button("Generate Report"):
    st.write(generate_report(data))

# Reasoning
if st.button("Explain Crack"):
    st.write(generate_reasoning(data))

# 👇 CHATBOT SECTION
st.subheader("Ask Questions")

question = st.text_input("Ask about the crack:")

if question:
    response = chatbot_response(question, data)
    st.write(response)