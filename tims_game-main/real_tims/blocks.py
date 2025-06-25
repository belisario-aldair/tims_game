# blocks.py
import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, breakable=True):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamaño del bloque
        self.image.fill((150, 75, 0) if breakable else (100, 100, 100))  # Color según tipo
        self.rect = self.image.get_rect(topleft=(x, y))
        self.breakable = breakable
