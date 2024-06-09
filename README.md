# Python Projects Repository

This repository contains a collection of Python projects including a simple chatbot, a movie recommendation system, and a Tic-Tac-Toe game with Minimax AI. Each project is implemented with detailed code and instructions for usage.

## Table of Contents

1. [Simple Chatbot](#simple-chatbot)
   - [Description](#description)
   - [Features](#features)
   - [Usage](#usage)
2. [Movie Recommendation System](#movie-recommendation-system)
   - [Description](#description-1)
   - [Features](#features-1)
   - [Usage](#usage-1)
3. [Tic-Tac-Toe with Minimax AI](#tic-tac-toe-with-minimax-ai)
   - [Description](#description-2)
   - [Features](#features-2)
   - [Installation](#installation)
   - [Usage](#usage-2)
   - [Example Interaction](#example-interaction)
4. [License](#license)
5. [Contributing](#contributing)
6. [Contact](#contact)

## Simple Chatbot

### Description

A simple chatbot implemented in Python using regular expressions. The chatbot responds to predefined patterns in user input.

### Features

- Responds to greetings
- Replies to inquiries about its well-being
- Provides its name
- Bids farewell
- Acknowledges thanks

### Usage

1. Navigate to the Simple Chatbot directory:

```bash
cd python-projects/simple-chatbot
```

2. Run the chatbot script:

```bash
python chatbot.py
```

3. Interact with the chatbot in the console.

---

## Movie Recommendation System

### Description

A movie recommendation system that recommends movies based on genre similarity using TF-IDF vectorization and cosine similarity.

### Features

- Recommends movies based on genre similarity
- Uses TF-IDF vectorization
- Calculates cosine similarity

### Usage

1. Navigate to the Movie Recommendation System directory:

```bash
cd python-projects/movie-recommendation-system
```

2. Run the movie recommendation script:

```bash
python movie_recommendation.py
```

3. Example usage within the script:

```python
movie_title = 'Movie 4'
recommendations = get_recommendations(movie_title)
print(f"Top 10 movie recommendations for '{movie_title}':")
print(recommendations)
```

---

## Tic-Tac-Toe with Minimax AI

### Description

A Tic-Tac-Toe game with an AI opponent that uses the Minimax algorithm with alpha-beta pruning.

### Features

- Play against an AI opponent
- AI uses Minimax algorithm with alpha-beta pruning
- Checks for win, loss, or draw conditions

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-projects.git
```

2. Navigate to the Tic-Tac-Toe directory:

```bash
cd python-projects/tic-tac-toe
```

3. Run the Tic-Tac-Toe game:

```bash
python tic_tac_toe.py
```

### Usage

1. **Start the game:**

Run the `tic_tac_toe.py` script to start the game. The game will display an empty 3x3 board and prompt the player to enter their move.

2. **Make a move:**

Enter the row and column numbers (0, 1, or 2) to place your 'X' on the board.

3. **AI makes a move:**

The AI will make its move after the player. The board will be updated to show the AI's move.

4. **Game ends:**

The game will check for win, loss, or draw conditions after each move. If the game ends, a message will be displayed indicating the result.

### Example Interaction

```
Welcome to Tic-Tac-Toe!

  |   |  
---------
  |   |  
---------
  |   |  

Enter the row (0, 1, or 2): 0
Enter the column (0, 1, or 2): 0

X |   |  
---------
  |   |  
---------
  |   |  

AI is making a move...

X |   |  
---------
  | O |  
---------
  |   |  
```


## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.
