# screens/end_screen.py
import pygame
from constants import WIDTH, HEIGHT, WHITE, BLACK

def end_screen(screen):
    font = pygame.font.SysFont(None, 48)
    msg = font.render("¡Felicidades! Nivel completado", True, BLACK)
    info = font.render("Presiona ESC para salir", True, BLACK)
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        screen.blit(msg, (WIDTH // 2 - 250, HEIGHT // 2 - 100))
        screen.blit(info, (WIDTH // 2 - 200, HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return "exit"

        clock.tick(60)
