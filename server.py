from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import ollama

app = FastAPI()

# Allow requests from your React app (e.g., localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify http://localhost:3000 for tighter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': user_input}
    ])
    
    return {"reply": response['message']['content']}
