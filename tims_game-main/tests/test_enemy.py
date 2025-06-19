import sys
import os
import pygame
import pytest
from unittest import mock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from real_tims.enemy import Enemy

pygame.init()
pygame.display.set_mode((1, 1))

# Fixture para mockear la carga de imagen del enemigo
@pytest.fixture(autouse=True)
def mock_pygame_image(monkeypatch):
    fake_surface = pygame.Surface((40, 40))
    monkeypatch.setattr(pygame.image, "load", lambda path: fake_surface)

def test_posicion_inicial():
    enemy = Enemy(100, 200, 50, 300)
    assert enemy.rect.topleft == (100, 200)

def test_direccion_inicial():
    enemy = Enemy(100, 0, 50, 300)
    assert enemy.speed == 2

def test_movimiento_derecha():
    enemy = Enemy(100, 0, 50, 300)
    x_inicial = enemy.rect.x
    enemy.update()
    assert enemy.rect.x == x_inicial + 2

def test_rebote_al_max_x():
    enemy = Enemy(260, 0, 50, 300)  # 260 + 40 = 300 justo en el borde
    enemy.update()
    assert enemy.speed == -2

def test_rebote_al_min_x():
    enemy = Enemy(50, 0, 50, 300)
    enemy.speed = -2
    enemy.update()
    assert enemy.speed == 2

def test_movimiento_bloqueado_fuera_rango():
    enemy = Enemy(100, 0, 90, 110)
    for _ in range(50):
        enemy.update()
        assert 90 <= enemy.rect.x <= 110
