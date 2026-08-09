# -------------------- Import Required Libraries -------------------- #

# FastAPI is used to build APIs and WebSocket applications
from fastapi import FastAPI, WebSocket

# HTMLResponse allows returning custom HTML content directly from FastAPI
from fastapi.responses import HTMLResponse


# -------------------- Create FastAPI Application -------------------- #

# Initialize FastAPI application instance
app = FastAPI(
    title="FastAPI WebSocket Demo",
    description="Simple real-time WebSocket communication example using FastAPI",
    version="1.0.0"
)


# -------------------- Frontend HTML for WebSocket Testing -------------------- #

# Simple HTML interface to test WebSocket communication
# This frontend connects to the FastAPI WebSocket server
html = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Chat</title>
</head>
<body>

    <h1>FastAPI WebSocket Chat</h1>

    <!-- Input field for sending messages -->
    <input type="text" id="messageText" placeholder="Type message">

    <!-- Button to send message -->
    <button onclick="sendMessage()">Send</button>

    <!-- List to display received messages -->
    <ul id="messages"></ul>

    <script>

        // Create WebSocket connection with FastAPI backend
        const ws = new WebSocket("ws://127.0.0.1:8000/ws");


        // Handle incoming messages from the server
        ws.onmessage = function(event) {

            // Select messages container
            const messages = document.getElementById('messages');

            // Create new list item
            const message = document.createElement('li');

            // Add received message text
            message.textContent = event.data;

            // Append message to UI
            messages.appendChild(message);
        };


        // Function to send messages to the WebSocket server
        function sendMessage() {

            // Get input element
            const input = document.getElementById("messageText");

            // Send message to server
            ws.send(input.value);

            // Clear input field after sending
            input.value = "";
        }

    </script>

</body>
</html>
"""


# -------------------- HTTP Route -------------------- #

# Route to serve HTML page in browser
@app.get("/")
async def home():
    return HTMLResponse(html)


# -------------------- WebSocket Route -------------------- #

# WebSocket endpoint for real-time communication
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    # Accept incoming WebSocket connection
    await websocket.accept()

    # Keep connection active continuously
    while True:

        # Receive text data from client
        data = await websocket.receive_text()

        # Send response back to client
        await websocket.send_text(f"Server received: {data}")