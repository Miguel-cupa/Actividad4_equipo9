import turtle
from random import choice, random
from freegames import vector


def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


def move(player, change):
    """Cambia la posición del jugador."""
    state[player] += change


def rectangle(x, y, width, height):
    """Dibuja un rectángulo en (x, y) con el ancho y la altura dados."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for count in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw():
    """Dibuja el juego y mueve la pelota de pong."""
    turtle.fillcolor('blue')  # El color de las paletas es azul
    turtle.clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    turtle.up()
    turtle.goto(x, y)
    turtle.dot(10)
    turtle.update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    turtle.ontimer(draw, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: move(1, 20), 'w')
turtle.onkey(lambda: move(1, -20), 's')
turtle.onkey(lambda: move(2, 20), 'i')
turtle.onkey(lambda: move(2, -20), 'k')
draw()
turtle.done()
