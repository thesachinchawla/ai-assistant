import os

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


async def generate_response(message: str) -> str:
    response = await client.response.create(
        model=os.getenv("OPENAI_MODEL"),
        instructions="You are a helpful AI assistant.",
        input=message
    )
    return response.output_text
