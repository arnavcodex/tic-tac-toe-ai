from colorama import Fore, Style, init
import random

init(autoreset=True)

# ═══════════════════════════════════════════════
#          ARNAVCODEX TIC-TAC-TOE AI
#              Created by Arnav
# ═══════════════════════════════════════════════

WINNING_POSITIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


# ───────────────────────────────────────────────
# COLORS
# ───────────────────────────────────────────────

def symbol(value):
    if value == "X":
        return Fore.BLUE + "X" + Style.RESET_ALL
    elif value == "O":
        return Fore.RED + "O" + Style.RESET_ALL
    else:
        return " "


# ───────────────────────────────────────────────
# BOARD
# ───────────────────────────────────────────────

def show_board(board):
    print()
    print(f"        {symbol(board[0])} │ {symbol(board[1])} │ {symbol(board[2])}")
    print("       ───┼───┼───")
    print(f"        {symbol(board[3])} │ {symbol(board[4])} │ {symbol(board[5])}")
    print("       ───┼───┼───")
    print(f"        {symbol(board[6])} │ {symbol(board[7])} │ {symbol(board[8])}")
    print()


def show_empty_board():
    print()
    print("        1 │ 2 │ 3")
    print("       ───┼───┼───")
    print("        4 │ 5 │ 6")
    print("       ───┼───┼───")
    print("        7 │ 8 │ 9")
    print()


# ───────────────────────────────────────────────
# GAME LOGIC
# ───────────────────────────────────────────────

def check_winner(board):
    for a, b, c in WINNING_POSITIONS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]

    if all(board):
        return "DRAW"

    return None


def available_moves(board):
    return [i for i in range(9) if board[i] == ""]


# ───────────────────────────────────────────────
# MINIMAX AI
# ───────────────────────────────────────────────

def minimax(board, maximizing, ai, human):

    result = check_winner(board)

    if result == ai:
        return 10

    if result == human:
        return -10

    if result == "DRAW":
        return 0

    if maximizing:
        best_score = -999

        for move in available_moves(board):
            board[move] = ai
            score = minimax(board, False, ai, human)
            board[move] = ""

            best_score = max(best_score, score)

        return best_score

    else:
        best_score = 999

        for move in available_moves(board):
            board[move] = human
            score = minimax(board, True, ai, human)
            board[move] = ""

            best_score = min(best_score, score)

        return best_score


def best_move(board, ai, human):

    best_score = -999
    move_choice = None

    for move in available_moves(board):

        board[move] = ai

        score = minimax(
            board,
            False,
            ai,
            human
        )

        board[move] = ""

        if score > best_score:
            best_score = score
            move_choice = move

    return move_choice


# ───────────────────────────────────────────────
# MOVE INPUT
# ───────────────────────────────────────────────

def get_move(board, player):

    while True:

        try:
            move = int(input(f"  {player} move → "))

            if move < 1 or move > 9:
                print("  ❌ Enter a number from 1 to 9.")
                continue

            index = move - 1

            if board[index] != "":
                print("  ❌ That position is already occupied.")
                continue

            return index

        except ValueError:
            print("  ❌ Enter a valid number.")


# ───────────────────────────────────────────────
# RESULT
# ───────────────────────────────────────────────

def show_result(result):

    print()

    if result == "X":
        print(Fore.BLUE + "  🎉 X WINS!" + Style.RESET_ALL)

    elif result == "O":
        print(Fore.RED + "  🎉 O WINS!" + Style.RESET_ALL)

    else:
        print(Fore.YELLOW + "  🤝 IT'S A DRAW!" + Style.RESET_ALL)

    print()


# ═══════════════════════════════════════════════
#        🧠 BEST MOVE TELLER
# ═══════════════════════════════════════════════

def best_move_mode():

    while True:

        print()
        print("╔══════════════════════════════════════╗")
        print("║       🧠 BEST MOVE TELLER           ║")
        print("╚══════════════════════════════════════╝")
        print()
        print("  1. 🔵 I am X")
        print("  2. 🔴 I am O")
        print("  3. 🔙 Back")

        choice = input("\n  Choose your side → ").strip()

        if choice == "3":
            return

        if choice == "1":
            human = "X"
            opponent = "O"

        elif choice == "2":
            human = "O"
            opponent = "X"

        else:
            print("  ❌ Invalid choice.")
            continue

        # ───────────────────────────────────────
        # FIRST MOVE QUESTION
        # ───────────────────────────────────────

        while True:

            first = input(
                "\n  Are you moving first? (y/n) → "
            ).strip().lower()

            if first in ("y", "n"):
                break

            print("  ❌ Type y or n.")

        board = [""] * 9

        print()
        print("╔══════════════════════════════════════╗")
        print("║      🧠 ASSISTANT ACTIVATED         ║")
        print("╚══════════════════════════════════════╝")

        print()
        print(
            f"  You are "
            + (
                Fore.BLUE + human
                if human == "X"
                else Fore.RED + human
            )
            + Style.RESET_ALL
        )

        print("  💡 I will calculate YOUR best move.")
        print("  🎯 Game continues until it ends.")

        show_empty_board()

        # ───────────────────────────────────────
        # OPPONENT MOVES FIRST
        # ───────────────────────────────────────

        if first == "n":

            print(
                f"  {Fore.RED if opponent == 'O' else Fore.BLUE}"
                f"Enter {opponent}'s first move."
                f"{Style.RESET_ALL}"
            )

            move = get_move(board, opponent)
            board[move] = opponent

            print(
                f"  ✓ {opponent} placed at position {move + 1}"
            )

            show_board(board)

        # ───────────────────────────────────────
        # MAIN ASSISTANT GAME LOOP
        # ───────────────────────────────────────

        while True:

            # ═══════════════════════════════════
            # YOUR TURN
            # ═══════════════════════════════════

            print(
                f"  YOUR TURN "
                + (
                    Fore.BLUE + f"({human})"
                    if human == "X"
                    else Fore.RED + f"({human})"
                )
                + Style.RESET_ALL
            )

            print("  🧠 ANALYZING YOUR BEST MOVE...")

            move = best_move(
                board,
                human,
                opponent
            )

            print(
                f"  💡 BEST MOVE FOR "
                + (
                    Fore.BLUE + human
                    if human == "X"
                    else Fore.RED + human
                )
                + Style.RESET_ALL
                + f" → POSITION {move + 1}"
            )

            print()

            # User chooses whether to follow suggestion
            while True:

                user_move = input(
                    f"  {human} move → "
                ).strip()

                try:
                    user_move = int(user_move)

                    if user_move < 1 or user_move > 9:
                        print("  ❌ Choose position 1-9.")
                        continue

                    user_index = user_move - 1

                    if board[user_index] != "":
                        print("  ❌ Position already occupied.")
                        continue

                    break

                except ValueError:
                    print("  ❌ Enter a valid number.")

            board[user_index] = human

            print(
                f"  ✓ {human} placed at position {user_index + 1}"
            )

            show_board(board)

            result = check_winner(board)

            if result:
                show_result(result)
                break

            # ═══════════════════════════════════
            # OPPONENT TURN
            # ═══════════════════════════════════

            print(
                f"  {Fore.RED if opponent == 'O' else Fore.BLUE}"
                f"OPPONENT'S TURN ({opponent})"
                f"{Style.RESET_ALL}"
            )

            move = get_move(board, opponent)
            board[move] = opponent

            print(
                f"  ✓ {opponent} placed at position {move + 1}"
            )

            show_board(board)

            result = check_winner(board)

            if result:
                show_result(result)
                break

        input("  Press Enter to return to menu...")


