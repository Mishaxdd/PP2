import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 24)

player = MusicPlayer("music")

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)

    screen.fill((30, 30, 30))

    # текст трека
    text = font.render("Track: " + player.get_current_track(), True, (255, 255, 255))
    screen.blit(text, (20, 50))

    # инструкции
    controls = [
        "P - Play",
        "S - Stop",
        "N - Next",
        "B - Back",
        "Q - Quit"
    ]

    for i, c in enumerate(controls):
        t = font.render(c, True, (180, 180, 180))
        screen.blit(t, (20, 120 + i * 30))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.previous_track()

            elif event.key == pygame.K_q:
                running = False

pygame.quit()