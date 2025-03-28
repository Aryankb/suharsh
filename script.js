function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    if (userInput.trim() === "") return;

    let chatbox = document.getElementById("chatbox");

    // Display user message
    let userMessage = `<div style="text-align:right; margin:5px;">
                        <b>You:</b> ${userInput}
                      </div>`;
    chatbox.innerHTML += userMessage;

    // Send request to API
    fetch("https://suharsh.onrender.com/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
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
