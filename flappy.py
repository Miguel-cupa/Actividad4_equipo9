"""Flappy, juego inspirado en Flappy Bird.

Ejercicios:
1. Llevar el puntaje.
2. Variar la velocidad.
3. Variar el tamaño de las bolas.
4. Permitir que el pájaro se mueva hacia adelante y hacia atrás.
"""

from random import *
from turtle import *

from freegames import vector

# Vector que representa la posición inicial del pájaro (x, y)
bird = vector(0, 0)
# Lista vacía que almacenará los obstáculos (bolas)
balls = []


def tap(x, y):
    """Mueve el pájaro hacia arriba al hacer clic en la pantalla."""
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    """Devuelve True si el punto está dentro de los límites de la pantalla."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Dibuja los objetos en la pantalla (pájaro y obstáculos)."""
    clear()

    goto(bird.x, bird.y)

    # El cambio visual es el pájaro de color azul y más grande.
    # Si choca, cambia a color rojo conservando el tamaño.
    if alive:
        dot(20, 'blue')
    else:
        dot(20, 'red')

    # Dibuja los obstáculos en la pantalla
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


def move():
    """Actualiza las posiciones del pájaro y los obstáculos en movimiento."""
    # Gravedad: hace que el pájaro caiga constantemente
    bird.y -= 5

    # Mueve los obstáculos hacia la izquierda
    for ball in balls:
        ball.x -= 3

    # Genera un nuevo obstáculo de manera aleatoria
    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    # Elimina los obstáculos que ya salieron de la pantalla para limpiar memoria
    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    # Si el pájaro toca el suelo o el techo, se acaba el juego
    if not inside(bird):
        draw(False)
        return

    # Si el pájaro choca con un obstáculo, se acaba el juego
    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    # Si sigue vivo, vuelve a dibujar y repite el ciclo de movimiento
    draw(True)
    ontimer(move, 50)


# Configuración inicial de la ventana gráfica
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()