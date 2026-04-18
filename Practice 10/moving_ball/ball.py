"""
ball.py — Ball class for the Moving Ball game.
"""

import pygame


class Ball:
    RADIUS = 25
    DIAMETER = RADIUS * 2   # 50px as per spec
    STEP = 20               # Pixels per key press
    COLOR = (220, 50, 50)   # Red
    OUTLINE_COLOR = (160, 20, 20)

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Start in center
        self.x = screen_width // 2
        self.y = screen_height // 2

    def move(self, direction):
        """
        Move ball by STEP in the given direction.
        direction: 'up', 'down', 'left', 'right'
        Ignores input that would move the ball off-screen.
        """
        new_x, new_y = self.x, self.y

        if direction == "up":
            new_y -= self.STEP
        elif direction == "down":
            new_y += self.STEP
        elif direction == "left":
            new_x -= self.STEP
        elif direction == "right":
            new_x += self.STEP

        # Boundary check — ignore move if it would go out of bounds
        if (self.RADIUS <= new_x <= self.screen_width - self.RADIUS and
                self.RADIUS <= new_y <= self.screen_height - self.RADIUS):
            self.x = new_x
            self.y = new_y

    def draw(self, screen):
        """Draw the ball with a subtle shadow and outline."""
        # Shadow
        pygame.draw.circle(screen, (180, 180, 180),
                           (self.x + 4, self.y + 4), self.RADIUS)
        # Main ball
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.RADIUS)
        # Outline
        pygame.draw.circle(screen, self.OUTLINE_COLOR,
                           (self.x, self.y), self.RADIUS, 3)
        # Highlight
        pygame.draw.circle(screen, (255, 130, 130),
                           (self.x - 8, self.y - 8), 7)
