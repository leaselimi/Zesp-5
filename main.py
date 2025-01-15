import pygame
import sys
import random
from Gra.py import *
from pics_sounds.py import *

pygame.init()
pygame.mixer.init()

# Rozdzielczość okna gry
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

# Ikona okna i tytuł
icon = pygame.image.load('KRZYŻYK.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("ULTIMATE TIC-TAC-TOE")

# --- czcionka / kolory ---
czcionka1 = pygame.font.SysFont(None, 35)
WHITE = (255, 255, 255)



# Zbiór wszystkich stref małych pól
strefy_small = {
    's1p1': s1p1, 's1p2': s1p2, 's1p3': s1p3,
    's1p4': s1p4, 's1p5': s1p5, 's1p6': s1p6,
    's1p7': s1p7, 's1p8': s1p8, 's1p9': s1p9,

    's2p1': s2p1, 's2p2': s2p2, 's2p3': s2p3,
    's2p4': s2p4, 's2p5': s2p5, 's2p6': s2p6,
    's2p7': s2p7, 's2p8': s2p8, 's2p9': s2p9,

    's3p1': s3p1, 's3p2': s3p2, 's3p3': s3p3,
    's3p4': s3p4, 's3p5': s3p5, 's3p6': s3p6,
    's3p7': s3p7, 's3p8': s3p8, 's3p9': s3p9,

    's4p1': s4p1, 's4p2': s4p2, 's4p3': s4p3,
    's4p4': s4p4, 's4p5': s4p5, 's4p6': s4p6,
    's4p7': s4p7, 's4p8': s4p8, 's4p9': s4p9,

    's5p1': s5p1, 's5p2': s5p2, 's5p3': s5p3,
    's5p4': s5p4, 's5p5': s5p5, 's5p6': s5p6,
    's5p7': s5p7, 's5p8': s5p8, 's5p9': s5p9,

    's6p1': s6p1, 's6p2': s6p2, 's6p3': s6p3,
    's6p4': s6p4, 's6p5': s6p5, 's6p6': s6p6,
    's6p7': s6p7, 's6p8': s6p8, 's6p9': s6p9,

    's7p1': s7p1, 's7p2': s7p2, 's7p3': s7p3,
    's7p4': s7p4, 's7p5': s7p5, 's7p6': s7p6,
    's7p7': s7p7, 's7p8': s7p8, 's7p9': s7p9,

    's8p1': s8p1, 's8p2': s8p2, 's8p3': s8p3,
    's8p4': s8p4, 's8p5': s8p5, 's8p6': s8p6,
    's8p7': s8p7, 's8p8': s8p8, 's8p9': s8p9,

    's9p1': s9p1, 's9p2': s9p2, 's9p3': s9p3,
    's9p4': s9p4, 's9p5': s9p5, 's9p6': s9p6,
    's9p7': s9p7, 's9p8': s9p8, 's9p9': s9p9,
}

# Pozycje X/O wewnątrz pól (przesunięcie obrazka o kilka pikseli)
positions_small = {}
for key, rect in strefy_small.items():
    positions_small[key] = (rect.x + 5, rect.y + 5)

# Stan gry w 81 polach -> "X", "O" lub None
plansza_ultimate = {k: None for k in strefy_small}
