board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
player = input("Enter what symbol you want: ")
start = int(input("Enter who to start (0 for computer / 1 for human): "))

def is_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'X':
            return 1  # 'X' won
        elif board[i][0] == board[i][1] == board[i][2] == 'O':
            return 2  # 'O' won

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            return 1  # 'X' won
        elif board[0][i] == board[1][i] == board[2][i] == 'O':
            return 2  # 'O' won

    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[2][0] == board[1][1] == board[0][2] == 'X':
        return 1  # 'X' won
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[2][0] == board[1][1] == board[0][2] == 'O':
        return 2  # 'O' won

    if all(board[row][column] != '.' for row in range(3) for column in range(3)):
        return 0  # Draw

    return 3  # Game continuing

def minimax(board, depth, is_maximizing, player, player2):
    state = is_winner(board)

    if state in [1, 2]:
        if state == 1 and player == 'X':
            return -1
        elif state == 2 and player == 'O':
            return -1
        if state == 1 and player == 'O':
            return 1
        if state == 2 and player == 'X':
            return 1

    if all(board[row][column] != '.' for row in range(3) for column in range(3)):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = player2
                    score = minimax(board, depth + 1, False, player, player2)
                    board[i][j] = '.'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    board[i][j] = player
                    score = minimax(board, depth + 1, True, player, player2)
                    board[i][j] = '.'
                    best_score = min(score, best_score)
        return best_score

def computer_turn(board, player, player2):
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                board[i][j] = player2
                score = minimax(board, 0, False, player, player2)
                print(score)
                board[i][j] = '.'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = player2

def print_board(board):
    for row in board:
        print(row)

if start == 1:

    if player == 'X':
        while True:
            print("Enter the row and column number of the place where you want to play X")
            row = int(input("Enter row here: "))
            player2 = 'O'
            column = int(input("Enter column here: "))
            board[row - 1][column - 1] = 'X'
            if is_winner(board) == 1:
                print_board(board)
                print("GAME OVER")
                break
            print("Current board configuration is")
            print_board(board)
            computer_turn(board, 'X', 'O')
            if is_winner(board) == 2:
                print("O won")
                print_board(board)
                break
            print("Computer played. Current board configuration is")
            print_board(board)

    else:
        while True:
            print("Enter the row and column number of the place where you want to play O")
            row = int(input("Enter row here: "))
            player2 = 'X'
            column = int(input("Enter column here: "))
            board[row - 1][column - 1] = 'O'
            if is_winner(board) == 2:
                print("O won")
                break
            print("Current configuration is")
            print_board(board)
            computer_turn(board, 'O', 'X')
            if is_winner(board) == 1:
                print("X won")
                print_board(board)
                break
            print("Computer played. Current board configuration is")
            print_board(board)
else:
    if player == 'X':
        while True:
            computer_turn(board, 'X', 'O')
            if is_winner(board) == 2:
                print("O won")
                print_board(board)
                break
            print("Computer played. Current board configuration is")
            print_board(board)

            print("Enter the row and column number of the place where you want to play X")
            row = int(input("Enter row here: "))
            player2 = 'O'
            column = int(input("Enter column here: "))
            board[row - 1][column - 1] = 'X'
            if is_winner(board) == 1:
                print_board(board)
                print("GAME OVER")
                break
            print("Current board configuration is")
            print_board(board)
            

    else:
        while True:
            computer_turn(board, 'O', 'X')
            if is_winner(board) == 1:
                print("X won")
                print_board(board)
                break
            print("Computer played. Current board configuration is")
            print_board(board)
            
            print("Enter the row and column number of the place where you want to play O")
            row = int(input("Enter row here: "))
            player2 = 'X'
            column = int(input("Enter column here: "))
            board[row - 1][column - 1] = 'O'
            if is_winner(board) == 2:
                print("O won")
                break
            print("Current configuration is")
            print_board(board)
            