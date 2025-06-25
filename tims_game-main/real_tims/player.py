# player.py
import pygame
import os
from constants import WIDTH

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "real_tims", "assets")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.load_images()
        self.state = "idle"
        self.direction = "right"
        self.image = self.images["idle_right"]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity_y = 0
        self.jump = False
        self.frame = 0
        self.frame_timer = 0

    def load_images(self):
        self.images = {
            "idle_right": self.load("mario_idle.png"),
            "idle_left": self.load("mario_idle_left.png"),
            "jump_right": self.load("mario_jump.png"),
            "jump_left": self.load("mario_jump_left.png"),
            "walk1_right": self.load("mario_walk1.png"),
            "walk2_right": self.load("mario_walk2.png"),
            "walk1_left": self.load("mario_walk1_left.png"),
            "walk2_left": self.load("mario_walk2_left.png")
        }

    def load(self, filename):
        path = os.path.join(ASSETS_DIR, filename)
        return pygame.transform.scale(pygame.image.load(path).convert_alpha(), (40, 60))

    def update(self, keys, blocks):
        dx = 0

        # Dirección
        if keys[pygame.K_LEFT]:
            dx = -5
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            dx = 5
            self.direction = "right"

        # Saltar
        if keys[pygame.K_SPACE] and not self.jump:
            self.velocity_y = -15
            self.jump = True

        # Gravedad
        self.velocity_y += 1
        dy = self.velocity_y

        # Movimiento horizontal
        self.rect.x += dx
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_hit_list:
            if dx > 0:
                self.rect.right = block.rect.left
            elif dx < 0:
                self.rect.left = block.rect.right

        # Movimiento vertical
        self.rect.y += dy
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False)
        for block in block_hit_list:
            if dy > 0:  # cayendo
                self.rect.bottom = block.rect.top
                self.velocity_y = 0
                self.jump = False
            elif dy < 0:  # saltando hacia arriba
                self.rect.top = block.rect.bottom
                self.velocity_y = 0
                if block.breakable:
                    blocks.remove(block)

        # Piso
        if self.rect.bottom >= 540:
            self.rect.bottom = 540
            self.jump = False
            self.velocity_y = 0

        # Estado
        if self.jump:
            self.state = "jump"
        elif dx != 0:
            self.state = "walk"
        else:
            self.state = "idle"

        self.animate()

    def animate(self):
        key = ""

        if self.state == "walk":
            self.frame_timer += 1
            if self.frame_timer >= 10:
                self.frame = (self.frame + 1) % 2  # 0 o 1
                self.frame_timer = 0
            key = f"walk{self.frame + 1}_{self.direction}"
        else:
            key = f"{self.state}_{self.direction}"

        self.image = self.images[key]
