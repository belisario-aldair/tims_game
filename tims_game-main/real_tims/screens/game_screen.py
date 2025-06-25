# screens/game_screen.py
import pygame
import os
from constants import WIDTH, HEIGHT, WHITE
from player import Player
from enemy import Enemy
from coin import Coin
from blocks import Block

def game_screen(screen, lives=3, coins=0, start_time=None, coin_group=None, level=1):
    font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 16)

    scroll_x = 0
    MAX_SCROLL = 1000  # ancho total del mapa menos WIDTH, puedes ajustar luego

    if start_time is None:
        start_time = pygame.time.get_ticks()

    # Jugador
    player = Player(100, 300)

    clock = pygame.time.Clock()

    # Ruta segura al fondo
    base_path = os.path.dirname(__file__)
    fondo_path = os.path.abspath(os.path.join(base_path, "..", "assets", "mapa.png"))
    fondo = pygame.image.load(fondo_path).convert()

    # Enemigos
    enemies = pygame.sprite.Group()
    enemy1 = Enemy(400, 500, 350, 600)
    enemies.add(enemy1)

    all_sprites = pygame.sprite.Group(player, enemy1)
    
    blocks = pygame.sprite.Group()
    blocks.add(Block(300, 400, breakable=False))
    blocks.add(Block(450, 400, breakable=True))
    
    if coin_group is None:
        coin_group = pygame.sprite.Group()
        coin_group.add(Coin(300, 500))
        coin_group.add(Coin(500, 500))
        coin_group.add(Coin(700, 500))

    all_sprites.add(coin_group)

    while True:
        screen.blit(fondo, (0, 0))  # dibuja fondo
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

        prev_x = player.rect.x
        player.update(keys, blocks)

        # Evita que Mario retroceda (no puede ir más allá del scroll actual)
        if player.rect.x < scroll_x:
            player.rect.x = scroll_x

        # Scroll hacia adelante si Mario avanza
        if player.rect.centerx - scroll_x > WIDTH // 2:
            scroll_x = player.rect.centerx - WIDTH // 2
            scroll_x = min(scroll_x, MAX_SCROLL)


        collected = pygame.sprite.spritecollide(player, coin_group, True)
        for coin in collected:
            coins += 1
            if coins >= 20:
                coins = 0
                lives += 1

        enemies.update()

        for sprite in all_sprites:
            screen.blit(sprite.image, (sprite.rect.x - scroll_x, sprite.rect.y))

        for block in blocks:
            screen.blit(block.image, (block.rect.x - scroll_x, block.rect.y))

        # Colisiones
        hits = pygame.sprite.spritecollide(player, enemies, False)
        for enemy in hits:
            if player.rect.bottom <= enemy.rect.top + 10:
                enemies.remove(enemy)
                all_sprites.remove(enemy)
                player.velocity_y = -15
            else:
                fall_animation(screen, player, fondo, scroll_x)
                lives -= 1
                if lives <= 0:
                    return "death"
                else:
                    return ("game", lives, coins, start_time, coin_group)

        
        # Tiempo
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = max(0, 100 - elapsed_time)
        if remaining_time <= 0:
            return "death"

        hud_color = (255, 255, 255)
        coin_text = font.render(f"Monedas: {coins}", True, hud_color)
        lives_text = font.render(f"Vidas: {lives}", True, hud_color)
        time_text = font.render(f"Tiempo: {remaining_time}", True, hud_color)

        screen.blit(coin_text, (20, 20))
        screen.blit(lives_text, (20, 50))
        screen.blit(time_text, (WIDTH - 200, 20))

        pygame.display.flip()
        clock.tick(60)

        if player.rect.right >= WIDTH:
            return "end"

def fall_animation(screen, player, fondo, scroll_x):
    for i in range(60):  # 1 segundo a 60 FPS
        screen.blit(fondo, (0, 0))
        for sprite in pygame.sprite.Group(player):
            player.rect.y += 5
            screen.blit(player.image, (player.rect.x - scroll_x, player.rect.y))
        pygame.display.flip()
        pygame.time.delay(16)

