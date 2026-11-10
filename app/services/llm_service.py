import os

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


async def generate_response(message: str) -> str:
    try:
        llm_response = await client.responses.create(
            model=os.getenv("OPENAI_MODEL"),
            instructions="You are a helpful AI assistant.",
            input=message
        )
        return llm_response.output_text
    except Exception as e:
        print(e)
        return "Sorry, I encountered an error while processing your request."
