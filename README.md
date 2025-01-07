This repository contains a Python-based implementation of the classic Connect 4 game with an intelligent AI opponent. The AI utilizes advanced algorithms such as α-β pruning and heuristic evaluation to provide a challenging gaming experience.

Features

Single-player mode: Play against the computer with a dynamic AI.
Intelligent AI: Implements α-β pruning and heuristics to make strategic decisions.
Interactive UI: Simple command-line interface for ease of use.

File Overview

main.py: Entry point of the program. Handles game flow and user interactions.
connect4_logic.py: Core logic for managing the Connect 4 game, including win conditions and board updates.
art_intelli.py: Implementation of the AI, including the α-β pruning algorithm and heuristic evaluation function.
user_interface.py: Handles the command-line interface and user interactions.


Getting Started

Prerequisites
Python 3.8 or higher
Basic knowledge of running Python scripts in the terminal

Installation
Clone the repository:
git clone https://github.com/your-username/connect4-ai.git
cd connect4-ai

Install required dependencies (if any):
pip install -r requirements.txt

Running the Game
Run the main.py file to start the game:
python main.py


AI Details

The AI opponent uses:

α-β pruning: Optimizes the decision-making process by pruning suboptimal branches in the game tree.
Heuristic evaluation: Assigns scores to board states based on potential winning opportunities.
Future Enhancements

Add a GUI for an improved visual experience.
Introduce difficulty levels for the AI.
Implement an online multiplayer mode.
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.

License

This project is licensed under the MIT License.
