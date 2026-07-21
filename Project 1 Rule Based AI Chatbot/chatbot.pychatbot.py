"""

Project: Rule-Based AI Chatbot
Author: Rabeel Fatima
Technology: Python
AI Type: Rule-Based System

Features:
- Greeting users
- Help menu
- Introduces itself
- Responds to common questions
- Shows current date
- Shows current time
- Tells random jokes
- Gives motivational quotes
- Handles unknown inputs
- Exits gracefully

"""

import random
from datetime import datetime


print("=" * 55)
print("🤖 Welcome to the Rule-Based AI Chatbot")
print("=" * 55)
print("Type 'help' to see available commands.")
print("Type 'bye' or 'exit' to quit.\n")


# ------------------------------
# Lists used for random responses
# ------------------------------

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python programmer wear glasses? Because they couldn't C.",
    "Debugging is like being the detective in a crime movie where you are also the criminal."
]

quotes = [
    "Believe in yourself. Every expert was once a beginner.",
    "Success is the sum of small efforts repeated every day.",
    "Keep learning. Keep building. Keep improving.",
    "Don't stop until you're proud."
]


# ------------------------------
# Main Chatbot Loop
# ------------------------------

while True:

    user = input("You: ").strip().lower()

    # ------------------------------
    # Greetings
    # ------------------------------
    if any(word in user for word in [
        "hello", "hi", "hey", "good morning",
        "good afternoon", "good evening"
    ]):
        print("Bot: Hello! Nice to meet you. How can I help you today?")

    # ------------------------------
    # Introduction
    # ------------------------------
    elif "your name" in user or "who are you" in user:
        print("Bot: I'm a Rule-Based AI Chatbot created using Python.")

    elif "who made you" in user or "who created you" in user:
        print("Bot: I was created by Rabeel Fatima using Python.")

    # ------------------------------
    # Conversation
    # ------------------------------
    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif (
        "what can you do" in user
        or "help me" in user
        or "your features" in user
    ):
        print("Bot: I can greet you, tell jokes, motivate you, show the date and time, and answer some predefined questions.")

    # ------------------------------
    # Date
    # ------------------------------
    elif "date" in user:
        today = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {today}")

    # ------------------------------
    # Time
    # ------------------------------
    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Bot: Current time is {current_time}")

    # ------------------------------
    # Jokes
    # ------------------------------
    elif any(word in user for word in [
        "joke",
        "funny",
        "make me laugh",
        "another joke"
    ]):
        print("Bot:", random.choice(jokes))

    # ------------------------------
    # Motivation
    # ------------------------------
    elif any(phrase in user for phrase in [
        "motivate",
        "motivation",
        "encourage",
        "inspire",
        "quote"
    ]):
        print("Bot:", random.choice(quotes))

    # ------------------------------
    # Thanks
    # ------------------------------
    elif any(word in user for word in [
        "thank",
        "thanks",
        "thank you"
    ]):
        print("Bot: You're welcome! Happy to help!")

    # ------------------------------
    # Goodbye
    # ------------------------------
    elif any(word in user for word in [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "see you"
    ]):
        print("Bot: Goodbye! 👋 Have a wonderful day.")
        break

    # ------------------------------
    # Help
    # ------------------------------
    elif "help" in user:
        print("\nI understand commands like:")
        print("--------------------------------")
        print("• hello")
        print("• hi there")
        print("• how are you")
        print("• what is your name")
        print("• who made you")
        print("• what can you do")
        print("• tell me a joke")
        print("• another joke")
        print("• motivate me")
        print("• inspire me")
        print("• what is the date")
        print("• what time is it")
        print("• thanks")
        print("• bye")
        print("--------------------------------\n")

    # ------------------------------
    # Empty input
    # ------------------------------
    elif user == "":
        print("Bot: Please type something.")

    # ------------------------------
    # Unknown
    # ------------------------------
    else:
        print("Bot: I'm not sure I understand.")
        print("Bot: Try asking things like:")
        print("     • Tell me a joke")
        print("     • Motivate me")
        print("     • What time is it?")
        print("     • What can you do?")
