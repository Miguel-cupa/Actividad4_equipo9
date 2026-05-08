"""Flappy, juego inspirado en Flappy Bird."""

from random import randrange
from turtle import (
    clear, done, dot, goto, hideturtle,
    onscreenclick, ontimer, setup, tracer, up, update
)
from freegames import vector

bird = vector(0, 0)
balls = []


def tap(x, y):
    """Mueve el pájaro hacia arriba al hacer clic."""
    up_vector = vector(0, 30)
    bird.move(up_vector)


def inside(point):
    """Devuelve True si el punto está dentro de los límites."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Dibuja los objetos en la pantalla."""
    clear()
    goto(bird.x, bird.y)

    if alive:
        dot(20, 'blue')
    else:
        dot(20, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


def move():
    """Actualiza las posiciones del pájaro y obstáculos."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
