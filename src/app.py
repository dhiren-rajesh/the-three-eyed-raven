from langchain_core.messages import ToolMessage
from agent import build_agent, ergast_f1_agent

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

f1_agent, llm_with_tools = build_agent()

def run_agent(query: str):
    response = f1_agent.invoke(query)

    if response.tool_calls:
        tool_messages = []

        for call in response.tool_calls:
            result=ergast_f1_agent.invoke(call["args"])
            tool_messages.append(
                ToolMessage(
                    tool_call_id=call["id"],
                    content=result
                )
            )

        final_response = llm_with_tools.invoke(
            [response] + tool_messages
        )
        return final_response.content

    return response.content


if __name__ == "__main__":
    print(run_agent("Who won the 2008 Japan Grand Prix?"))