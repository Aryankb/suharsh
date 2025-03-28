document.getElementById("userInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") return;

    let chatbox = document.getElementById("chatbox");

    // Display user message
    let userMessage = `<div style="text-align:right; margin:5px;">
                        <b>You:</b> ${userInput}
                      </div>`;
    chatbox.innerHTML += userMessage;

    // Show "Thinking..." before response
    let thinkingMessage = `<div id="thinking" style="text-align:left; margin:5px; color: gray;">
                            AI is thinking...
                          </div>`;
    chatbox.innerHTML += thinkingMessage;

    // Send request to API
    fetch("https://suharsh.onrender.com/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("thinking").remove(); // Remove thinking message
        
        // Display AI response
        let botMessage = `<div style="text-align:left; margin:5px;">
                            <b>AI:</b> ${data.answer}
                          </div>`;
        chatbox.innerHTML += botMessage;
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    // Clear input field
    document.getElementById("userInput").value = "";
}
