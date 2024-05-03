def is_safe(board, row, col, n):

    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))
    print()

def solve_n_queens_util(chessboard, col, n):
    if col == n:
        print_solution(chessboard)
        return True

    res = False
    for i in range(n):
        if is_safe(chessboard, i, col, n):
            chessboard[i][col] = 1
            res = solve_n_queens_util(chessboard, col + 1, n) or res
            chessboard[i][col] = 0  

    return res

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist.")
    else:
        print("All solutions found.")


solve_n_queens(4)
