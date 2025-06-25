# screens/next_level_screen.py
import pygame
from constants import WIDTH, HEIGHT

def next_level_screen(screen, level_text):
    font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 24)
    screen.fill((0, 0, 0))
    text = font.render(level_text, True, (255, 255, 255))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.delay(2000)  # Espera 2 segundos
