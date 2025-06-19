import pygame
import os

SCALE_FACTOR = 2

def scale_image(img):
    width = img.get_width() * SCALE_FACTOR
    height = img.get_height() * SCALE_FACTOR
    return pygame.transform.scale(img, (width, height))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        assets_path = os.path.join(os.path.dirname(__file__), "assets")

        # Imágenes mirando a la derecha
        self.idle_image_right = scale_image(pygame.image.load(os.path.join(assets_path, "mario_idle.png")).convert_alpha())
        self.walk_images_right = [
            scale_image(pygame.image.load(os.path.join(assets_path, "mario_walk1.png")).convert_alpha()),
            scale_image(pygame.image.load(os.path.join(assets_path, "mario_walk2.png")).convert_alpha())
        ]
        self.jump_image_right = scale_image(pygame.image.load(os.path.join(assets_path, "mario_jump.png")).convert_alpha())

        # Imágenes mirando a la izquierda
        self.idle_image_left = scale_image(pygame.image.load(os.path.join(assets_path, "mario_idle_left.png")).convert_alpha())
        self.walk_images_left = [
            scale_image(pygame.image.load(os.path.join(assets_path, "mario_walk1_left.png")).convert_alpha()),
            scale_image(pygame.image.load(os.path.join(assets_path, "mario_walk2_left.png")).convert_alpha())
        ]
        self.jump_image_left = scale_image(pygame.image.load(os.path.join(assets_path, "mario_jump_left.png")).convert_alpha())

        # Imagen inicial y rectángulo
        self.image = self.idle_image_right
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Movimiento y animación
        self.velocity_y = 0
        self.jump = False
        self.facing_right = True
        self.walk_index = 0
        self.frame_counter = 0

    def update(self, keys):
        dx = 0

        # Movimiento horizontal y dirección
        if keys[pygame.K_LEFT]:
            dx = -5
            self.facing_right = False
        elif keys[pygame.K_RIGHT]:
            dx = 5
            self.facing_right = True

        # Iniciar salto (solo si no está en el aire)
        if keys[pygame.K_SPACE] and not self.jump:
            self.velocity_y = -15
            self.jump = True

        # Aplicar gravedad
        self.velocity_y += 1
        dy = self.velocity_y

        # Mover jugador
        self.rect.x += dx
        self.rect.y += dy

        # Colisión con suelo
        if self.rect.bottom >= 545:
            self.rect.bottom = 545
            self.jump = False

        # --- ACTUALIZAR LA IMAGEN SEGÚN ESTADO ---
        if self.jump:
            self.image = self.jump_image_right if self.facing_right else self.jump_image_left
        elif dx != 0:
            self._animate_walk()
        else:
            self.image = self.idle_image_right if self.facing_right else self.idle_image_left

    def _animate_walk(self):
        self.frame_counter += 1
        if self.frame_counter >= 10:
            self.frame_counter = 0
            self.walk_index = (self.walk_index + 1) % 2  # Hay 2 imágenes

        if self.facing_right:
            self.image = self.walk_images_right[self.walk_index]
        else:
            self.image = self.walk_images_left[self.walk_index]
