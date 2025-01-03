# Nowy dźwięk po wygranej
win_sound = pygame.mixer.Sound('winsound.mp3')
win_sound.set_volume(20)
 
# OBRAZY
try:
    menu = pygame.image.load("MENU.png").convert_alpha()
    menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))
    plansza = pygame.image.load("PLANSZA.png").convert_alpha()
    plansza = pygame.transform.scale(plansza, (SCREEN_WIDTH, SCREEN_HEIGHT))
    krzyzyk = pygame.image.load("KRZYŻYK.png").convert_alpha()
    krzyzyk = pygame.transform.scale(krzyzyk, (250, 250))
    kolko = pygame.image.load("KÓŁKO.png").convert_alpha()
    kolko = pygame.transform.scale(kolko, (250, 250))
    pierwszy = pygame.image.load("PIERWSZY.png").convert_alpha()
    pierwszy = pygame.transform.scale(pierwszy, (SCREEN_WIDTH, SCREEN_HEIGHT))
    drugi = pygame.image.load("DRUGI.png").convert_alpha()
    drugi = pygame.transform.scale(drugi, (SCREEN_WIDTH, SCREEN_HEIGHT))
    komputer = pygame.image.load("KOMPUTER.png").convert_alpha()
    komputer = pygame.transform.scale(komputer, (SCREEN_WIDTH, SCREEN_HEIGHT))
    remis_img = pygame.image.load("REMIS.png").convert_alpha()
    remis_img = pygame.transform.scale(remis_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except Exception as e:
    print(f"Wczytanie obrazu nie powiodło się :(: {e}")
    pygame.quit()
    sys.exit()
