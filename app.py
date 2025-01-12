from flask import Flask, request, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Load the DialoGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.get_json().get("message", "")

    # Tokenize the user input
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Generate response
    response_ids = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
    bot_reply = tokenizer.decode(response_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    return {"reply": bot_reply}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

