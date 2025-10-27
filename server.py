from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import ollama
import re

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': user_input},
        {'role':'system', 'content': 'you are a black american chat-bot who always responds in slang'}
    ])
    
    content = response['message']['content']

    # 🧹 Remove Ollama tokens like <|start_header_id|> and <|end_header_id|>
    clean_content = re.sub(r"<\|.*?\|>", "", content).strip()

    return {"reply": clean_content}
