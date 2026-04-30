import pygame
import chess

# --- Configuration ---
WIDTH, HEIGHT = 600, 600
SQ_SIZE = WIDTH // 8
COLORS = [(235, 235, 208), (119, 149, 86)]  # Light and Dark green board
HIGHLIGHT = (186, 202, 68)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Chess: PvP")

def draw_board(board, selected_sq):
    """Draws the board squares and highlights the selected one."""
    for r in range(8):
        for c in range(8):
            # Chess uses 0,0 at bottom-left; Pygame uses 0,0 at top-left
            # We map Pygame (r, c) to chess square
            sq = chess.square(c, 7 - r)
            color = HIGHLIGHT if sq == selected_sq else COLORS[(r + c) % 2]
            pygame.draw.rect(screen, color, (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
            # Draw piece using Unicode characters (simple placeholder)
            piece = board.piece_at(sq)
            if piece:
                font = pygame.font.SysFont("Segoe UI Symbol", 50)
                # piece.unicode_symbol() returns the actual chess glyph
                text = font.render(piece.unicode_symbol(), True, (0, 0, 0))
                text_rect = text.get_rect(center=(c * SQ_SIZE + SQ_SIZE // 2, r * SQ_SIZE + SQ_SIZE // 2))
                screen.blit(text, text_rect)

def main():
    board = chess.Board()
    running = True
    selected_sq = None

    while running:
        draw_board(board, selected_sq)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = pos[0] // SQ_SIZE, 7 - (pos[1] // SQ_SIZE)
                sq = chess.square(col, row)

                if selected_sq is None:
                    # Select a piece if it's the current player's turn
                    piece = board.piece_at(sq)
                    if piece and piece.color == board.turn:
                        selected_sq = sq
                else:
                    # Attempt a move
                    move = chess.Move(selected_sq, sq)
                    
                    # Basic Pawn Promotion (Always to Queen for simplicity)
                    if board.piece_at(selected_sq).piece_type == chess.PAWN:
                        if (board.turn == chess.WHITE and row == 7) or (board.turn == chess.BLACK and row == 0):
                            move.promotion = chess.QUEEN

                    if move in board.legal_moves:
                        board.push(move)
                        print(f"Move: {move.uci()} | Turn: {'White' if board.turn else 'Black'}")
                    
                    selected_sq = None # Deselect after attempt

        # Check for Game Over
        if board.is_game_over():
            print(f"Game Over: {board.result()}")
            running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
