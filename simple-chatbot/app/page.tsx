"use client";
import { useState } from "react";
import './globals.css';

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    setLoading(true);
   try {
     const res = await fetch("http://localhost:8000/api/chat", {
       method: "POST",
       headers: { "Content-Type": "application/json" },
       body: JSON.stringify({ message }),
     });
     const data = await res.json();
     setResponse(data.reply);
     setLoading(false);
   } catch (error) {
    console.log(error);  
    setLoading(false);
   }
    
  };

  return (
    <div style={{ padding: 20 }} className="flex flex-col w-full justify-center items-center">
      <h2 className="font-bold text-3xl my-20">Chat with Llama 3.2</h2>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        rows={4}
        cols={50}
        className="shadow-lg border rounded-xl"
      />
      <br />
      <button onClick={sendMessage} disabled={loading} className="bg-neutral-500 px-8 py-2 rounded-lg shadow-lg my-8 text-white hover:bg-neutral-400">
        {loading ? "Thinking..." : "Send"}
      </button>
      <p><strong>AI:</strong> {response}</p>
    </div>
  );
}
