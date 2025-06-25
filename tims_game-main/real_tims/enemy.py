import pygame
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "real_tims", "assets")

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, min_x, max_x):
        super().__init__()
        asset_path = os.path.join(ASSETS_DIR, "enemigo.png")
        self.image = pygame.image.load(asset_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.min_x = min_x
        self.max_x = max_x
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= self.min_x or self.rect.right >= self.max_x:
            self.speed *= -1
