# DialoGPT Flask Chatbot

A simple AI chatbot built with **DialoGPT**, **Python**, and **Flask**. This chatbot uses Microsoft's DialoGPT model to generate human-like conversational responses, making it ideal for experimenting with conversational AI.

---

## Features
- Generates human-like responses using DialoGPT.
- Simple Flask-based backend for serving the chatbot.
- Lightweight web-based frontend for user interaction.
- Easy to deploy on any server.

---

## Prerequisites
Before getting started, ensure you have the following installed:
- Python 3.7 or later
- pip (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dialogpt-flask-chatbot.git
   cd dialogpt-flask-chatbot
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv chatbot_env
   source chatbot_env/bin/activate
   ```

3. Install the required Python libraries:
   ```bash
   pip install flask transformers
   ```

---

## Usage

1. Start the Flask app:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://<your-server-ip>:5000
   ```

3. Interact with the chatbot through the web-based interface.

---

## How It Works
- The backend uses the DialoGPT model from Hugging Face's `transformers` library to generate conversational responses.
- Flask serves as the web framework to process user input and return the chatbot's response.
- A simple HTML-based frontend allows users to chat with the AI.

---

## Example Interaction

- **User**: Hello, who are you?  
- **Bot**: Hi! I'm an AI chatbot created with DialoGPT. How can I assist you today?  

---

## Deployment
To deploy the chatbot on a production server:
1. Use a production WSGI server like `gunicorn`:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. Optionally, set up a reverse proxy with Nginx for better performance and security.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests.

---

## Acknowledgments
- Powered by [DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium) by Microsoft.
- Built using [Flask](https://flask.palletsprojects.com/) and [Hugging Face Transformers](https://huggingface.co/transformers/).
