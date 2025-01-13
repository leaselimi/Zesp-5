import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load('KRZYŻYK.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("ULTIMATE TIC-TAC-TOE")

#dodac muzyke


try:
    menu = pygame.image.load("MENU.png").convert_alpha()
    menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

    plansza = pygame.image.load("BOARD.png").convert_alpha()
    plansza = pygame.transform.scale(plansza, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Małe iksy i kółka (na pojedyncze pola)
    krzyzyk = pygame.image.load("KRZYŻYK.png").convert_alpha()
    krzyzyk = pygame.transform.scale(krzyzyk, (65, 65))

    kolko = pygame.image.load("KÓŁKO.png").convert_alpha()
    kolko = pygame.transform.scale(kolko, (65, 65))

    gracz = pygame.image.load("KÓŁKO_WIN.png").convert_alpha()
    gracz = pygame.transform.scale(gracz, (SCREEN_WIDTH, SCREEN_HEIGHT))

    komputer = pygame.image.load("KÓŁKO_WIN.png").convert_alpha()
    komputer = pygame.transform.scale(komputer, (SCREEN_WIDTH, SCREEN_HEIGHT))

    remis_img = pygame.image.load("DRAW.png").convert_alpha()
    remis_img = pygame.transform.scale(remis_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

except Exception as e:
    print(f"Wczytanie obrazu nie powiodło się :(: {e}")
    pygame.quit()
    sys.exit()
    
#fonty
font_path = 'czcionka.ttf'
font1 = pygame.font.SysFont(None, 35)
WHITE = (255, 255, 255)

#przyciskowe strefy menu
graj_prostokat = pygame.prostokat(253, 270, 390, 100)
pc_play_prostokat = pygame.prostokat(253, 436, 390, 100)
quit_prostokat = pygame.prostokat(253, 591, 390, 100)

---------------------------
STREFY POSZCZEGÓLNYCH PÓL
---------------------------
Sub-plansza 1 (górny-lewy róg)
Sub-plansza 1: 3 kolumny i 3 wiersze.
# ---------------------------
# STREFY POSZCZEGÓLNYCH PÓL
# ---------------------------

# Sub-plansza 1
s1p1 = pygame.Rect(57, 47, 65, 65)
s1p2 = pygame.Rect(127, 47, 65, 65)
s1p3 = pygame.Rect(197, 47, 65, 65)
s1p4 = pygame.Rect(57, 119, 65, 65)
s1p5 = pygame.Rect(127, 119, 65, 65)
s1p6 = pygame.Rect(197, 119, 65, 65)
s1p7 = pygame.Rect(57, 193, 65, 65)
s1p8 = pygame.Rect(127, 193, 65, 65)
s1p9 = pygame.Rect(197, 193, 65, 65)

# Sub-plansza 2
s2p1 = pygame.Rect(350, 47, 65, 65)
s2p2 = pygame.Rect(422, 47, 65, 65)
s2p3 = pygame.Rect(493, 47, 65, 65)
s2p4 = pygame.Rect(350, 119, 65, 65)
s2p5 = pygame.Rect(422, 119, 65, 65)
s2p6 = pygame.Rect(493, 119, 65, 65)
s2p7 = pygame.Rect(350, 193, 65, 65)
s2p8 = pygame.Rect(422, 193, 65, 65)
s2p9 = pygame.Rect(493, 193, 65, 65)

# Sub-plansza 3
s3p1 = pygame.Rect(635, 47, 65, 65)
s3p2 = pygame.Rect(705, 47, 65, 65)
s3p3 = pygame.Rect(777, 47, 65, 65)
s3p4 = pygame.Rect(635, 119, 65, 65)
s3p5 = pygame.Rect(705, 119, 65, 65)
s3p6 = pygame.Rect(777, 119, 65, 65)
s3p7 = pygame.Rect(635, 193, 65, 65)
s3p8 = pygame.Rect(705, 193, 65, 65)
s3p9 = pygame.Rect(777, 193, 65, 65)

# Sub-plansza 4
s4p1 = pygame.Rect(57, 337, 65, 65)
s4p2 = pygame.Rect(127, 337, 65, 65)
s4p3 = pygame.Rect(197, 337, 65, 65)
s4p4 = pygame.Rect(57, 408, 65, 65)
s4p5 = pygame.Rect(127, 408, 65, 65)
s4p6 = pygame.Rect(197, 408, 65, 65)
s4p7 = pygame.Rect(57, 485, 65, 65)
s4p8 = pygame.Rect(127, 485, 65, 65)
s4p9 = pygame.Rect(197, 485, 65, 65)

# Sub-plansza 5
s5p1 = pygame.Rect(350, 337, 65, 65)
s5p2 = pygame.Rect(422, 337, 65, 65)
s5p3 = pygame.Rect(493, 337, 65, 65)
s5p4 = pygame.Rect(350, 408, 65, 65)
s5p5 = pygame.Rect(422, 408, 65, 65)
s5p6 = pygame.Rect(493, 408, 65, 65)
s5p7 = pygame.Rect(350, 485, 65, 65)
s5p8 = pygame.Rect(422, 485, 65, 65)
s5p9 = pygame.Rect(493, 485, 65, 65)

# Sub-plansza 6
s6p1 = pygame.Rect(635, 337, 65, 65)
s6p2 = pygame.Rect(705, 337, 65, 65)
s6p3 = pygame.Rect(777, 337, 65, 65)
s6p4 = pygame.Rect(635, 408, 65, 65)
s6p5 = pygame.Rect(705, 408, 65, 65)
s6p6 = pygame.Rect(777, 408, 65, 65)
s6p7 = pygame.Rect(635, 485, 65, 65)
s6p8 = pygame.Rect(705, 485, 65, 65)
s6p9 = pygame.Rect(777, 485, 65, 65)

# Sub-plansza 7
s7p1 = pygame.Rect(57, 627, 65, 65)
s7p2 = pygame.Rect(127, 627, 65, 65)
s7p3 = pygame.Rect(197, 627, 65, 65)
s7p4 = pygame.Rect(57, 700, 65, 65)
s7p5 = pygame.Rect(127, 700, 65, 65)
s7p6 = pygame.Rect(197, 700, 65, 65)
s7p7 = pygame.Rect(57, 777, 65, 65)
s7p8 = pygame.Rect(127, 777, 65, 65)
s7p9 = pygame.Rect(197, 777, 65, 65)

# Sub-plansza 8
s8p1 = pygame.Rect(350, 627, 65, 65)
s8p2 = pygame.Rect(422, 627, 65, 65)
s8p3 = pygame.Rect(493, 627, 65, 65)
s8p4 = pygame.Rect(350, 700, 65, 65)
s8p5 = pygame.Rect(422, 700, 65, 65)
s8p6 = pygame.Rect(493, 700, 65, 65)
s8p7 = pygame.Rect(350, 777, 65, 65)
s8p8 = pygame.Rect(422, 777, 65, 65)
s8p9 = pygame.Rect(493, 777, 65, 65)

# Sub-plansza 9
s9p1 = pygame.Rect(635, 627, 65, 65)
s9p2 = pygame.Rect(705, 627, 65, 65)
s9p3 = pygame.Rect(777, 627, 65, 65)
s9p4 = pygame.Rect(635, 700, 65, 65)
s9p5 = pygame.Rect(705, 700, 65, 65)
s9p6 = pygame.Rect(777, 700, 65, 65)
s9p7 = pygame.Rect(635, 777, 65, 65)
s9p8 = pygame.Rect(705, 777, 65, 65)
s9p9 = pygame.Rect(777, 777, 65, 65)
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

# Pozycje X/O wewnątrz pól
positions_small = {}
for key, prostokat in strefy_small.items():
    positions_small[key] = (prostokat.x + 5, prostokat.y + 5)

# Stan gry w 81 polach
plansza_ultimate = {k: None for k in strefy_small}  # "X", "O" lub None

# Mapowanie: sub-plansza (1..9), pole (1..9)
mapowanie_sub = {
    's1p1': (1,1), 's1p2': (1,2), 's1p3': (1,3),
    's1p4': (1,4), 's1p5': (1,5), 's1p6': (1,6),
    's1p7': (1,7), 's1p8': (1,8), 's1p9': (1,9),

    's2p1': (2,1), 's2p2': (2,2), 's2p3': (2,3),
    's2p4': (2,4), 's2p5': (2,5), 's2p6': (2,6),
    's2p7': (2,7), 's2p8': (2,8), 's2p9': (2,9),

    's3p1': (3,1), 's3p2': (3,2), 's3p3': (3,3),
    's3p4': (3,4), 's3p5': (3,5), 's3p6': (3,6),
    's3p7': (3,7), 's3p8': (3,8), 's3p9': (3,9),

    's4p1': (4,1), 's4p2': (4,2), 's4p3': (4,3),
    's4p4': (4,4), 's4p5': (4,5), 's4p6': (4,6),
    's4p7': (4,7), 's4p8': (4,8), 's4p9': (4,9),

    's5p1': (5,1), 's5p2': (5,2), 's5p3': (5,3),
    's5p4': (5,4), 's5p5': (5,5), 's5p6': (5,6),
    's5p7': (5,7), 's5p8': (5,8), 's5p9': (5,9),

    's6p1': (6,1), 's6p2': (6,2), 's6p3': (6,3),
    's6p4': (6,4), 's6p5': (6,5), 's6p6': (6,6),
    's6p7': (6,7), 's6p8': (6,8), 's6p9': (6,9),

    's7p1': (7,1), 's7p2': (7,2), 's7p3': (7,3),
    's7p4': (7,4), 's7p5': (7,5), 's7p6': (7,6),
    's7p7': (7,7), 's7p8': (7,8), 's7p9': (7,9),

    's8p1': (8,1), 's8p2': (8,2), 's8p3': (8,3),
    's8p4': (8,4), 's8p5': (8,5), 's8p6': (8,6),
    's8p7': (8,7), 's8p8': (8,8), 's8p9': (8,9),

    's9p1': (9,1), 's9p2': (9,2), 's9p3': (9,3),
    's9p4': (9,4), 's9p5': (9,5), 's9p6': (9,6),
    's9p7': (9,7), 's9p8': (9,8), 's9p9': (9,9),
}
Duże X/O (pokrywające całą sub-planszę 300×300)
big_krzyzyk = pygame.transform.scale(krzyzyk, (300, 300))
big_kolko = pygame.transform.scale(kolko, (300, 300))

Współrzędne pikselowe dla górnego-lewego rogu każdej z 9 sub-plansz.
Sub-plansze rozmieszczone są w siatce 3x3 na głównej planszy.
sub_positions = {
    1: (0,0),   2: (300,0),   3: (600,0),
    4: (0,300), 5: (300,300), 6: (600,300),
    7: (0,600), 8: (300,600), 9: (600,600),
}

Kombinacje zwycięstwa na mini-planszy 3x3 (poziome, pionowe, ukośne).
warunki_zwyciestwa_subplanszy = [
    (1,2,3), (4,5,6), (7,8,9),
    (1,4,7), (2,5,8), (3,6,9),
    (1,5,9), (3,5,7)
]

Słownik przechowujący zwycięzcę dla każdej z 9 sub-plansz.
Klucze (1-9) odpowiadają numerom sub-plansz, a wartości to:
None (brak zwycięzcy),
"X" (gracz X wygrał sub-planszę),
"O" (gracz O wygrał sub-planszę)
zwycięzcy_sub_plansz = {i: None for i in range(1,10)}

Warunki zwycięstwa na dużej planszy (3×3 sub-plansz)
warunki_zwyciestwa_duzej_planszy = [
    (1,2,3), (4,5,6), (7,8,9),
    (1,4,7), (2,5,8), (3,6,9),
    (1,5,9), (3,5,7)
]

--- Strefy końcowe (Rematch / Quit) ---
rematch1 = pygame.prostokat(90, 734, 268, 70)
quit1 = pygame.prostokat(515, 734, 268, 70)
rematch2 = pygame.prostokat(320, 680, 260, 65)
quit2 = pygame.prostokat(320, 789, 260, 65)
rematch_pc = pygame.prostokat(322, 694, 200, 56)
quit_pc = pygame.prostokat(322, 786, 200, 70)
rematch_remis = pygame.prostokat(360, 785, 187, 52)

--- Inicjalizacja gry ---
obecny_ekran = "menu"
game_over = False
winner = None
win_sound_played = False
tura: numer tury (0 dla X, 1 dla O, itd.)
tura = 0
aktualny_tekst = "TURA GRACZA 1"

działanie_gry = True
