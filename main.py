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

# Duże X/O (pokrywające całą sub-planszę 300×300)
big_krzyzyk = pygame.transform.scale(krzyzyk, (300, 300))
big_kolko = pygame.transform.scale(kolko, (300, 300))

# Kwadrat na wynik TIE (jeżeli chcesz wypełnić sub-planszę np. czarnym kolorem)
black_square = pygame.Surface((300,300))
black_square.fill((0,0,0))

# Położenia 9 sub-plansz w pikselach
sub_positions = {
    1: (0,0),   2: (300,0),   3: (600,0),
    4: (0,300), 5: (300,300), 6: (600,300),
    7: (0,600), 8: (300,600), 9: (600,600),
}

# Warunki zwycięstwa w mini-planszy (3×3)
warunki_zwyciestwa_subplanszy = [
    (1,2,3), (4,5,6), (7,8,9),
    (1,4,7), (2,5,8), (3,6,9),
    (1,5,9), (3,5,7)
]

# Zwycięzcy sub-plansz (None, "X", "O" lub "TIE")
zwycięzcy_sub_plansz = {i: None for i in range(1,10)}

# Warunki zwycięstwa na dużej planszy (3×3 sub-plansz)
warunki_zwyciestwa_duzej_planszy = [
    (1,2,3), (4,5,6), (7,8,9),
    (1,4,7), (2,5,8), (3,6,9),
    (1,5,9), (3,5,7)
]

# --- Strefy końcowe (Rematch / Quit) ---
rematch1 = pygame.Rect(90, 734, 268, 70)
quit1 = pygame.Rect(515, 734, 268, 70)
rematch2 = pygame.Rect(320, 680, 260, 65)
quit2 = pygame.Rect(320, 789, 260, 65)
rematch_pc = pygame.Rect(322, 694, 200, 56)
quit_pc = pygame.Rect(322, 786, 200, 70)
rematch_remis = pygame.Rect(360, 785, 187, 52)

# --- Inicjalizacja gry ---
obecny_ekran = "menu"
game_over = False
winner = None
win_sound_played = False
tura = 0  # 0 = X, 1 = O, 2 = X, ...
aktualny_tekst = "TURA GRACZA 1"

# Funkcja sprawdzająca, czy sub-plansza jest pełna (a nie ma w niej zwycięzcy).
def sprawdz_remis_w_subplanszy(sub_idx: int):
    """
    Sprawdza, czy sub-plansza sub_idx jest już pełna
    i nie ma zwycięzcy.
    Jeśli tak, zwraca True.
    """
    if zwycięzcy_sub_plansz[sub_idx] is not None:
        return False

    licznik = 0
    for klucz_pola in plansza_ultimate:
        si, ci = mapowanie_sub[klucz_pola]
        if si == sub_idx and plansza_ultimate[klucz_pola] is not None:
            licznik += 1

    return (licznik == 9)

działanie_gry = True
aktualna_subplansza = None
while działanie_gry:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            działanie_gry = False

        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                działanie_gry = False

        elif zdarzenie.type == pygame.MOUSEBUTTONDOWN:
            pozycja_myszki = pygame.mouse.get_pos()

            # ----------------
            # EKRAN MENU
            # ----------------
            if obecny_ekran == "menu":
                if graj_prostokat.collidepoint(pozycja_myszki):
                    obecny_ekran = "plansza"
                    plansza_ultimate = {k: None for k in plansza_ultimate}
                    zwycięzcy_sub_plansz = {i: None for i in range(1,10)}
                    tura = 0
                    game_over = False
                    winner = None
                    win_sound_played = False
                    aktualny_tekst = "TURA GRACZA 1"
                    aktualna_subplansza = None

                elif pc_play_prostokat.collidepoint(pozycja_myszki):
                    obecny_ekran = "plansza2"
                    plansza_ultimate = {k: None for k in plansza_ultimate}
                    zwycięzcy_sub_plansz = {i: None for i in range(1,10)}
                    tura = 0
                    game_over = False
                    winner = None
                    win_sound_played = False
                    aktualny_tekst = "TWOJA TURA"
                    aktualna_subplansza = None

                elif quit_prostokat.collidepoint(pozycja_myszki):
                    działanie_gry = False
                    z
