# screens/death_screen.py
import pygame
import os
from real_tims.constants import WIDTH, HEIGHT, WHITE

def death_screen(screen):
    clock = pygame.time.Clock()
    pygame.font.init()

    # Ruta absoluta a la fuente
    base_path = os.path.dirname(__file__)
    font_path = os.path.abspath(os.path.join(base_path, "..", "assets", "PressStart2P-Regular.ttf"))

    font_title = pygame.font.Font(font_path, 28)
    font_info = pygame.font.Font(font_path, 16)

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))

    while True:
        screen.blit(overlay, (0, 0))

        msg = "Has muerto..."
        msg2 = "No te rindas"

        msg_surface = font_title.render(msg, True, WHITE)
        msg2_surface = font_title.render(msg2, True, WHITE)
        msg_rect = msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
        msg2_rect = msg2_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))

        screen.blit(msg_surface, msg_rect)
        screen.blit(msg2_surface, msg2_rect)

        info_surface1 = font_info.render("Presiona R para reiniciar", True, WHITE)
        info_surface2 = font_info.render("Presiona ESC para salir", True, WHITE)
        info_rect1 = info_surface1.get_rect(center=(WIDTH // 2, HEIGHT - 80))
        info_rect2 = info_surface2.get_rect(center=(WIDTH // 2, HEIGHT - 50))

        screen.blit(info_surface1, info_rect1)
        screen.blit(info_surface2, info_rect2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "exit"
                elif event.key == pygame.K_r:
                    return "game"

        clock.tick(60)
