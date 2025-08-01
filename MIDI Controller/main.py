import pygame.midi
import pygame
import os.path
from sys import exit

# starts the game and initializes the mixer/music player, clock, and screen
pygame.init()
pygame.midi.init()
screen = pygame.display.set_mode((800,400))
mixer = pygame.mixer.init()
clock = pygame.time.Clock()

# list of all the notes, to be expanded
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sounds = {60: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.C4.aiff")),
          61: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.Db4.aiff")),
          62: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.D4.aiff")),
          63: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.Eb4.aiff")),
          64: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.E4.aiff")),
          65: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.F4.aiff")),
          66: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.Gb4.aiff")),
          67: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.G4.aiff")),
          68: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.Ab4.aiff")),
          69: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.A4.aiff")),
          70: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.Bb4.aiff")),
          71: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.B4.aiff")),
          72: pygame.mixer.Sound(os.path.join(BASE_DIR, "SFX", "Piano.mf.C5.aiff")),}

# setting up midi input
device_id = pygame.midi.get_default_input_id()
if device_id:
    midi_input = pygame.midi.Input(device_id)
else:
    print("Please connect a device before running this program")
    pygame.quit()
    exit()


while True:
    # quits the game, either with the X on the window or by pressing
    # escape and terminates the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting...")
            pygame.quit()
            exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            print("Quitting...")
            pygame.quit()
            exit()
    

    # play sounds from midi device
    if midi_input.poll():
        events = midi_input.read(10)
        for evt in events:
            data = evt[0]
            status, note, velocity, _ = data
            if status == 144 and velocity > 0:
                if 60 <= note <= 72:
                    sounds[note].play()
                else:
                    pass
            

    # updates display and unlocks framerate
    pygame.display.update()
    clock.tick()
    