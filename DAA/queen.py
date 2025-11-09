# 8-Queens Problem using Backtracking

N = 8  # chessboard size

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

# Check if a queen can be placed safely
def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Solve N-Queens recursively
def solve_queens(board, row):
    # Base condition: All queens are placed
    if row >= N:
        print("Final 8-Queens Solution:")
        print_board(board)
        return True

    # Try placing a queen in each column
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen

            if solve_queens(board, row + 1):
                return True  # Solution found

            board[row][col] = 0  # Backtrack

    return False

# --- MAIN PROGRAM ---
if __name__ == "__main__":
    # Create 8x8 chessboard initialized to 0
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Place the first queen (example: first row, 0th column)
    first_row, first_col = map(int, input("Enter position of first queen (row col): ").split())
    board[first_row][first_col] = 1

    # Start solving from next row
    if not solve_queens(board, first_row + 1):
        print("No solution exists.")
