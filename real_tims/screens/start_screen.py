# screens/start_screen.py
import pygame
from constants import WIDTH, HEIGHT, WHITE, BLACK

def start_screen(screen):
    font = pygame.font.SysFont(None, 48)
    title = font.render("MARIO-LIKE GAME", True, BLACK)
    info = font.render("Presiona ESPACIO para comenzar", True, BLACK)
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        screen.blit(title, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
        screen.blit(info, (WIDTH // 2 - 250, HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "game"

        clock.tick(60)
