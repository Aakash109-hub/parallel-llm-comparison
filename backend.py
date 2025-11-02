from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from typing import TypedDict
import os

load_dotenv()  # Loads variables from .env file

# Optional check
print("GROQ Key Loaded:", os.getenv("GROQ_API_KEY") is not None)

# Initialize model
llm1 = ChatGroq(
    model="compound-beta",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

llm2 = ChatOllama(model = "qwen3:1.7b")

class LLMState(TypedDict):
    query: str
    response1: str
    response2: str


def call_to_llm1(state: LLMState):
    query = state["query"]  # <-- Extract topic from the state dictionary
    prompt = f"""
    You are a helpful assistant, provide answer for the query \n {query} \n \n
    If you don't know the answer just say i don't know.
    """
    output1 = llm1.invoke(prompt)
    return {'response1': output1.content}

def call_to_llm2(state: LLMState):
    query = state["query"]  # <-- Extract topic from the state dictionary
    prompt = f"""
    You are a helpful assistant, provide answer for the query \n {query} \n \n
    If you don't know the answer just say i don't know.
    """
    output2 = llm2.invoke(prompt)
    return {'response2': output2.content}


graph = StateGraph(LLMState)

graph.add_node("call_to_llm1", call_to_llm1)
graph.add_node("call_to_llm2", call_to_llm2)

graph.add_edge(START, "call_to_llm1")
graph.add_edge(START, "call_to_llm2")

graph.add_edge("call_to_llm1", END)
graph.add_edge("call_to_llm2", END)

chatbot_flow = graph.compile()

