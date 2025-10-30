"use client";
import { useState } from "react";
import './globals.css';

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    setLoading(true);
    const res = await fetch("http://localhost:8000/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await res.json();
    setResponse(data.reply);
    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Chat with Llama 3.2</h2>
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        rows={4}
        cols={50}
      />
      <br />
      <button onClick={sendMessage} disabled={loading}>
        {loading ? "Thinking..." : "Send"}
      </button>
      <p><strong>AI:</strong> {response}</p>
    </div>
  );
}
