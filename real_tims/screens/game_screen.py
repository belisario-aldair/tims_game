# screens/game_screen.py
import pygame
from constants import WIDTH, HEIGHT, WHITE
from player import Player
from enemy import Enemy

def game_screen(screen):
    clock = pygame.time.Clock()
    player = Player(100, 300)

    enemies = pygame.sprite.Group()
    enemy1 = Enemy(400, 500, 350, 600)
    enemies.add(enemy1)

    all_sprites = pygame.sprite.Group(player, enemy1)

    while True:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

        player.update(keys)
        enemies.update()

        all_sprites.draw(screen)

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

        if player.rect.x > WIDTH:
            return "end"
