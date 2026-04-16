from openai import OpenAI
from llm_module.config import API_KEY
from llm_module.rag_engine import load_rules

client = OpenAI(api_key=API_KEY)

def chatbot_response(question, data):
    rules = load_rules()

    prompt = f"""
    You are an AI assistant for infrastructure inspection.

    Rules:
    {rules}

    Crack Details:
    Length: {data['crack_length']}
    Width: {data['crack_width']}
    Location: {data['location']}

    User Question:
    {question}

    Answer clearly.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content