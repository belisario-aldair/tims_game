# player.py
import pygame
from constants import BLUE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity_y = 0
        self.jump = False

    def update(self, keys):
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5
        if keys[pygame.K_SPACE] and not self.jump:
            self.velocity_y = -15
            self.jump = True

        self.velocity_y += 1
        dy = self.velocity_y

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom >= 540:
            self.rect.bottom = 540
            self.jump = False
