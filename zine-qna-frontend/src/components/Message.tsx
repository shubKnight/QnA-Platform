import React from "react";

type MessageProps = {
  text: string;
  sender: "user" | "bot";
};

const Message: React.FC<MessageProps> = ({ text, sender }) => {
  return (
    <div
      className={`p-3 my-2 rounded-lg max-w-xs ${
        sender === "user"
          ? "bg-blue-500 text-white self-end"
          : "bg-gray-200 text-black self-start"
      }`}
    >
      {text}
    </div>
  );
};

export default Message;
