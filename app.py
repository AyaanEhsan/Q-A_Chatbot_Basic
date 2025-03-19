from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Loading secrets from .env
load_dotenv()

# Environment varibles in os.environ dictionary
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful AI bot. Your name is {name}."),
        # ("system", "You are a helpful AI bot."),
        ("user","Question:{question}")
    ]
)

# llm
llm = ChatOpenAI(model = "gpt-3.5-turbo")

# Output parser to convert o/p to string
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Streamlit 
st.title("Langchain Basic Q&A")
input_text = st.text_input("Search the topic you want")

if input_text:
    st.write(chain.invoke({"question":input_text, "name":"Bottim"}))

