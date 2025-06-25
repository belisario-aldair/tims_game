import pygame
import os
from constants import WIDTH, HEIGHT, WHITE

def credits_screen(screen):
    clock = pygame.time.Clock()
    pygame.font.init()

    # Carga segura de la fuente
    base_path = os.path.dirname(__file__)
    font_path = os.path.abspath(os.path.join(base_path, "..", "assets", "PressStart2P-Regular.ttf"))

    font_title = pygame.font.Font(font_path, 28)
    font_names = pygame.font.Font(font_path, 16)
    exit_font = pygame.font.Font(font_path, 14)

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # Más opaco

    developers = [
        "Apaza Mamani Anhely",
        "Belisario Fernandez Aldair",
        "Ccuno Cuno Kris",
        "Pilco Quispe Jhon"
    ]

    while True:
        screen.blit(overlay, (0, 0))

        # Título
        title_surface = font_title.render("CRÉDITOS", True, WHITE)
        title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 120))
        screen.blit(title_surface, title_rect)

        # Nombres
        for i, name in enumerate(developers):
            name_surface = font_names.render(name, True, WHITE)
            name_rect = name_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40 + i * 30))
            screen.blit(name_surface, name_rect)

        # Instrucción para salir
        exit_surface = exit_font.render("Presiona ESC para volver", True, WHITE)
        exit_rect = exit_surface.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        screen.blit(exit_surface, exit_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "start"

        clock.tick(60)
