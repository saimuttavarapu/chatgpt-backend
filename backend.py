from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

# Set your OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "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")  # Replace "12345" later

app = FastAPI()

# CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask(q: Question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": q.question}
            ]
        )
        return {"answer": response.choices[0].message.content}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
