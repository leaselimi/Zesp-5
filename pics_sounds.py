import pygame
import sys

# Rozdzielczość okna gry
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)

# OBRAZY
try:
    menu = pygame.image.load("MENU.png").convert_alpha()
    menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
    plansza = pygame.image.load("BOARD.png").convert_alpha()
    plansza = pygame.transform.scale(plansza, (SCREEN_WIDTH, SCREEN_HEIGHT))
    krzyzyk = pygame.image.load("KRZYŻYK.png").convert_alpha()
    krzyzyk = pygame.transform.scale(krzyzyk, (65, 65))
    kolko = pygame.image.load("KÓŁKO.png").convert_alpha()
    kolko = pygame.transform.scale(kolko, (65, 65))
    pierwszy = pygame.image.load("KRZYŻYK_WIN.png").convert_alpha()
    pierwszy = pygame.transform.scale(pierwszy, (SCREEN_WIDTH, SCREEN_HEIGHT))
    drugi = pygame.image.load("KÓŁKO_WIN.png").convert_alpha()
    drugi = pygame.transform.scale(drugi, (SCREEN_WIDTH, SCREEN_HEIGHT))
    komputer = pygame.image.load("KÓŁKO_WIN.png").convert_alpha()
    komputer = pygame.transform.scale(komputer, (SCREEN_WIDTH, SCREEN_HEIGHT))
    remis_img = pygame.image.load("REMIS.png").convert_alpha()
    remis_img = pygame.transform.scale(remis_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except Exception as e:
    print(f"Wczytanie obrazu nie powiodło się :(: {e}")
    pygame.quit()
    sys.exit()
