#test_enemy.py
from behave import given, when, then
from real_tims.enemy import Enemy

import pygame

pygame.init()
pygame.display.set_mode((1, 1))

@given('un enemigo comienza en x = 100 entre 50 y 300')
def step_enemy_start(context):
    context.enemy = Enemy(100, 0, 50, 300)

@when('el enemigo se actualiza')
def step_enemy_update(context):
    context.old_x = context.enemy.rect.x
    context.old_speed = context.enemy.speed
    context.enemy.update()

@then('debe haber avanzado hacia la derecha')
def step_enemy_moved(context):
    assert context.enemy.rect.x > context.old_x

@given('un enemigo está al borde derecho')
def step_enemy_right_limit(context):
    context.enemy = Enemy(260, 0, 50, 300)  # 260 + 40 = 300

@then('debe cambiar de dirección a la izquierda')
def step_enemy_reverses_right(context):
    assert context.enemy.speed == -2

@given('un enemigo está al borde izquierdo')
def step_enemy_left_limit(context):
    context.enemy = Enemy(50, 0, 50, 300)
    context.enemy.speed = -2

@then('debe cambiar de dirección a la derecha')
def step_enemy_reverses_left(context):
    assert context.enemy.speed == 2

@given('su velocidad es negativa')
def step_set_negative_speed(context):
    context.enemy.speed = -2
