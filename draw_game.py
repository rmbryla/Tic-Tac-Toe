import turtle


def HOME():
    return -300,300


def make_dict():  # locations on the canvas of the different indexes
    dict = {}
    dict[7] = -300,300
    dict[8] = -100, 300
    dict[9] = 100, 300
    dict[4] = -300, 100
    dict[5] = -100, 100
    dict[6] = 100, 100
    dict[1] = -300, -100
    dict[2] = -100, -100
    dict[3] = 100, -100
    return dict


def draw_blank():
    turtle.speed(0)
    turtle.pensize(0)
    turtle.color('black')
    turtle.up()
    turtle.goto(0,0)
    turtle.back(300)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.down()
    turtle.forward(600)
    turtle.back(200)
    turtle.left(90)
    turtle.back(400)
    turtle.forward(600)
    turtle.back(400)
    turtle.right(90)
    turtle.back(400)
    turtle.forward(600)
    turtle.back(400)
    turtle.left(90)
    turtle.forward(400)
    turtle.back(600)
    turtle.right(90)
    turtle.up()
    turtle.goto(HOME())
    turtle.speed(10) # change this to make the game faster or slower (0 fastest)


def draw_x():
    turtle.pensize(3)
    turtle.color('red')
    turtle.up()
    turtle.right(45)
    turtle.forward(20)
    turtle.down()
    turtle.forward(242)
    turtle.back(121)
    turtle.left(90)
    turtle.forward(121)
    turtle.back(242)
    turtle.right(45)
    turtle.up()
    turtle.goto(HOME())


def draw_o():
    turtle.pensize(3)
    turtle.color('blue')
    turtle.up()
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.down()
    turtle.circle(85)
    turtle.up()
    turtle.goto(HOME())


def draw_at(index, turn):
    turtle.up()
    indexes = make_dict()
    turtle.goto(indexes[index])
    if turn == 'O':
        draw_o()
    elif turn == 'X':
        draw_x()


def main():  # just for testing
    turtle.speed(0)
    draw_blank()
    turtle.speed(1)
    draw_at(5, 'X')
    draw_at(3, 'O')
    turtle.done()


if __name__ == "__main__":
    main()