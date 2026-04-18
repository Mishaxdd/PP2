import pygame
import datetime
import math
import os


class MickeysClock:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)

        # Load hand image (fallback to drawn hand if image missing)
        self.hand_image = self._load_hand_image()

    def _load_hand_image(self):
        """Load Mickey Mouse hand image, or return None to use drawn fallback."""
        path = os.path.join(os.path.dirname(__file__), "images", "mickey_hand.png")
        if os.path.exists(path):
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, (30, 80))
        return None

    def _draw_hand(self, angle_deg, length, color, width):
        """
        Draw a clock hand from center.
        angle_deg: 0 = up (12 o'clock), increases clockwise.
        """
        angle_rad = math.radians(angle_deg)
        end_x = self.center[0] + length * math.sin(angle_rad)
        end_y = self.center[1] - length * math.cos(angle_rad)

        if self.hand_image:
            # Rotate image: pygame rotates counter-clockwise, so negate angle
            rotated = pygame.transform.rotate(self.hand_image, -angle_deg)
            rect = rotated.get_rect(center=(
                self.center[0] + (length // 2) * math.sin(angle_rad),
                self.center[1] - (length // 2) * math.cos(angle_rad)
            ))
            self.screen.blit(rotated, rect)
        else:
            # Fallback: draw a thick gloved hand shape
            pygame.draw.line(self.screen, color, self.center,
                             (int(end_x), int(end_y)), width)
            # Draw circle at tip to simulate glove
            pygame.draw.circle(self.screen, color, (int(end_x), int(end_y)), width + 4)

    def _draw_clock_face(self):
        """Draw the clock face background and hour markers."""
        # Clock face circle
        pygame.draw.circle(self.screen, (255, 255, 255), self.center, 160, 0)
        pygame.draw.circle(self.screen, (30, 30, 30), self.center, 160, 4)

        # Minute markers
        for i in range(60):
            angle = math.radians(i * 6)
            if i % 5 == 0:
                r_inner, r_outer, lw = 135, 155, 3
            else:
                r_inner, r_outer, lw = 145, 155, 1
            sx = self.center[0] + r_inner * math.sin(angle)
            sy = self.center[1] - r_inner * math.cos(angle)
            ex = self.center[0] + r_outer * math.sin(angle)
            ey = self.center[1] - r_outer * math.cos(angle)
            pygame.draw.line(self.screen, (30, 30, 30),
                             (int(sx), int(sy)), (int(ex), int(ey)), lw)

        # Center dot
        pygame.draw.circle(self.screen, (30, 30, 30), self.center, 8)

    def draw(self):
        """Draw the full clock for the current time."""
        now = datetime.datetime.now()
        minutes = now.minute
        seconds = now.second

        # Angles: 0° = 12 o'clock, clockwise
        minute_angle = minutes * 6       # 360 / 60 = 6° per minute
        second_angle = seconds * 6       # 360 / 60 = 6° per second

        self._draw_clock_face()

        # Right hand = minutes (longer)
        self._draw_hand(minute_angle, 120, (220, 50, 50), 8)

        # Left hand = seconds (shorter, thinner)
        self._draw_hand(second_angle, 100, (50, 50, 220), 5)

        # Display digital time
        font = pygame.font.SysFont("Arial", 32, bold=True)
        time_text = now.strftime("%H:%M:%S")
        text_surf = font.render(time_text, True, (30, 30, 30))
        text_rect = text_surf.get_rect(center=(self.width // 2, self.height // 2 + 200))
        self.screen.blit(text_surf, text_rect)
