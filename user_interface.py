"""
Graphical User Interface for the Connect Four Application using Pygame.
"""

import pygame

# Constants
SquareSize = 100
Radius = SquareSize // 2 - 5

def draw_board(board, screen):
    for r in range(len(board)):
        for c in range(len(board[0])):
            pygame.draw.rect(screen, (0, 0, 255), (c * SquareSize, r * SquareSize + SquareSize, SquareSize, SquareSize))
            color = (0, 0, 0)
            if board[r][c] == 1:
                color = (255, 0, 0)
            elif board[r][c] == -1:
                color = (255, 255, 0)

            pygame.draw.circle(screen, color, (c * SquareSize + SquareSize // 2, r * SquareSize + SquareSize + SquareSize // 2), Radius)
    pygame.display.update()