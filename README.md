# Lumi 🤖
### A Simple Rule-Based Chatbot

This is a small project I built while exploring how rule-based chatbots work before moving into more advanced NLP/AI concepts. Lumi responds to greetings, basic questions, and casual conversation using keyword matching — no machine learning involved, just plain logic.

---

## Screenshots
<img width="1595" height="659" alt="image" src="https://github.com/user-attachments/assets/fea546f9-fd53-4406-bd46-08b446614efc" />
<img width="1595" height="669" alt="image" src="https://github.com/user-attachments/assets/d1e724cb-a83e-481e-bf24-7a3bf010325e" />

### Chat Interface
<!-- add your screenshot here -->

### Loading / Farewell Screen
<!-- add your screenshot here -->

---

## What it does

Lumi only responds to a fixed set of predefined keywords and phrases — it doesn't understand free-form or open-ended input. This was intentional: the goal of this project was to practice control flow and rule-based logic, not natural language understanding.

- Responds to greetings and common questions (how are you, what's your name, tell me a joke, etc.)
- Detects exit keywords (bye, exit, quit) and ends the conversation politely
- Uses exact keyword matching first, then falls back to partial matching
- Gives a random fallback reply when it doesn't understand the input
- Runs through a simple web interface built with Flask
  
---

## Tech Stack

- Python, Flask (backend)
- HTML, CSS, JavaScript (frontend)

---

## How it works

1. User types a message in the chat box
2. Flask receives it and cleans the input (lowercase, trimmed)
3. Checks for exit keywords first
4. Looks for an exact match in the response dictionary
5. If no exact match, checks if any known keyword appears inside the message
6. If nothing matches, sends a random fallback response

This project was mainly about practicing control flow, dictionaries, and basic decision-making logic in Python — the building blocks before working with anything ML-based.

---

## Project Structure

chatbot_project/
│
├── app.py                 # Flask routes
├── chatbot.py              # Chatbot logic and response dictionary
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
├── css/style.css
├── js/script.js
└── images/lumi_robot.png

---

## Run it locally

```bash
git clone https://github.com/<your-username>/lumi-chatbot.git
cd lumi-chatbot
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## What I learned

- Structuring a small Flask app with separate concerns (routes vs. chatbot logic)
- Using dictionaries for fast lookups instead of long if-elif chains
- Basic input sanitization before processing
- Handling partial/fuzzy matching with simple keyword checks
- Connecting a Python backend to a JS frontend via fetch/JSON

---

## Author

**Noor Fatima**
BSCS Student — Lahore Garrison University
