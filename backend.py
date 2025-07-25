# backend.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from openai import OpenAI

# Set your API key here (will be replaced in Render env var)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "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"))

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(question: Question):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question.question}],
            temperature=0.7,
        )
        return {"answer": chat_completion.choices[0].message.content}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}
