import pygame

# Inițializare pygame
pygame.init()

# Setări ecran
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Meniu cu Background Animat")

# Încărcare imagine background
bg = pygame.image.load("..\\resources\\map.png")
bg_width = bg.get_width()

# Încărcare sprite jucător
player_img = pygame.image.load("..\\resources\\player.png")  # Asigură-te că ai această imagine în folder!
player_img = pygame.transform.scale(player_img, (50, 50))  # Redimensionăm dacă e nevoie

# Coordonate pentru scrolling
x1 = 0
x2 = bg_width
speed = 2  # Viteza de mișcare a backgroundului

# Culori
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Font
font = pygame.font.Font(None, 50)

# Creare butoane
buttons = {
    "Start": pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 80, 200, 50),
    "Help": pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 50),
    "Quit": pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 80, 200, 50)
}

# Variabilă pentru a schimba între meniu și joc
in_game = False

# Funcție pentru desenarea textului pe butoane
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Funcție pentru meniul principal
def menu():
    global x1, x2, in_game

    running = True
    while running:
        screen.fill((0, 0, 0))  # Curățare ecran

        # Evenimente
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if buttons["Start"].collidepoint((mx, my)):
                    in_game = True
                    return  # Iese din funcția menu() și trece la joc
                if buttons["Help"].collidepoint((mx, my)):
                    print("Ajutor: Apasă Start pentru a începe, Quit pentru a ieși.")
                if buttons["Quit"].collidepoint((mx, my)):
                    running = False

        # Mișcarea backgroundului
        x1 -= speed
        x2 -= speed

        # Resetare poziție pentru loop
        if x1 <= -bg_width:
            x1 = bg_width
        if x2 <= -bg_width:
            x2 = bg_width

        # Desenare background
        screen.blit(bg, (x1, 0))
        screen.blit(bg, (x2, 0))

        # Desenare butoane
        for text, rect in buttons.items():
            pygame.draw.rect(screen, GRAY, rect)
            draw_text(text, font, WHITE, screen, rect.centerx, rect.centery)

        pygame.display.update()

# Funcție pentru joc
def game():
    global in_game
    player_x, player_y = WIDTH // 2, HEIGHT // 2  # Poziția inițială a jucătorului
    player_speed = 1

    running = True
    while running:
        screen.fill((0, 0, 0))  # Fundal negru pentru joc

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Înapoi la meniu cu ESC
                    in_game = False
                    return  # Revine la meniu

        # Controale pentru jucător
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Desenare jucător (sprite)
        screen.blit(player_img, (player_x, player_y))

        pygame.display.update()

# Loop principal care schimbă între meniu și joc
while True:
    if in_game:
        game()
    else:
        menu()
