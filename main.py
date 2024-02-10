board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8], 
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def solve(board):
    empty = find_empty(board)

    if empty:
        row, col = empty
    else:
        return True

    for i in range(1,10):
        if check(board, (row,col), i):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False


def check(board, row_and_col, num):
    # Checking rows
    for i in range(0, len(board)):
        if board[row_and_col[0]][i] == num and row_and_col[1] != i:
            return False

    # Checking columns
    for i in range(0,len(board)):
        if board[i][row_and_col[1]] == num and row_and_col[1] != i:
            return False

    # Checking box
    box1 = row_and_col[0]//3
    box2 = row_and_col[1]//3

    for i in range(box1*3, box1*3 + 3):
        for k in range(box2*3, box2*3+3):
            if board[i][k] == num and (i,k) != row_and_col:
                return False
    
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board)
solve(board)
print("\n")
print_board(board)





