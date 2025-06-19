import pygame
import os
from constants import WIDTH, HEIGHT
from player import Player
from enemy import Enemy

def game_screen(screen):
    clock = pygame.time.Clock()
    player = Player(100, 300)

    enemies = pygame.sprite.Group()
    enemy1 = Enemy(400, 500, 350, 600)
    enemies.add(enemy1)

    all_sprites = pygame.sprite.Group(player, enemy1)

    # Cargar imagen de fondo
    fondo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "fondo.png")
    fondo_image = pygame.image.load(fondo_path).convert()
    fondo_image = pygame.transform.scale(fondo_image, (WIDTH, HEIGHT))

    while True:
        # Dibujar fondo
        screen.blit(fondo_image, (0, 0))

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

        player.update(keys)
        enemies.update()

        all_sprites.draw(screen)

        # Colisiones con enemigos
        hits = pygame.sprite.spritecollide(player, enemies, False)
        for enemy in hits:
            if player.rect.bottom <= enemy.rect.top + 10:
                enemies.remove(enemy)
                all_sprites.remove(enemy)
                player.velocity_y = -15
            else:
                print("Muerto")

        pygame.display.flip()
        clock.tick(60)

        if player.rect.x > WIDTH:
            return "end"
