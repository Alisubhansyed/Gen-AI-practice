from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()



async def main():
    client=MultiServerMCPClient({
        "math":{
            "command":"python", 
            "args":["mathserver.py"], 
            "transport":"stdio"

        }, 
        "weargerserver":{
            "url":"http://127.0.0.1:8000/mcp", 
            "transport":"streamable-http"

        }
    })
    os.environ["OPENAI_API_KEY"]=os.getenv('OPENAI_API_KEY')
    os.environ["GEMINI_API_KEY"]=os.getenv('GEMINI_API_KEY')
    os.environ["GROQ_API_KEY"]=os.getenv('GROQ_API')
    try:
      tools = await client.get_tools()
    except Exception as e:
       print(f"Failed initialization: {e}")
    model=ChatOpenAI(model="gpt-4.1")
    # model_with_tool = model.bind_tools(tools=tools)
           
    agent = create_agent(model, tools)
    response = await agent.ainvoke({
         "messages": [{"role": "user", "content": "what is weather in lahore? and what is 2+5*3? "}]
     })
    # response = await agent.ainvoke({
    #      "messages": [{"role": "user", "content": "hi what is 2+4?"}]
    #  })

    print(response["messages"][-1].content)

asyncio.run(main())    

