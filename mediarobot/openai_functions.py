import openai
import streamlit as st

@st.spinner(text="Thinking...")
def ask(message: str, prompt: str, model: str) -> str:
    """Answers a query using GPT and a prompt."""

    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.7,
        messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": message},
    ]
    )
    response_message = response["choices"][0]["message"]["content"]
    return response_message
