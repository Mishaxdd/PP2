"""
Music Player - Practice 7 Task 3.2
Interactive music player with keyboard controls.

Controls:
  P — Play / Resume
  S — Stop
  N — Next track
  B — Previous (Back) track
  Q / ESC — Quit
"""

import pygame
import sys
import os
from player import MusicPlayer

# Window settings
WIDTH, HEIGHT = 520, 400
FPS = 30
TITLE = "Music Player"

# Colors
BG_COLOR      = (18, 18, 30)
PANEL_COLOR   = (30, 30, 50)
ACCENT        = (100, 220, 150)
TEXT_COLOR    = (230, 230, 230)
DIM_COLOR     = (120, 120, 140)
PLAY_COLOR    = (80, 200, 120)
STOP_COLOR    = (200, 80, 80)
BTN_COLOR     = (50, 50, 80)
BTN_HOVER     = (70, 70, 110)


def draw_progress_bar(screen, player, x, y, w, h):
    """Draw a fake animated progress bar (position not available in pygame.mixer)."""
    pygame.draw.rect(screen, (50, 50, 70), (x, y, w, h), border_radius=4)
    if player.is_playing and pygame.mixer.music.get_busy():
        pos_ms = pygame.mixer.music.get_pos()  # ms since play started
        # Show scrolling bar — wrap every 30 seconds for visual feedback
        fraction = (pos_ms % 30000) / 30000
        pygame.draw.rect(screen, ACCENT,
                         (x, y, int(w * fraction), h), border_radius=4)


def draw_key_hint(screen, font, key, label, x, y, active=False):
    """Draw a single keyboard shortcut hint."""
    color = BTN_HOVER if active else BTN_COLOR
    rect = pygame.Rect(x, y, 48, 36)
    pygame.draw.rect(screen, color, rect, border_radius=6)
    pygame.draw.rect(screen, ACCENT if active else DIM_COLOR, rect, 2, border_radius=6)

    key_surf = font.render(key, True, ACCENT if active else TEXT_COLOR)
    screen.blit(key_surf, key_surf.get_rect(center=(x + 24, y + 11)))

    label_font = pygame.font.SysFont("Arial", 12)
    label_surf = label_font.render(label, True, DIM_COLOR)
    screen.blit(label_surf, label_surf.get_rect(center=(x + 24, y + 26)))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Music folder next to this script
    music_folder = os.path.join(os.path.dirname(__file__), "music")
    player = MusicPlayer(music_folder)

    # Fonts
    title_font   = pygame.font.SysFont("Arial", 26, bold=True)
    track_font   = pygame.font.SysFont("Arial", 20, bold=True)
    info_font    = pygame.font.SysFont("Arial", 15)
    key_font     = pygame.font.SysFont("Arial", 16, bold=True)

    last_key = None  # For visual key feedback

    running = True
    while running:
        # --- Event handling ---
        last_key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False
                elif event.key == pygame.K_p:
                    player.play()
                    last_key = "P"
                elif event.key == pygame.K_s:
                    player.stop()
                    last_key = "S"
                elif event.key == pygame.K_n:
                    player.next_track()
                    last_key = "N"
                elif event.key == pygame.K_b:
                    player.prev_track()
                    last_key = "B"

        # --- Drawing ---
        screen.fill(BG_COLOR)

        # Title bar
        pygame.draw.rect(screen, PANEL_COLOR, (0, 0, WIDTH, 60))
        title_surf = title_font.render("🎵  Music Player", True, TEXT_COLOR)
        screen.blit(title_surf, (20, 15))

        # Track info panel
        pygame.draw.rect(screen, PANEL_COLOR, (20, 80, WIDTH - 40, 110), border_radius=12)

        # Status indicator
        status = player.get_status()
        status_color = PLAY_COLOR if status == "Playing" else STOP_COLOR
        pygame.draw.circle(screen, status_color, (45, 110), 8)
        status_surf = info_font.render(status, True, status_color)
        screen.blit(status_surf, (60, 102))

        # Track name
        track_name = player.get_current_track_name()
        if len(track_name) > 34:
            track_name = track_name[:31] + "..."
        track_surf = track_font.render(track_name, True, TEXT_COLOR)
        screen.blit(track_surf, (35, 125))

        # Track counter
        if player.has_tracks():
            counter = f"Track {player.get_current_index() + 1} / {player.get_track_count()}"
        else:
            counter = "Add .mp3 / .wav files to the music/ folder"
        counter_surf = info_font.render(counter, True, DIM_COLOR)
        screen.blit(counter_surf, (35, 158))

        # Progress bar
        draw_progress_bar(screen, player, 20, 210, WIDTH - 40, 14)

        # Keyboard controls
        controls_y = 250
        ctrl_label = info_font.render("Keyboard Controls:", True, DIM_COLOR)
        screen.blit(ctrl_label, (20, controls_y))

        controls_y += 28
        keys = [
            ("P", "Play",  last_key == "P"),
            ("S", "Stop",  last_key == "S"),
            ("N", "Next",  last_key == "N"),
            ("B", "Back",  last_key == "B"),
            ("Q", "Quit",  False),
        ]
        for i, (k, lbl, active) in enumerate(keys):
            draw_key_hint(screen, key_font, k, lbl, 20 + i * 62, controls_y, active)

        # No tracks hint
        if not player.has_tracks():
            hint = info_font.render(
                "Place audio files in the music/ folder and restart.", True, (180, 130, 60))
            screen.blit(hint, hint.get_rect(center=(WIDTH // 2, 360)))

        pygame.display.flip()
        clock.tick(FPS)

    player.stop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
