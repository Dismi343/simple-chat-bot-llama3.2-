# Simple Chat bot 
This chatbot runs in local machine using Llama3.2 model
## created using 
python (backend), Ollama, React(next.js)(Frontend),

## Run backend
```bash
python -m uvicorn server:app --reload
```

## Run frontend
```bash
cd simple-chatbot
npm install
npm run dev
```

## prerequisites
Download ollama, 
  In cmd
```bash
  ollama run llama3.2:1b
```
  then type 
  ```bash
  ollama list
```
  and check whether llama3.2:1b installed correctly
