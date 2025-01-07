"""
Drew Fleming
Project 1: Connect-Four AI Game
CS 384: Artificial Intelligence
"""

import pygame
import math
from user_interface import draw_board
from connect4_logic import create_board, drop_piece, get_next_open_row, is_valid_move, winning_move
from art_intelli import minimax

# Game constants
rows = 6
columns = 7
squareSize = 100
radius = squareSize // 2 - 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def display_buttons(screen, play_again_rect, quit_rect):
    """
    Draws the "Play Again" and "Quit" buttons on the screen.
    """
    font = pygame.font.Font(None, 40)
    play_again_text = font.render("Play Again", True, WHITE)
    quit_text = font.render("Quit", True, WHITE)

    # Draw buttons
    screen.blit(play_again_text, play_again_rect)
    screen.blit(quit_text, quit_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((columns * squareSize, (rows + 1) * squareSize))
    pygame.display.set_caption("Connect-Four AI Game")
    clock = pygame.time.Clock()

    # Initialize the game
    board = create_board()
    game_over = False
    turn = 0  # 0 = Human, 1 = AI

    while True:
        draw_board(board, screen)  # Draw the board in each iteration

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if not game_over:  # Handle game interactions
                if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:  # Human's turn
                    column = event.pos[0] // squareSize
                    if is_valid_move(board, column):
                        row = get_next_open_row(board, column)
                        drop_piece(board, row, column, 1)

                        if winning_move(board, 1):
                            game_over = True
                            winner = "Player 1 (Human)"
                        turn = 1  # AI's turn

                if turn == 1 and not game_over:  # AI's turn
                    column, _ = minimax(board, 5, -math.inf, math.inf, True)
                    if column is not None and is_valid_move(board, column):
                        row = get_next_open_row(board, column)
                        drop_piece(board, row, column, -1)

                        if winning_move(board, -1):
                            game_over = True
                            winner = "Player 2 (AI)"
                        turn = 0  # Human's turn

        # Display "Game Over" with buttons when the game ends
        if game_over:
            draw_board(board, screen)  # Draw the final board state
            pygame.time.wait(1000)  # Wait briefly to show the final move

            # Set up button dimensions
            play_again_rect = pygame.Rect(
                columns * squareSize // 4, (rows + 1) * squareSize // 3, 150, 50
            )
            quit_rect = pygame.Rect(
                3 * (columns * squareSize // 4) - 150, (rows + 1) * squareSize // 3, 150, 50
            )

            # Draw buttons and overlay winner text
            display_buttons(screen, play_again_rect, quit_rect)
            font = pygame.font.Font(None, 60)
            winner_text = font.render(f"{winner} Wins!", True, WHITE)
            text_rect = winner_text.get_rect(center=(columns * squareSize // 2, (rows + 1) * squareSize // 6))
            screen.blit(winner_text, text_rect)
            pygame.display.update()

            # Wait for button interaction
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_again_rect.collidepoint(event.pos):  # Restart the game
                            main()
                        if quit_rect.collidepoint(event.pos):  # Quit the game
                            pygame.quit()
                            return
                clock.tick(30)  # Limit loop to 30 FPS

        clock.tick(30)  # Main game loop at 30 FPS


if __name__ == "__main__":
    main()
