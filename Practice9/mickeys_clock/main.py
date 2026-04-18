import pygame
from clock import MickeyClock

pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Mickey's Clock")

BASE_PATH = r'C:\Users\User\work\practice9\mickeys_clock\images'

mickey_clock = MickeyClock(screen, BASE_PATH)
clock_fps = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    mickey_clock.update()

    pygame.display.flip()
    clock_fps.tick(60)

pygame.quit()