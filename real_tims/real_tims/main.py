# main.py
import pygame
from constants import WIDTH, HEIGHT
from screens.start_screen import start_screen
from screens.game_screen import game_screen
from screens.end_screen import end_screen
from screens.credits_screen import credits_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mario-Like Game")

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
        elif state == "exit":
            break

    pygame.quit()

if __name__ == "__main__":
    main()