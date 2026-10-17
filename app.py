from flask import Flask, request



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ezra AI assistant</title>
    </head>
    <body>
        <h1>Hello, I'm Ezra, your AI assistant</h1>

        <form id="chat-form">
            <input
                type="text"
                id="message"
                placeholder="type your message here"
                required
            >
            <button type="submit">Send</button>
        </form>
        <div id="chat"></div>
        <div id="response"></div>

        <script>
            const form = document.getElementById("chat-form");
            const messageInput = document.getElementById("message");
            const response = document.getElementById("response");

            function addMessage(who, text){
                const line = document.createElement("p");
                line.textContent = who + ":" + text;
                chat.appendChild(line);
            }

            form.addEventListener("submit", function(event) {
                event.preventDefault();

                const message = messageInput.value.trim();
                const lower = message.toLowerCase();
                const chat = document.getElementById("chat");

                addMessage("You", message);
                messageInput.value = "";
                
                if (lower.includes("hello")) {
                    addMessage("Ezra", " Hello! How can I help you?");
                } else if (lower.includes("what is your name")){
                    addMessage("Ezra", " My name is Ezra! I'm your AI assistant.");
                } else if (lower.includes("how are you")){
                    addMessage("Ezra", " I'm doing great! Thanks for asking!");
                } else if (lower.includes("what can you do")){
                    addMessage("Ezra", " I can respond to simple questions for now");
                } else {
                    addMessage("Ezra", " Ezra received message: " + message);

                }

                    messageInput.value = "";
            });
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)