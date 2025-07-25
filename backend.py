from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
# Set your OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY", "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")  # Replace "12345" later

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your GitHub Pages domain for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(question: Question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question.question}],
        temperature=0.7,
    )
    return {"answer": response.choices[0].message.content}
