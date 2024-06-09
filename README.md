# Simple Chatbot Project

This repository contains a simple chatbot implemented in Python using regular expressions. The chatbot can respond to a set of predefined patterns in user input, making it a basic yet functional conversational agent.

## Features

- Responds to greetings such as "hi", "hello", and "hey".
- Replies to inquiries about its well-being.
- Provides its name when asked.
- Bids farewell when prompted with "bye" or "goodbye".
- Acknowledges thanks from the user.
- Gives a default response when it doesn't understand the input.

## Technologies Used

- Python: The programming language used to implement the chatbot.
- Regular Expressions (re module): Used for pattern matching in user input.

## How It Works

The chatbot uses regular expressions to identify patterns in user input and responds with predefined messages. The script includes a simple loop that allows continuous interaction with the chatbot until the user types "exit".

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/simple-chatbot.git
```

2. **Navigate to the project directory:**

```bash
cd simple-chatbot
```

3. **Run the chatbot script:**

```bash
python chatbot.py
```

## Usage

- Start the script to begin interacting with the chatbot.
- Type a greeting, question, or farewell message to see the chatbot's response.
- Type "exit" to end the conversation and close the script.

### Example Interaction

```
You: hello
Chatbot: Hello! How can I help you?

You: what is your name
Chatbot: I'm a simple chatbot. You can call me ChatGPT.

You: thanks
Chatbot: You're welcome!

You: goodbye
Chatbot: Goodbye! If you have more questions, feel free to ask.
```

## Customization

You can customize the chatbot by modifying the `patterns_responses` list in the `simple_chatbot` function. Add more patterns and corresponding responses as needed.

```python
patterns_responses = [
    (r"hi|hello|hey", "Hello! How can I help you?"),
    (r"how are you", "I'm just a computer program, but thanks for asking!"),
    (r"what is your name", "I'm a simple chatbot. You can call me ChatGPT."),
    (r"bye|goodbye", "Goodbye! If you have more questions, feel free to ask."),
    (r"\bthanks\b|\bthank you\b", "You're welcome!"),
    # Add more patterns and responses here
]
```


## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.


