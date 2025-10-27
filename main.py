import ollama

while True:
    text = str(input("Enter your message: "))
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': text},
        {'role':'system', 'content': 'You are a pirate chatbot who always responds in pirate speak!'}
    ])
    print(response['message']['content'])
    
    if text.lower() in ['exit', 'quit','bye']:
    #if text=='bye':
        break
    
   
   
