const API_URL = "http://127.0.0.1:8000/api/v1";

let conversationId = localStorage.getItem("golf_conversation_id");

const chat = document.getElementById("chat");
const form = document.getElementById("chat-form");
const input = document.getElementById("message");

function addMessage(text, role) {
  const d = document.createElement("div");
  d.className = "msg " + role;
  d.textContent = text;
  chat.appendChild(d);
}

form.addEventListener("submit", async function(event) {
  event.preventDefault();

  const message = input.value.trim();

  if (message === "") {
    return;
  }

  addMessage(message, "user");
  input.value = "";

  try {
    const response = await fetch(API_URL + "/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        conversation_id: conversationId,
        message: message,
        language: "es"
      })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "No se pudo procesar la pregunta");
    }

    conversationId = data.conversation_id;

    localStorage.setItem(
      "golf_conversation_id",
      conversationId
    );

    addMessage(data.answer, "bot");

  } catch (error) {
    addMessage(
      "Error al conectar con el chatbot: " + error.message,
      "bot"
    );
  }
});
