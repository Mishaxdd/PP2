import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.index = 0
        self.is_playing = False

        pygame.mixer.init()

    def load_music(self):
        files = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                files.append(os.path.join(self.music_folder, file))
        files.sort()
        return files

    def load_track(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.index])

    def play(self):
        if not self.playlist:
            return

        if not self.is_playing:
            self.load_track()
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return

        self.index = (self.index + 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()

    def previous_track(self):
        if not self.playlist:
            return

        self.index = (self.index - 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()

    def get_current_track(self):
        if not self.playlist:
            return "No music found"
        return os.path.basename(self.playlist[self.index])