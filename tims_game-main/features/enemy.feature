Feature: Comportamiento del enemigo

  Scenario: El enemigo se mueve a la derecha
    Given un enemigo comienza en x = 100 entre 50 y 300
    When el enemigo se actualiza
    Then debe haber avanzado hacia la derecha

  Scenario: El enemigo rebota al alcanzar su límite derecho
    Given un enemigo está al borde derecho
    When el enemigo se actualiza
    Then debe cambiar de dirección a la izquierda

  Scenario: El enemigo rebota al alcanzar su límite izquierdo
    Given un enemigo está al borde izquierdo
    And su velocidad es negativa
    When el enemigo se actualiza
    Then debe cambiar de dirección a la derecha
