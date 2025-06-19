import pygame
import os

from real_tims.constants import WIDTH
#from real_tims.constants import WIDTH

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "real_tims", "assets")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        asset_path = os.path.join(ASSETS_DIR, "mario_idle.png")
        self.image = pygame.image.load(asset_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 60))
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

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom >= 540:
            self.rect.bottom = 540
            self.jump = False
