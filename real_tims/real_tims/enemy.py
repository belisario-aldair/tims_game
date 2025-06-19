import pygame
import os

SCALE = 2  # Ajusta según el tamaño que desees

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, min_x, max_x):
        super().__init__()

        # Ruta a la imagen
        image_path = os.path.join(os.path.dirname(__file__), "assets", "enemigo.png")
        image = pygame.image.load(image_path).convert_alpha()

        # Escalar la imagen
        width = image.get_width() * SCALE
        height = image.get_height() * SCALE
        self.image = pygame.transform.scale(image, (width, height))

        # Posición y movimiento
        self.rect = self.image.get_rect(topleft=(x, y))
        self.min_x = min_x
        self.max_x = max_x
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= self.min_x or self.rect.right >= self.max_x:
            self.speed *= -1
