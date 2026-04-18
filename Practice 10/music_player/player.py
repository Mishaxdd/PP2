"""
player.py — Playlist and playback logic for the Music Player.
"""

import pygame
import os


class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = []       # List of (filename, display_name)
        self.current_index = 0
        self.is_playing = False
        self.is_stopped = True

        self._load_playlist()

    def _load_playlist(self):
        """Scan music folder for supported audio files."""
        supported = (".mp3", ".wav", ".ogg", ".flac")
        if not os.path.exists(self.music_folder):
            return
        for fname in sorted(os.listdir(self.music_folder)):
            if fname.lower().endswith(supported):
                full_path = os.path.join(self.music_folder, fname)
                display = os.path.splitext(fname)[0]  # Remove extension
                self.playlist.append((full_path, display))

    def has_tracks(self):
        return len(self.playlist) > 0

    def play(self):
        """Play or resume current track."""
        if not self.has_tracks():
            return
        if self.is_stopped or not self.is_playing:
            path, _ = self.playlist[self.current_index]
            try:
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
                self.is_playing = True
                self.is_stopped = False
            except pygame.error as e:
                print(f"Cannot play {path}: {e}")

    def stop(self):
        """Stop playback."""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_stopped = True

    def next_track(self):
        """Advance to next track and play it."""
        if not self.has_tracks():
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.stop()
        self.is_stopped = True
        self.play()

    def prev_track(self):
        """Go back to previous track and play it."""
        if not self.has_tracks():
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.stop()
        self.is_stopped = True
        self.play()

    def get_current_track_name(self):
        """Return display name of current track."""
        if not self.has_tracks():
            return "No tracks found"
        _, name = self.playlist[self.current_index]
        return name

    def get_status(self):
        """Return playback status string."""
        if not self.has_tracks():
            return "No tracks"
        if self.is_stopped:
            return "Stopped"
        if self.is_playing and pygame.mixer.music.get_busy():
            return "Playing"
        # Track finished naturally — auto advance
        self.next_track()
        return "Playing"

    def get_track_count(self):
        return len(self.playlist)

    def get_current_index(self):
        return self.current_index
