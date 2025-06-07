import pygame

def load_image(path):
    try:
        image = pygame.image.load(path)
        return image
    except pygame.error as e:
        print(f"Error cargando la imagen: {path} - {e}")
        return None

def load_sound(path):
    try:
        sound = pygame.mixer.Sound(path)
        return sound
    except pygame.error as e:
        print(f"Error cargando el sonido: {path} - {e}")
        return None
