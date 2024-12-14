from turtle import Turtle
import math
t = Turtle()

def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x + radius, y)
    t.down()
    t.setheading(90)
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)

def main():
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    radius = int(input("Enter the radius: "))
    drawCircle(t, x, y, radius)

if __name__ == "__main__":
    main()

input("booo")