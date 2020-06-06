import turtle

screen = turtle.getscreen()

initialLength = 150
division = 1.4
levels = 12
angle = 90
branches = 2

cursor = screen.turtles()[0]
cursor.hideturtle()
cursor.setheading(90)
cursor.speed(0)

if angle < 45:
    cursor.up()
    cursor.backward(initialLength)
    cursor.down()


def drawFractal(fractalCursor, size, levelsLeft):
    if not levelsLeft:
        return

    initialPos = fractalCursor.pos()
    initialHeading = fractalCursor.heading()

    branchAngle = (2 * angle)/(branches - 1)

    for i in range(branches):
        fractalCursor.left(angle)
        fractalCursor.right(i * branchAngle)
        fractalCursor.forward(size)
        drawFractal(fractalCursor, size / division, levelsLeft - 1)

        fractalCursor.up()
        fractalCursor.setpos(initialPos)
        fractalCursor.setheading(initialHeading)
        fractalCursor.down()


drawFractal(cursor, initialLength, levels)

turtle.mainloop()
