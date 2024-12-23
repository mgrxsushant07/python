import pygame
import time
import datetime

# Initialize pygame mixer
pygame.mixer.init()

# Load your music file (make sure the path is correct)
pygame.mixer.music.load("musicplay.mp3")

# Play the music
pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Sleep to keep the program running and the music playing
