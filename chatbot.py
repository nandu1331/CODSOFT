import re

def simple_chatbot(user_input):
    # Define patterns and corresponding responses
    patterns_responses = [
        (r"hi|hello|hey", "Hello! How can I help you?"),
        (r"how are you", "I'm just a computer program, but thanks for asking!"),
        (r"what is your name", "I'm a simple chatbot. You can call me ChatGPT."),
        (r"bye|goodbye", "Goodbye! If you have more questions, feel free to ask."),
        (r"\bthanks\b|\bthank you\b", "You're welcome!"),
    ]

    # Check user input against patterns
    for pattern, response in patterns_responses:
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # Default response if no patterns match
    return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Simple loop for interacting with the chatbot
    
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)

