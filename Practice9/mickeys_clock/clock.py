import pygame
import datetime
import os


class MickeyClock:
    def __init__(self, screen, base_path):
        image_surface = pygame.image.load(os.path.join(base_path, 'clock.png')).convert_alpha()
        mickey        = pygame.image.load(os.path.join(base_path, 'mUmrP.png')).convert_alpha()
        hand_l        = pygame.image.load(os.path.join(base_path, 'hand_left_centered.png')).convert_alpha()
        hand_r        = pygame.image.load(os.path.join(base_path, 'hand_right_centered.png')).convert_alpha()

        self.clock_img  = pygame.transform.scale(image_surface, (800, 600))
        self.mickey_img = pygame.transform.scale(mickey, (350, 350))
        self.hand_l     = pygame.transform.scale(hand_l, (80, 80))
        self.hand_r     = pygame.transform.scale(hand_r, (100, 100))

        self.screen        = screen
        self.CLOCK_CENTER  = (600, 320)
        self.MICKEY_CENTER = (300, 170)

    def update(self):
        now = datetime.datetime.now()
        m = now.minute
        s = now.second

        seconds_angle = -(s * 6)
        minutes_angle = -(m * 6 + s * 0.1)

        rotated_seconds = pygame.transform.rotate(self.hand_l, seconds_angle)
        rotated_minutes = pygame.transform.rotate(self.hand_r, minutes_angle)

        seconds_rect = rotated_seconds.get_rect(center=self.CLOCK_CENTER)
        minutes_rect = rotated_minutes.get_rect(center=self.CLOCK_CENTER)

        clock_rect = self.clock_img.get_rect(center=self.CLOCK_CENTER)
        self.screen.blit(self.clock_img, clock_rect)

        mic_rect = self.mickey_img.get_rect(center=self.MICKEY_CENTER)
        self.screen.blit(self.mickey_img, mic_rect)

        self.screen.blit(rotated_seconds, seconds_rect)
        self.screen.blit(rotated_minutes, minutes_rect)