"""
CodeAlpha - Python Programming Internship
Task 3: Basic Chatbot
"""

import random

RESPONSES = {
    "hello": ["Hi!", "Hello there!", "Hey!"],
    "hi": ["Hi!", "Hello there!", "Hey!"],
    "how are you": ["I'm fine, thanks!", "Doing great, how about you?"],
    "what is your name": ["I'm a simple chatbot made in Python.", "You can call me PyBot."],
    "help": ["I can chat about basic things. Try saying hello, asking how I am, or say bye to exit."],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care."],
}

EXIT_KEYWORDS = ["bye", "exit", "quit"]


def get_response(user_input):
    text = user_input.lower().strip()

    for key, replies in RESPONSES.items():
        if key in text:
            return random.choice(replies)

    return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def is_exit(user_input):
    text = user_input.lower().strip()
    return any(word in text for word in EXIT_KEYWORDS)


def chat():
    print("Chatbot: Hi! I'm a simple rule-based chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if is_exit(user_input):
            print(f"Chatbot: {get_response(user_input)}")
            break

        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chat()