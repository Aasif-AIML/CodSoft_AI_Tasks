# tictactoe.py
# CODSOFT - Task 2: Tic Tac Toe AI
# Unbeatable AI using Minimax Algorithm

import math

# Initialize board
board = [" " for _ in range(9)]  # 3x3 board

# Print board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check for winner
def winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_conditions)

# Check if board full
def full(brd):
    return " " not in brd

# Minimax Algorithm
def minimax(brd, depth, is_maximizing):
    if winner(brd, "O"):  # AI win
        return 1
    elif winner(brd, "X"):  # Human win
        return -1
    elif full(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Main game loop
def play():
    print("Welcome to Tic Tac Toe! (You = X, AI = O)")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        if winner(board, "X"):
            print_board()
            print("🎉 You win! (somehow...)")
            break
        elif full(board):
            print_board()
            print("🤝 It's a draw!")
            break

        # AI move
        ai_move()

        print_board()
        if winner(board, "O"):
            print("💻 AI wins! Better luck next time.")
            break
        elif full(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play()
