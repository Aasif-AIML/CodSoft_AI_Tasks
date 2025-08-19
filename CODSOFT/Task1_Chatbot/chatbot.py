# chatbot.py

import re
import wikipedia # pyright: ignore[reportMissingImports]
from datetime import datetime

# Predefined rules (pattern -> response)
rules = {
    r"(hi|hello|hey)": "Hello! How can I assist you?",
    r"how are you": "I'm doing well! How about you?",
    r"(who are you|your name)": "I am CodSoft Chatbot, your virtual assistant.",
    r"(bye|exit|quit)": "Goodbye! Have a nice day!"
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Handle Date and Time queries
    if "time" in user_input:
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    
    elif "date" in user_input or "today" in user_input:
        today = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}."

    # Rule-based matching
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    
    # Wikipedia integration (for general knowledge queries)
    try:
        summary = wikipedia.summary(user_input, sentences=2)
        return f"Here's what I found on Wikipedia:\n{summary}"
    except:
        return "Sorry, I don't understand that yet."

# Run chatbot
if __name__ == "__main__":
    print("🤖 Chatbot is ready! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if "bye" in user_input or "exit" in user_input or "quit" in user_input:
            break
