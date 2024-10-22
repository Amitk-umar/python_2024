import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize the Pygame mixer
pygame.mixer.init()

# Function to load and play a song
def load_song():
    song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Function to pause the music
def pause_song():
    pygame.mixer.music.pause()

# Function to resume the music
def resume_song():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_song():
    pygame.mixer.music.stop()

# Create the GUI window
root = tk.Tk()
root.title("Music Player")

# Load Song Button
load_button = tk.Button(root, text="Load Song", command=load_song)
load_button.pack()

# Play Button
play_button = tk.Button(root, text="Play", command=load_song)
play_button.pack()

# Pause Button
pause_button = tk.Button(root, text="Pause", command=pause_song)
pause_button.pack()

# Resume Button
resume_button = tk.Button(root, text="Resume", command=resume_song)
resume_button.pack()

# Stop Button
stop_button = tk.Button(root, text="Stop", command=stop_song)
stop_button.pack()

# Run the GUI loop
root.mainloop()