# ═══════════════════════════════════════════════
# EASY AI
# ═══════════════════════════════════════════════

def easy_ai(board):
    return random.choice(available_moves(board))


# ═══════════════════════════════════════════════
# MEDIUM AI
# ═══════════════════════════════════════════════

def medium_ai(board, ai, human):

    # Try to win
    for move in available_moves(board):

        board[move] = ai

        if check_winner(board) == ai:
            board[move] = ""
            return move

        board[move] = ""

    # Block human
    for move in available_moves(board):

        board[move] = human

        if check_winner(board) == human:
            board[move] = ""
            return move

        board[move] = ""

    # Center
    if board[4] == "":
        return 4

    # Corners
    corners = [0, 2, 6, 8]
    free_corners = [
        move for move in corners
        if board[move] == ""
    ]

    if free_corners:
        return random.choice(free_corners)

    return random.choice(available_moves(board))


# ═══════════════════════════════════════════════
# 1V1 GAME
# ═══════════════════════════════════════════════

def play_1v1(difficulty):

    board = [""] * 9

    human = "X"
    ai = "O"

    print()
    print("╔══════════════════════════════════════╗")
    print(f"║      🎮 {difficulty.upper()} MODE")
    print("╚══════════════════════════════════════╝")

    print()
    print("  You are 🔵 X")
    print("  AI is 🔴 O")

    show_empty_board()

    while True:

        # Player
        print("  YOUR TURN 🔵 X")

        move = get_move(board, human)
        board[move] = human

        show_board(board)

        result = check_winner(board)

        if result:
            show_result(result)
            break

        # AI
        print("  🤖 AI THINKING...")

        if difficulty == "Easy":
            move = easy_ai(board)

        elif difficulty == "Medium":
            move = medium_ai(board, ai, human)

        else:
            move = best_move(board, ai, human)

        board[move] = ai

        print(
            f"  🤖 AI placed O at position {move + 1}"
        )

        show_board(board)

        result = check_winner(board)

        if result:
            show_result(result)
            break

    input("  Press Enter to return to menu...")


# ═══════════════════════════════════════════════
# DIFFICULTY MENU
# ═══════════════════════════════════════════════

def difficulty_menu():

    while True:

        print()
        print("╔══════════════════════════════════════╗")
        print("║           🎮 1V1 MODE              ║")
        print("╚══════════════════════════════════════╝")
        print()
        print("  1. 🟢 Easy")
        print("  2. 🟡 Medium")
        print("  3. 🔴 Impossible")
        print("  4. 🔙 Back")

        choice = input("\n  Choose difficulty → ").strip()

        if choice == "1":
            play_1v1("Easy")

        elif choice == "2":
            play_1v1("Medium")

        elif choice == "3":
            play_1v1("Impossible")

        elif choice == "4":
            return

        else:
            print("  ❌ Invalid choice.")


# ═══════════════════════════════════════════════
# MAIN MENU
# ═══════════════════════════════════════════════

def main():

    while True:

        print()
        print(Fore.CYAN + "╔══════════════════════════════════════╗")
        print("║      ARNAVCODEX TIC-TAC-TOE AI     ║")
        print("╚══════════════════════════════════════╝")
        print(Style.RESET_ALL)

        print("  ⚡ Created by Arnav")
        print("  💻 github.com/arnavcodex")
        print()
        print("  1. 🎮 1v1")
        print("  2. 🧠 Best Move Teller")
        print("  3. 🚪 Exit")

        choice = input("\n  Choose option → ").strip()

        if choice == "1":
            difficulty_menu()

        elif choice == "2":
            best_move_mode()

        elif choice == "3":
            print("\n  👋 Thanks for playing!")
            print("  ⚡ ArnavCodex\n")
            break

        else:
            print("  ❌ Invalid option.")


# ═══════════════════════════════════════════════

if __name__ == "__main__":
    main()
