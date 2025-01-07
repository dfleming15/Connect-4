rows = 6
columns = 7

def create_board():
    return [[0 for _ in range(columns)] for _ in range(rows)]

def is_valid_move(board, column):
    return board[0][column] == 0

def get_next_open_row(board, column):
    for r in range(rows - 1, -1, -1):
        if board[r][column] == 0:
            return r
        
def drop_piece(board, row, column, piece):
    board[row][column] = piece

def winning_move(board, piece):
    # Check horizontal locations for win
    for r in range(rows):
        for c in range(columns - 3):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for r in range(rows - 3):
        for c in range(columns):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for r in range(rows - 3):
        for c in range(columns - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for r in range(3, rows):
        for c in range(columns - 3):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True
    
    return False