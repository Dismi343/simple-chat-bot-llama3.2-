# Simple Chat bot 
runs in local machine using Llama3.2 model
## create using 
python (backend), Ollama, React(next.js)(Frontend),

##Run backend
python -m uvicorn server:app --reload

##Run frontend
cd my-chatbot-model
npm install
npm run dev

##prerequisites
Download ollama, 
  In cmd- ollama run llama3.2:1b
  type ollama list and check whether llama3.2:1b installed correctly
