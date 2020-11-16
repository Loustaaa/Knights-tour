#Python program to solve the knights tour problem using backtracking and recursion.

#Board list representing the 8x8 chessboard.
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]


def move(x, y, count, xmoves, ymoves):
    '''
        A recursive function that makes the moves and backtracks if a dead-end is reached.
    '''
    if count == 64:
        return True
    for i in range(8):
        if is_valid(x + xmoves[i], y + ymoves[i], board):
            board[x][y] = count
            if move(x + xmoves[i], y + ymoves[i], count + 1, xmoves, ymoves):
                return True
            board[x][y] = 0
    return False
        

def print_board(bo):
    '''
        Prints out the board graphic.
    '''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j == (len(board[0]) - 1):
                print(bo[i][j])
            else:
                if bo[i][j] >= 10:
                    print(bo[i][j], end=' ')
                else:
                    print(bo[i][j], end=' ')


def is_valid(x, y, board):
    '''
        Checks if the move is valid. Returns true if it is. Returns False if it is not.
    '''
    valid = False
    if x >= 0 and y >= 0 and x < len(board) and y < len(board) and board[x][y] == 0:
        return True
    return False



def solve(bo):
    '''
        prints the unsolved board, then either prints the solution if possible, or prints 'no solution' if none.
    '''
    print_board(board)
    print("Solving...")
    
    #Possible moves on the X axis.
    xmoves = [1, 2, 2, 1, -1, -2, -2, -1]
    #Possible moves on the y Y axis.
    ymoves = [2, 1, -1, -2, -2, -1, 1, 2]

    #Counts the moves on the board.
    counter = 1

    #The X and Y coordinates of the current move
    x_loc = 0
    y_loc = 0

    if not(move(x_loc, y_loc, counter, xmoves, ymoves)):
        print("No solution")
    else:
        print("                 ")
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    bo[i][j] = 64
        print_board(board)
    
solve(board)
        
