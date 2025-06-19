# screens/game_screen.py
import pygame
import os
from real_tims.constants import WIDTH, HEIGHT, WHITE
from real_tims.player import Player
from real_tims.enemy import Enemy

def game_screen(screen):
    clock = pygame.time.Clock()

    # Ruta segura al fondo
    base_path = os.path.dirname(__file__)
    fondo_path = os.path.abspath(os.path.join(base_path, "..", "assets", "mapa.png"))
    fondo = pygame.image.load(fondo_path).convert()

    # Jugador
    player = Player(100, 300)

    # Enemigos
    enemies = pygame.sprite.Group()
    enemy1 = Enemy(400, 500, 350, 600)
    enemies.add(enemy1)

    all_sprites = pygame.sprite.Group(player, enemy1)

    while True:
        screen.blit(fondo, (0, 0))  # dibuja fondo
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

        player.update(keys)
        enemies.update()

        all_sprites.draw(screen)

        # Colisiones
        hits = pygame.sprite.spritecollide(player, enemies, False)
        for enemy in hits:
            if player.rect.bottom <= enemy.rect.top + 10:
                enemies.remove(enemy)
                all_sprites.remove(enemy)
                player.velocity_y = -15
            else:
                return "death"

        pygame.display.flip()
        clock.tick(60)

        if player.rect.right >= WIDTH:
            return "end"
