import pygame
import sys
from clock import MickeysClock
WIDTH, HEIGHT = 500, 550
FPS = 1  
TITLE = "Mickey's Clock"
BG_COLOR = (255, 248, 220) 
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock_tick = pygame.time.Clock()
    mickey_clock = MickeysClock(screen, WIDTH, HEIGHT)
    title_font = pygame.font.SysFont("Arial", 28, bold=True)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill(BG_COLOR)
        title_surf = title_font.render("Mickey's Clock", True, (180, 30, 30))
        screen.blit(title_surf, title_surf.get_rect(center=(WIDTH // 2, 35)))
        legend_font = pygame.font.SysFont("Arial", 16)
        screen.blit(legend_font.render("Right hand = Minutes", True, (220, 50, 50)),
                    (20, HEIGHT - 55))
        screen.blit(legend_font.render("Left hand = Seconds", True, (50, 50, 220)),
                    (20, HEIGHT - 30))
        mickey_clock.draw()

        pygame.display.flip()
        clock_tick.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
