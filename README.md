🎮 ArnavCodex — Tic-Tac-Toe AI

«🧠 A terminal-based Tic-Tac-Toe game featuring multiple AI difficulties and a real-time Best Move Teller powered by the Minimax algorithm.»

"Python" (https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
"AI" (https://img.shields.io/badge/AI-Minimax-purple?style=for-the-badge)
"Terminal" (https://img.shields.io/badge/Interface-Terminal-black?style=for-the-badge)
"Status" (https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

✨ About The Project

Tic-Tac-Toe AI is a lightweight but powerful terminal game built with Python.

The project includes:

- 🎮 1v1 Game Mode
- 🟢 Easy AI
- 🟡 Medium AI
- 🔴 Impossible AI
- 🧠 Best Move Teller
- 🎨 Colorful terminal interface
- ⚡ Instant AI calculations
- 🧩 Minimax-based optimal decision making
- 🔢 Simple 1–9 position system

The goal wasn't just to make a basic Tic-Tac-Toe game — it was to build a small project that demonstrates game logic, AI decision-making, algorithms, and clean Python development.

---

🧠 AI Difficulty

🟢 Easy

The AI chooses a random available position.

Perfect for beginners.

🟡 Medium

The AI uses basic strategy:

- Attempts to win
- Blocks the opponent
- Takes the center
- Uses corners
- Adds some randomness

🔴 Impossible

The Impossible AI uses the Minimax algorithm.

It evaluates possible future game states and chooses an optimal move.

«🎯 The AI cannot be beaten when Minimax is implemented correctly. The strongest possible result against it is a draw.»

---

🧠 Best Move Teller

This is one of the main features of the project.

Instead of simply playing against the AI, you can use the program as a Tic-Tac-Toe assistant.

You choose:

1. 🔵 I am X
2. 🔴 I am O

Then:

Are you moving first? (y/n)

The assistant continuously analyzes the current board and tells you the best move for your selected side.

Example:

YOUR TURN (X)

🧠 ANALYZING YOUR BEST MOVE...

💡 BEST MOVE FOR X → POSITION 5

X move → 5
✓ X placed at position 5

The game continues until:

- 🏆 X wins
- 🏆 O wins
- 🤝 Draw

No manual board reconstruction is required between turns.

---

🧩 How It Works

The project uses several core programming concepts:

Python
  │
  ├── Game Board
  │
  ├── Win Detection
  │
  ├── Move Validation
  │
  ├── AI Difficulty System
  │
  ├── Minimax Algorithm
  │
  └── Terminal UI

Minimax

The Impossible AI recursively evaluates possible moves.

Conceptually:

Current Position
       │
       ▼
Possible Moves
       │
       ▼
Future Game States
       │
       ▼
Evaluate Outcomes
       │
       ▼
Choose Optimal Move

This allows the AI to make decisions based on future game possibilities rather than simply choosing random positions.

---

🎮 Controls

The board uses numbers instead of coordinates:

  1 │ 2 │ 3
 ───┼───┼───
  4 │ 5 │ 6
 ───┼───┼───
  7 │ 8 │ 9

For example:

X move → 5

places X in the center.

---

🛠️ Tech Stack

Technology| Purpose
🐍 Python| Core programming language
🧠 Minimax| Optimal AI decision making
🎨 Colorama| Colored terminal interface
🎮 Game Logic| Board and win detection

---

📁 Project Structure

tic-tac-toe-ai/
│
├── main.py
└── README.md

Everything is intentionally kept inside a single Python file to make the project easy to understand, run, and modify.

---

🚀 Installation

Clone the repository:

git clone https://github.com/arnavcodex/tic-tac-toe-ai.git

Enter the project:

cd tic-tac-toe-ai

Install the required package:

pip install colorama

Run:

python main.py

---

💻 Main Menu

╔══════════════════════════════════════╗
║      ARNAVCODEX TIC-TAC-TOE AI     ║
╚══════════════════════════════════════╝

  ⚡ Created by Arnav
  💻 github.com/arnavcodex

  1. 🎮 1v1
  2. 🧠 Best Move Teller
  3. 🚪 Exit

---

🏗️ Part of the ArnavCodex Ecosystem

This project is part of my growing collection of coding and AI projects under ArnavCodex.

⚡ Team Nexus

Team Nexus is my collaborative coding/project ecosystem where I work on different experiments, tools, and ideas with other developers.

🤖 Zensis AI

Zensis AI is my AI-focused project and one of the larger projects in the ArnavCodex ecosystem.

While this Tic-Tac-Toe project is much smaller, it shares the same goal:

«Learn by building. Build by experimenting.»

---

🎯 Learning Goals

This project helped explore:

- Python functions
- Lists and loops
- Conditional logic
- Recursion
- Game-state evaluation
- Algorithmic thinking
- AI decision making
- Terminal UI design
- Input validation
- Git & GitHub workflow

---

🔮 Future Ideas

Possible future upgrades:

- 📊 Win/Loss statistics
- 🔄 Replay system
- 💾 Save game history
- 🏆 Leaderboard
- 🎨 More terminal themes
- 🌐 Web version
- 🤖 More advanced AI analysis
- 📈 Move analysis
- 🎮 Multiplayer mode

---

👨‍💻 Creator

Arnav

ArnavCodex

Python developer • AI enthusiast • Builder

🔗 GitHub: "@arnavcodex" (https://github.com/arnavcodex)

---

🤝 Team

Team Nexus

«Building projects, experimenting with technology, and learning together.»

Zensis AI

«An AI project from the ArnavCodex ecosystem.»

---

⭐ Support

If you found this project interesting, consider giving the repository a ⭐ on GitHub.

Every star motivates me to build the next project. 🚀

---

<div align="center">⚡ ARNAVCODEX

Code. Build. Experiment. Repeat.

Made with Python 🐍 and curiosity 🧠

</div>
