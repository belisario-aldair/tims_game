#test_player.py
from behave import given, when, then
from real_tims.player import Player
from real_tims.constants import WIDTH
import pygame

pygame.init()
pygame.display.set_mode((1, 1))

@given('el jugador está en la posición inicial exacta')
def step_start_player(context):
    context.player = Player(0, 0)

@when('el jugador se mueve a la derecha y luego salta')
def step_move_and_jump(context):
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}
    context.player.update(keys)
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True}
    context.player.update(keys)

@then('debe haberse movido hacia la derecha')
def step_check_right_movement(context):
    assert context.player.rect.x > 0

@then('debe estar en el aire')
def step_check_air(context):
    assert context.player.velocity_y < 0

@given('el jugador está en el borde derecho del mapa')
def step_player_at_right_edge(context):
    context.player = Player(WIDTH - 40, 0)

@when('se intenta mover a la derecha')
def step_try_move_right(context):
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_SPACE: False}
    context.player.update(keys)

@then('el jugador no debe salir del mapa')
def step_check_map_limit(context):
    assert context.player.rect.right <= WIDTH

@given('el jugador está ya en el aire')
def step_airborne(context):
    context.player = Player(100, 100)
    context.player.jump = True
    context.player.velocity_y = -5

@when('se intenta volver a saltar')
def step_attempt_double_jump(context):
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_SPACE: True}
    context.player.update(keys)

@then('el salto no debe reiniciarse')
def step_check_no_double_jump(context):
    assert context.player.velocity_y != -15
