def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def solve_n_queens(board, row, n):
    if row == n:
        # All queens are placed successfully
        print("Solution:")
        print_board(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1

            # Recur for the next row
            solve_n_queens(board, row + 1, n)

            # Backtrack (remove the queen)
            board[row][col] = 0

if __name__ == "__main__":
    n = int(input("Enter the value of n for the N-Queens problem: "))

    # Initialize the chessboard with the first queen placed
    first_queen_col = int(input("Enter the column (0-indexed) for the first queen: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][first_queen_col] = 1

    # Solve the N-Queens problem using backtracking
    solve_n_queens(board, 1, n)
