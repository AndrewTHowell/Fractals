import turtle

screen = turtle.getscreen()

initialLength = 150
division = 3
levels = 4
angle = 150
branches = 6

cursor = screen.turtles()[0]
cursor.hideturtle()
cursor.setheading(90)
cursor.up()

cursor.backward(initialLength)

cursor.down()
cursor.speed(0)


def drawFractal(cursor, size, levelsLeft):
    if not levelsLeft:
        return

    initialPos = cursor.pos()
    initialHeading = cursor.heading()

    branchAngle = (2 * angle)/(branches - 1)

    for i in range(branches):
        cursor.left(angle)
        cursor.right(i * branchAngle)
        cursor.forward(size)
        drawFractal(cursor, size/division, levelsLeft - 1)

        cursor.up()
        cursor.setpos(initialPos)
        cursor.setheading(initialHeading)
        cursor.down()


drawFractal(cursor, initialLength, levels)

turtle.mainloop()
