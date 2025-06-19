#test_movimiento.py
from behave import given, when, then
from real_tims.player import Player
import pygame

pygame.init()
pygame.display.set_mode((1, 1))

@given('el jugador está en x = 0')
def step_set_position(context):
    context.jugador = Player(0, 0)

@when('se presiona solo la tecla derecha')
def step_move_right_only(context):
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}
    context.jugador.update(keys)

@then('la posición x del jugador debe aumentar')
def step_verify_position(context):
    assert context.jugador.rect.x > 0
