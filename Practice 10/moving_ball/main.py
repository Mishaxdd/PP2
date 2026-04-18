"""
Moving Ball Game - Practice 7 Task 3.3

Controls:
  Arrow Keys — Move the ball (20px per press)
  ESC        — Quit

Rules:
  - Ball cannot leave the screen boundaries
  - Moves that would take the ball off-screen are ignored
"""

import pygame
import sys
from ball import Ball

# Window settings
WIDTH, HEIGHT = 600, 500
FPS = 60
TITLE = "Moving Ball Game"
BG_COLOR = (245, 245, 245)  # White background (spec requirement)
GRID_COLOR = (230, 230, 230)


def draw_grid(screen):
    """Draw a subtle grid for visual reference."""
    step = 40
    for x in range(0, WIDTH, step):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, step):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y))


def draw_ui(screen, ball, font):
    """Draw position info and controls hint."""
    # Position display
    pos_text = font.render(f"Position: ({ball.x}, {ball.y})", True, (80, 80, 80))
    screen.blit(pos_text, (10, 10))

    # Controls hint
    hint = font.render("Arrow Keys: Move  |  ESC: Quit", True, (150, 150, 150))
    screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 18)))

    # Boundary warning indicators
    warn_color = (220, 100, 100)
    r = ball.RADIUS
    if ball.x == r:
        pygame.draw.rect(screen, warn_color, (0, 0, 4, HEIGHT))   # Left wall
    if ball.x == WIDTH - r:
        pygame.draw.rect(screen, warn_color, (WIDTH - 4, 0, 4, HEIGHT))  # Right wall
    if ball.y == r:
        pygame.draw.rect(screen, warn_color, (0, 0, WIDTH, 4))    # Top wall
    if ball.y == HEIGHT - r:
        pygame.draw.rect(screen, warn_color, (0, HEIGHT - 4, WIDTH, 4))  # Bottom wall


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    ball = Ball(WIDTH, HEIGHT)
    font = pygame.font.SysFont("Arial", 16)

    running = True
    while running:
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    ball.move("up")
                elif event.key == pygame.K_DOWN:
                    ball.move("down")
                elif event.key == pygame.K_LEFT:
                    ball.move("left")
                elif event.key == pygame.K_RIGHT:
                    ball.move("right")

        # --- Drawing ---
        screen.fill(BG_COLOR)
        draw_grid(screen)
        ball.draw(screen)
        draw_ui(screen, ball, font)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
