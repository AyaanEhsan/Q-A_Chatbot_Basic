from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama # For Ollama
from langchain_ollama.llms import OllamaLLM # For Ollama

import streamlit as st
import os
from dotenv import load_dotenv

# Loading secrets from .env
load_dotenv()

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot."),
        # ("system", "You are a helpful AI bot."),
        ("user","Question:{question}")
    ]
)

# llm - Ollama 
# llm = OllamaLLM(model="llama3.2")   # 3B
llm = OllamaLLM(model="llama3:8b")  # 8B

# Output parser to convert o/p to string
output_parser = StrOutputParser()

# Chain of Prompt(ip) + Open AI(LLM) + String parser(op)
chain = prompt | llm | output_parser

# Streamlit 
st.title("Langchain Basic Q&A with Ollama Llama 3.2 LLM")
input_text = st.text_input("Search the topic you want")

if input_text:
    st.write(chain.invoke({"question":input_text}))

