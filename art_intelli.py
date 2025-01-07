"""
File containing the AI Logic for the Connect-Four Game
"""

import math
from connect4_logic import is_valid_move, get_next_open_row, drop_piece, winning_move

def evaluate_window(window, piece):
    """
    Evaluate a window of four slots for scoring.
    """
    score = 0
    opponent_piece = -piece

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 5

    if window.count(opponent_piece) == 3 and window.count(0) == 1:
        score -= 8

    return score

def score_position(board, piece):
    """
    Score the board for a given player's piece.
    """
    score = 0

    # Score horizontal
    for r in range(len(board)):
        row = board[r]
        for c in range(len(row) - 3):
            window = row[c:c + 4]
            score += evaluate_window(window, piece)

    # Score vertical
    for c in range(len(board[0])):
        column = [board[r][c] for r in range(len(board))]
        for r in range(len(column) - 3):
            window = column[r:r + 4]
            score += evaluate_window(window, piece)

    # Score positive diagonals
    for r in range(len(board) - 3):
        for c in range(len(board[0]) - 3):
            window = [board[r + i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negative diagonals
    for r in range(3, len(board)):
        for c in range(len(board[0]) - 3):
            window = [board[r - i][c + i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    """
    Perform the minimax algorithm with alpha-beta pruning.
    """
    valid_moves = [col for col in range(len(board[0])) if is_valid_move(board, col)]
    is_terminal = len(valid_moves) == 0 or any(winning_move(board, p) for p in [1, -1])

    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, -1):  # AI wins
                return None, 1000000
            elif winning_move(board, 1):  # Human wins
                return None, -1000000
            else:  # Tie
                return None, 0
        return None, score_position(board, -1)

    if maximizingPlayer:
        value = -math.inf
        best_column = None
        for column in valid_moves:
            row = get_next_open_row(board, column)
            temp_board = [r[:] for r in board]  # Deep copy the board
            drop_piece(temp_board, row, column, -1)  # AI piece
            new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                best_column = column
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_column, value
    else:
        value = math.inf
        best_column = None
        for column in valid_moves:
            row = get_next_open_row(board, column)
            temp_board = [r[:] for r in board]  # Deep copy the board
            drop_piece(temp_board, row, column, 1)  # Human piece
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                best_column = column
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_column, value