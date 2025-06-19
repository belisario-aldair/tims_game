# enemy.py
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, min_x, max_x):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.min_x = min_x
        self.max_x = max_x
        self.speed = 2

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= self.min_x or self.rect.right >= self.max_x:
            self.speed *= -1
