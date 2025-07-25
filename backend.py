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
