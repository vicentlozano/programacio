import pygame
import sys


# Inicializar Pygame
pygame.init()

# Configurar la ventana
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Cargar la imagen de la pelota
pelota = pygame.image.load('C:/Users/lozan/OneDrive/Documentos/programacio/PongGame/images/basketball-155997_640.png')
ancho_nuevo = 30
alto_nuevo = 30
pelota = pygame.transform.scale(pelota, (ancho_nuevo, alto_nuevo))

# Configurar la posición inicial y la velocidad de la pelota
posicion = [0, 0]
velocidad = [1.5, 1.5]

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la posición de la pelota
    dt = clock.tick(60)/4
    posicion[0] += velocidad[0] *dt
    posicion[1] += velocidad[1] *dt

    # Hacer que la pelota rebote en los bordes de la ventana
    if posicion[0] < 0 or posicion[0] > size[0] - pelota.get_width():
        velocidad[0] = -velocidad[0]
    if posicion[1] < 0 or posicion[1] > size[1] - pelota.get_height():
        velocidad[1] = -velocidad[1]

    # Dibujar la pelota en la nueva posición
    screen.fill((0, 0, 0))
    screen.blit(pelota, posicion)

    # Actualizar la pantalla
    pygame.display.flip()