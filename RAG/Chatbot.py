import langchain as lc
import openai as ai
import datasets as ds
import tiktoken as tk

import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key is None:
    raise ValueError("No OpenAI API key found. Please set it in the .env file.")

# Initialize the ChatOpenAI with the API key
chat = ChatOpenAI(open_api_key=openai_api_key, model="gpt-3.5-turbo")

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi AI, how are you today?."),
    AIMessage(content="I am great, thank you. How can I help you?"),
    HumanMessage(content="I am looking for a restaurant in the center of Berlin."),
]

