import streamlit as st
from llm_module.data_loader import load_data
from llm_module.report_engine import generate_report
from llm_module.reasoning_engine import generate_reasoning

st.title("AI Crack Detection System")

data = load_data()[0]

if st.button("Generate Report"):
    st.write(generate_report(data))

if st.button("Explain Crack"):
    st.write(generate_reasoning(data))