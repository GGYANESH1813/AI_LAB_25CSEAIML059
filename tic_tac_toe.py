
def check_winner(board):
    # All possible winning combinations
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in lines:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


def minimax(board, is_max):
    result = check_winner(board)

    # Terminal state scores
    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_max:
        # AI (O) tries to maximize the score
        best = float("-inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best = max(best, score)

        return best

    else:
        # Opponent (X) tries to minimize the score
        best = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best = min(best, score)

        return best


# Initial board from your handwritten program
board = ["X", "O", "X",
         "O", "O", " ",
         "X", " ", " "]

best_score = float("-inf")
best_move = -1

# Find the best move for AI (O)
for i in range(9):
    if board[i] == " ":
        board[i] = "O"
        score = minimax(board, False)
        board[i] = " "

        if score > best_score:
            best_score = score
            best_move = i

# Make the best move
if best_move != -1:
    board[best_move] = "O"
    print("AI chosen position:", best_move + 1)

# Display the board
print("\nFinal Tic-Tac-Toe Board:")
for i in range(0, 9, 3):
    print(" | ".join(board[i:i + 3]))
    if i < 6:
        print("--+---+--")

# Display the result
result = check_winner(board)

if result == "O":
    print("AI (O) wins!")
elif result == "X":
    print("Player (X) wins!")
elif result == "Draw":
    print("Game is a draw!")
else:
    print("Game is not over yet.")