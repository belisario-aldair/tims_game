# screens/game_screen.py
import pygame
from constants import WIDTH, HEIGHT, WHITE
from player import Player

def game_screen(screen):
    clock = pygame.time.Clock()
    player = Player(100, 300)
    all_sprites = pygame.sprite.Group(player)

    while True:
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
        
        all_sprites.update(keys)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

        if player.rect.x > WIDTH:
            return "end"
