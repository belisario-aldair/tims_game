import pygame
import sys

pygame.init()

# Pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jugador Animado - 4 Direcciones")

# Cargar spritesheet
sprite_sheet = pygame.image.load("sprites/player.png").convert_alpha()

# Constantes
FRAME_WIDTH = 32
FRAME_HEIGHT = 32
FRAMES_PER_DIR = 4
NUM_DIRECTIONS = 4
ANIMATION_SPEED = 150  # milisegundos por frame

# Extraer todos los frames en una matriz [dirección][frame]
frames = []
SCALE_FACTOR = 2  # Agrandar al doble (64x64)
for row in range(NUM_DIRECTIONS):  # dirección
    dir_frames = []
    for col in range(FRAMES_PER_DIR):  # animación
        frame = sprite_sheet.subsurface(
            pygame.Rect(col * FRAME_WIDTH, row * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT)
        )
        scaled_frame = pygame.transform.scale(frame, (FRAME_WIDTH * SCALE_FACTOR, FRAME_HEIGHT * SCALE_FACTOR))
        dir_frames.append(scaled_frame)
    frames.append(dir_frames)

# Posición y control
player_rect = frames[0][0].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
direction = 0  # 0: abajo, 1: izquierda, 2: arriba, 3: derecha
frame_index = 0
animation_timer = 0
speed = 3

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_DOWN]:
        direction = 0
        player_rect.y += speed
        moving = True
    elif keys[pygame.K_LEFT]:
        direction = 1
        player_rect.x -= speed
        moving = True
    elif keys[pygame.K_UP]:
        direction = 2
        player_rect.y -= speed
        moving = True
    elif keys[pygame.K_RIGHT]:
        direction = 3
        player_rect.x += speed
        moving = True

    # Animación
    if moving:
        animation_timer += dt
        if animation_timer >= ANIMATION_SPEED:
            animation_timer = 0
            frame_index = (frame_index + 1) % FRAMES_PER_DIR
    else:
        frame_index = 0  # quieto

    # Dibujar
    screen.blit(frames[direction][frame_index], player_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
