# main.py
import pygame
from constants import WIDTH, HEIGHT
from screens.start_screen import start_screen
from screens.game_screen import game_screen
from screens.end_screen import end_screen
from screens.credits_screen import credits_screen
from screens.death_screen import death_screen
from screens.next_level_screen import next_level_screen

def main():
    lives = 3
    coins = 0
    start_time = None
    coin_group = None
    level = 1

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego TIMS")

    state = "start"
    while True:
        if state == "start":
            state = start_screen(screen)
        elif state == "game":
            result = game_screen(screen, lives, coins, start_time, coin_group,level)
            if isinstance(result, tuple):
                state, lives, coins, start_time, coin_group = result
            else:
                state = result
                if state == "death":
                    # Reiniciar valores si el jugador murió del todo
                    lives = 3
                    coins = 0
                    start_time = None
                    coin_group = None

        elif state == "end":
            level += 1
            if level > 3:
                state = "credits"
            else:
                next_level_screen(screen, f"Nivel 1-{level}")
                state = "game"
        elif state == "credits":
            state = credits_screen(screen)
        elif state == "death":
            state = death_screen(screen)
        elif state == "exit":
            break

    pygame.quit()

if __name__ == "__main__":
    main()
