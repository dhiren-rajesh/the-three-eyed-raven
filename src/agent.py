from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from api import fetch_f1_api

@tool
def ergast_f1_agent(endpoint: str) -> dict:
    """
    Fetch F1 data via the Ergast API
    """
    return fetch_f1_api(endpoint)

def build_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    llm_with_tools = llm.bind_tools([ergast_f1_agent])

    f1_prompt = ChatPromptTemplate.from_messages([
        ("system", 
        "You are a Formula 1 expert. "
        "You MUST use the ergast_f1_api tool for factual data."),
        ("human", "{input}")
    ])

    f1_agent = (
        {"input": RunnablePassthrough()}
        | f1_prompt
        | llm_with_tools
    )

    return f1_agent, llm_with_tools