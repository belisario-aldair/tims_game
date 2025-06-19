# main.py
import pygame
from real_tims.constants import WIDTH, HEIGHT
from real_tims.screens.start_screen import start_screen
from real_tims.screens.game_screen import game_screen
from real_tims.screens.end_screen import end_screen
from real_tims.screens.credits_screen import credits_screen
from real_tims.screens.death_screen import death_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego TIMS")

    state = "start"
    while True:
        if state == "start":
            state = start_screen(screen)
        elif state == "game":
            state = game_screen(screen)
        elif state == "end":
            state = end_screen(screen)
        elif state == "credits":
            state = credits_screen(screen)
        elif state == "death":
            state = death_screen(screen)
        elif state == "exit":
            break

    pygame.quit()

if __name__ == "__main__":
    main()
