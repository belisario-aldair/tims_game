Feature: Control completo del jugador

  Scenario: El jugador se mueve a la derecha y salta
    Given el jugador está en la posición inicial exacta
    When el jugador se mueve a la derecha y luego salta
    Then debe haberse movido hacia la derecha
    And debe estar en el aire

  Scenario: El jugador no puede salir del mapa por el borde derecho
    Given el jugador está en el borde derecho del mapa
    When se intenta mover a la derecha
    Then el jugador no debe salir del mapa

  Scenario: El jugador no puede saltar dos veces en el aire
    Given el jugador está ya en el aire
    When se intenta volver a saltar
    Then el salto no debe reiniciarse
