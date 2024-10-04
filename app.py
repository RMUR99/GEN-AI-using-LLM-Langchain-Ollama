import os 
from dotenv import load_dotenv 
from langchain_community.llms import Ollama
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

# Load environment variables from .env file
load_dotenv()  # Ensure this is properly imported

# in the previous notebook we used to add the OpenAI keys but we won't be doing that here; we will just add the Langchain keys
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Let's make prompt Template, here we will set the prompt and we can determine how our model's personality be, 
## and we are preparing it that the question will come from the user 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer questions and make sure to summarize."),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework 
st.title("Langchain Demo with Llama3 Model")
input_text = st.text_input("What is your question?")  # Changed to text_input for user interaction

## Setting up the model 
# This pipeline processes an input prompt using the "llama3" language model, generating a response.
# The response is then parsed by the output parser for further interpretation or formatting.c
llm = Ollama(model='llama3.2')
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
