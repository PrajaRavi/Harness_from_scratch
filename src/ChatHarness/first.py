from .Models.Groq import GroqLLM
import os
from dotenv import load_dotenv
load_dotenv()
groq=GroqLLM(params={
  "api_key":os.getenv("GROQ_API_KEY_KADIR"),
  "model":"openai/gpt-oss-20b",
  "temprature":1,
  "max_retries":3
  }
  )
response=groq.invoke({"messages":[{"role":"user","content":'hello'}]})
print(response["content"])