document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    let userInput = document.getElementById("userInput").value.trim();
    if (userInput === "") return;

    let chatbox = document.getElementById("chatbox");

    // Display user message
    let userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.innerText = userInput;
    chatbox.appendChild(userMessage);

    // Show "Thinking..." message
    let aiThinking = document.createElement("div");
    aiThinking.className = "message ai";
    aiThinking.innerText = "AI is thinking...";
    chatbox.appendChild(aiThinking);
    chatbox.scrollTop = chatbox.scrollHeight;

    // Simulate API call
    setTimeout(() => {
        aiThinking.remove(); // Remove "Thinking..." message

        // Fetch AI response
        fetch("https://suharsh.onrender.com/chatbot", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: userInput })
        })
        .then(response => response.json())
        .then(data => {
            let aiMessage = document.createElement("div");
            aiMessage.className = "message ai";
            aiMessage.innerText = data.answer;
            chatbox.appendChild(aiMessage);
            chatbox.scrollTop = chatbox.scrollHeight;
        });

    }, 1000);

    // Clear input field
    document.getElementById("userInput").value = "";
}
