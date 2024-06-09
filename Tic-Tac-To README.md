# Tic-Tac-Toe with Minimax AI

This repository contains a Tic-Tac-Toe game implemented in Python. The game features a simple AI opponent that uses the Minimax algorithm with alpha-beta pruning to play optimally against the player.

## Features

- Play Tic-Tac-Toe against an AI opponent.
- AI uses Minimax algorithm with alpha-beta pruning for optimal moves.
- Check for win, loss, or draw conditions.
- Interactive console-based gameplay.

## Technologies Used

- Python: The programming language used to implement the Tic-Tac-Toe game and AI.

## How It Works

The game is played on a 3x3 board. The player is 'X' and the AI is 'O'. The player and AI take turns to place their marks on the board. The AI uses the Minimax algorithm with alpha-beta pruning to determine the best possible move. The game checks for win, loss, or draw conditions after each move.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/tic-tac-toe-ai.git
```

2. **Navigate to the project directory:**

```bash
cd tic-tac-toe-ai
```

3. **Run the Tic-Tac-Toe game:**

```bash
python tic_tac_toe.py
```

## Usage

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
