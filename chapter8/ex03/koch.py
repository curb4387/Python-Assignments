from turtle import Turtle, tracer, update

# Method to draw each line 3 times
def kochFractal(width, height, size, level):
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()
    drawFractalLine(t, size, 0, level)
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)

# Method to determine whether to draw a straight line for level 0 or other for levels 1+
def drawFractalLine(t, distance, angle, level):
    if level == 0:
        drawLine(t, distance, angle)
    else:
        drawFractalLine(t, distance // 3, angle, level - 1)
        drawFractalLine(t, distance // 3, angle + 60, level - 1)
        drawFractalLine(t, distance // 3, angle - 60, level - 1)
        drawFractalLine(t, distance // 3, angle, level - 1)

# Method to draw a straight line
def drawLine(t, distance, angle):
    t.setheading(angle)
    t.forward(distance)


def main():
    level = int(input("Enter the level: "))
    tracer(False)
    kochFractal(200, 200, 400, level)
    update()

if __name__ == "__main__":
    main()

input("booo")