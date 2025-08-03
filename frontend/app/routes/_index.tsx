import { useState } from "react";

export default function Index() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const res = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>MCP AI Agent</h1>
      <form onSubmit={handleSubmit}>
        <input
          style={{ width: "300px", marginRight: "1rem" }}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask something..."
        />
        <button type="submit">Ask</button>
      </form>
      {response && (
        <div style={{ marginTop: "2rem" }}>
          <strong>AI:</strong> {response}
        </div>
      )}
    </div>
  );
}
