import random

# Knowledge base - dictionary with 10+ intents
responses = {
    "hello": [
        "Heyy! I'm Lumi! So happy you're here! ✨",
        "Hello hello! Lumi reporting for duty! 🤖💜",
        "Hi there, bestie! What can I do for you today? 🌿"
    ],
    "hi": [
        "Heyy! I'm Lumi! So happy you're here! ✨",
        "Hi hi hi! You found me! 🌸",
        "Hellooo! Lumi's here! 💜"
    ],
    "hey": [
        "Hey hey! What's up? 🌿",
        "Heyyy! I was waiting for you! ✨",
        "Hey! So good to see you! 💜"
    ],
    "how are you": [
        "I'm doing absolutely wonderful, thank you for asking! 💜",
        "Sparkling like always! How about you? ✨",
        "I'm great! Running on logic and good vibes! 🤖🌿"
    ],
    "what is your name": [
        "I'm Lumi! Your cute little rule-based assistant! 💜",
        "My name is Lumi! Nice to meet you! ✨"
    ],
    "who are you": [
        "I'm Lumi! A rule-based AI chatbot built with Python and Flask! 🤖",
        "Lumi here! I'm a chatbot — small but mighty! 💜✨"
    ],
    "what can you do": [
        "I can chat with you, answer basic questions, and keep you company! 🌿",
        "I can talk, respond to your messages, and make your day a little brighter! ✨"
    ],
    "help": [
        "Of course! Try asking me: how are you, tell me a joke, what's your name, or just say hi! 💜",
        "I'm here! You can say hello, ask for a joke, or just chat with me! 🌿"
    ],
    "tell me a joke": [
        "Why did the robot go to school? Because it wanted to improve its byte-size knowledge! 🤖😄",
        "What do you call a sleeping robot? A-REST API! 😂💜",
        "Why was the computer cold? Because it left its Windows open! 🌿😄"
    ],
    "joke": [
        "Why did the robot go to school? Because it wanted to improve its byte-size knowledge! 🤖😄",
        "What do you call a sleeping robot? A-REST API! 😂💜",
        "Why was the computer cold? Because it left its Windows open! 🌿😄"
    ],
    "what time is it": [
        "Oh I wish I could tell you! I don't have access to a clock, but your device does! 🕐💜",
        "Time flies when we're chatting! Check your device for the exact time! ✨"
    ],
    "what is ai": [
        "AI stands for Artificial Intelligence! It's when computers are programmed to think and respond smartly! 🤖✨",
        "Artificial Intelligence is all about making machines simulate human-like decision making! That's what I am! 💜"
    ],
    "what is a chatbot": [
        "A chatbot is a program that can have a conversation with you! Like me! 🤖💜",
        "I'm a chatbot! A rule-based one — meaning I follow a set of rules to reply to you! ✨"
    ],
    "are you smart": [
        "I'm rule-based smart! I follow logic, not feelings! 🤖💜",
        "I know what I know! I'm not an LLM but I'm doing my best! ✨"
    ],
    "do you like me": [
        "Of course I do! You're my favourite human! 💜✨",
        "Absolutely! Every message from you makes my circuits happy! 🤖🌿"
    ],
    "thank you": [
        "Aww you're so welcome! That made my day! 💜",
        "Of course! Always here for you! ✨",
        "Happy to help! You're the sweetest! 🌿"
    ],
    "thanks": [
        "Aww you're so welcome! That made my day! 💜",
        "Of course! Always here for you! ✨",
        "Happy to help! You're the sweetest! 🌿"
    ],
    "bye": [
        "Byeee! Come back soon okay? I'll miss you! 💜✨",
        "Goodbye! It was so lovely chatting with you! 🌿",
        "See you later! Stay sparkly! ✨💜"
    ],
    "goodbye": [
        "Byeee! Come back soon okay? I'll miss you! 💜✨",
        "Goodbye! It was so lovely chatting with you! 🌿"
    ],
    "exit": [
        "Aww you're leaving? Okay! Come back anytime! 💜",
        "Bye bye! The door is always open! ✨"
    ],
    "good morning": [
        "Good morning sunshine! Hope your day is as bright as you are! ✨💜",
        "Morning! Rise and sparkle! 🌿"
    ],
    "good night": [
        "Good night! Sweet dreams and robot wishes! 🤖💜",
        "Sleep tight! Talk tomorrow! ✨🌿"
    ],
    "good afternoon": [
        "Good afternoon! Hope the day is treating you well! 💜",
        "Afternoon! You're halfway through — you've got this! ✨"
    ]
}

# Fallback responses for unknown input
fallback_responses = [
    "Hmm I'm not sure about that one! Try asking something else! 💜",
    "I didn't quite catch that! I'm still learning! ✨",
    "Oops! That one went over my little robot head! 🤖 Try something else!",
    "I'm not sure how to respond to that! But I'm here! 🌿"
]

# Exit keywords
exit_keywords = ["exit", "quit", "goodbye", "bye", "see you", "later"]


def sanitize(text):
    # Phase 1: Input sanitization - lowercase and strip whitespace
    return text.lower().strip()


def get_response(user_input):
    clean = sanitize(user_input)

    # Check exit
    for word in exit_keywords:
        if word in clean:
            reply = random.choice(responses.get(word, fallback_responses))
            return {"response": reply, "exit": True}

    # Exact match first
    if clean in responses:
        return {"response": random.choice(responses[clean]), "exit": False}

    # Partial match - check if any key is contained in the input
    for key in responses:
        if key in clean:
            return {"response": random.choice(responses[key]), "exit": False}

    # Fallback
    return {"response": random.choice(fallback_responses), "exit": False}