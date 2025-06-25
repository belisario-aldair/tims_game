import pygame
import os
from constants import WIDTH, HEIGHT, WHITE, BLACK

def start_screen(screen):
    clock = pygame.time.Clock()
    pygame.font.init()

    # Ruta corregida al archivo de fuente y fondo
    base_path = os.path.dirname(__file__)
    font_path = os.path.abspath(os.path.join(base_path, "..", "assets", "PressStart2P-Regular.ttf"))
    fondo_path = os.path.abspath(os.path.join(base_path, "..", "assets", "fondo.png"))

    # Cargar y escalar el fondo al tamaño de la pantalla
    fondo = pygame.image.load(fondo_path).convert()
    fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

    font_title = pygame.font.Font(font_path, 32)
    font_option = pygame.font.Font(font_path, 20)

    options = ["JUGAR", "CRÉDITOS", "SALIR"]
    selected = 0

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 100))

    while True:
        screen.blit(fondo, (0, 0))  # Mostrar fondo ajustado
        screen.blit(overlay, (0, 0))

        title_surface = font_title.render("JUEGO TESTING", True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        screen.blit(title_surface, title_rect)

        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else WHITE
            option_surface = font_option.render(option, True, color)
            option_rect = option_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40))
            screen.blit(option_surface, option_rect)

            if i == selected:
                arrow_surface = font_option.render("▶", True, color)
                arrow_rect = arrow_surface.get_rect(midright=(option_rect.left - 20, option_rect.centery))
                screen.blit(arrow_surface, arrow_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        return "game"
                    elif selected == 1:
                        return "credits"
                    elif selected == 2:
                        return "exit"

        clock.tick(60)
