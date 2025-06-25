import sys
import os
import pygame
import pytest
from unittest import mock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from real_tims.player import Player
from real_tims.constants import WIDTH

pygame.init()
pygame.display.set_mode((1, 1))

# Fixture para mockear la carga de imagen del jugador
@pytest.fixture(autouse=True)
def mock_pygame_image(monkeypatch):
    fake_surface = pygame.Surface((40, 60))
    monkeypatch.setattr(pygame.image, "load", lambda path: fake_surface)

# ----------------------
# Pruebas básicas iniciales
# ----------------------

def test_posicion_inicial():
    player = Player(100, 200)
    assert player.rect.topleft == (100, 200)

def test_movimiento_derecha():
    player = Player(0, 0)
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}
    player.update(keys)
    assert player.rect.x > 0

def test_salto_aplica_velocidad():
    player = Player(0, 0)
    player.jump = False
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True}
    player.update(keys)
    assert player.velocity_y == -14  # -15 + 1 por gravedad

def test_caida_termina_en_suelo():
    player = Player(0, 530)
    player.velocity_y = 10
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: False}
    player.update(keys)
    assert player.rect.bottom == 540
    assert player.jump is False

def test_movimiento_izquierda_bloqueado_fuera_mapa():
    player = Player(0, 0)
    keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False, pygame.K_SPACE: False}
    player.update(keys)
    assert player.rect.left >= 0

def test_movimiento_derecha_bloqueado_fuera_mapa():
    player = Player(WIDTH - 40, 0)
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}
    player.update(keys)
    assert player.rect.right <= WIDTH

def test_gravedad_aplica_correctamente():
    player = Player(0, 0)
    player.velocity_y = 0
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: False}
    player.update(keys)
    assert player.velocity_y == 1

def test_salto_no_aplica_si_ya_esta_saltando():
    player = Player(0, 0)
    player.jump = True
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True}
    initial_velocity = player.velocity_y
    player.update(keys)
    assert player.velocity_y != -15

def test_suelo_resetea_salto():
    player = Player(0, 530)
    player.jump = True
    player.velocity_y = 10
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: False}
    player.update(keys)
    assert player.jump is False

def test_velocidad_gravedad_acumulativa():
    player = Player(0, 0)
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: False}
    for _ in range(3):
        player.update(keys)
    assert player.velocity_y == 3

def test_tamaño_sprite_correcto():
    player = Player(0, 0)
    assert player.image.get_size() == (40, 60)

def test_rect_actualiza_correctamente_en_salto():
    player = Player(0, 300)
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True}
    player.update(keys)
    assert player.rect.y < 300

@pytest.mark.xfail(reason="Simula error crítico: jugador se sale del borde derecho")
def test_error_sale_fuera_de_la_pantalla_derecha():
    player = Player(WIDTH - 39, 0)
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}
    player.update(keys)
    assert player.rect.right <= WIDTH
