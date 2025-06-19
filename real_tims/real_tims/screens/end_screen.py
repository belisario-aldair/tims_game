import pygame
from constants import WIDTH, HEIGHT, WHITE

def end_screen(screen):
    clock = pygame.time.Clock()
    pygame.font.init()

    font_path = "assets/PressStart2P-Regular.ttf"
    font_title = pygame.font.Font(font_path, 28)
    font_info = pygame.font.Font(font_path, 16)

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))

    while True:
        screen.blit(overlay, (0, 0))

        msg = "¡FELICIDADES!"
        msg2 = "NIVEL COMPLETADO"

        msg_surface = font_title.render(msg, True, WHITE)
        msg2_surface = font_title.render(msg2, True, WHITE)
        msg_rect = msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
        msg2_rect = msg2_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))

        screen.blit(msg_surface, msg_rect)
        screen.blit(msg2_surface, msg2_rect)

        info_surface = font_info.render("Presiona ESC para salir", True, WHITE)
        info_rect = info_surface.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        screen.blit(info_surface, info_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "exit"

        clock.tick(60)