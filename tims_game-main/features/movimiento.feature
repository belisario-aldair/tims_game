Feature: Movimiento básico del jugador

  Scenario: El jugador se mueve hacia la derecha
    Given el jugador está en x = 0
    When se presiona solo la tecla derecha
    Then la posición x del jugador debe aumentar
