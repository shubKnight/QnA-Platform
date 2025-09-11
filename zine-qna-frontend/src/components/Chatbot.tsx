import React, { useState } from "react";
import axios from "axios";
import Message from "./Message";

type ChatMessage = {
  text: string;
  sender: "user" | "bot";
};

const ChatBox: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: ChatMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);

    try {
      // replace with your backend API
      const res = await axios.post("http://localhost:5000/api/chat", {
        query: input,
      });

      const botMessage: ChatMessage = {
        text: res.data.answer || "No response",
        sender: "bot",
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { text: "Error connecting to server", sender: "bot" },
      ]);
    }

    setInput("");
  };

  return (
    <div className="flex flex-col h-screen p-4 bg-gray-100">
      <div className="flex-1 overflow-y-auto flex flex-col">
        {messages.map((msg, idx) => (
          <Message key={idx} text={msg.text} sender={msg.sender} />
        ))}
      </div>

      <div className="flex gap-2 mt-2">
        <input
          type="text"
          className="flex-1 p-2 border rounded-lg"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Ask a question..."
        />
        <button
          className="px-4 py-2 bg-blue-600 text-white rounded-lg"
          onClick={sendMessage}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBox;
