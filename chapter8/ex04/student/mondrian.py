from turtle import Turtle, tracer, update, colormode
import random
colormode(255)

def fillRectangle(t, x1, y1, x2, y2): # x1, y1, x2, y2 are the corners needed for each rectangle to be filled
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    # make the pen color and fill color the same random color
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

def mondrian(t, x1, y1, x2, y2, level):
    if level > 0:
        fillRectangle(t, x1, y1, x2, y2)
        # figure out where to place the rectangles: 1 = vertical, 2 = horizontal
        vertical = random.randint(1, 2)
        if vertical == 1:
            # here we want to call mondrian in itself - recursive function
            # when we call mondrian, we call it twice
            # it needs to fill a subset, not refill the whole window so we have to divide into thirds
            mondrian(t, x1, y1, ((x2 - x1) / 3 + x1), y2, level - 1)
            mondrian(t, ((x2 - x1) / 3 + x1), y1, x2, y2, level - 1)
        else:
            mondrian(t, x1, y1, x2, ((y2 - y1) / 3 + y1), level - 1)
            mondrian(t, x1, ((y2 - y1) / 3 + y1), x2, y2, level - 1)

def main():
    level = int(input("Enter the level: "))
    t = Turtle()
    t.speed(10)
    # this is the "aesthetically right moment" and then turtle will automatically finish the rest
    # use the same if statement for the update() function
    if level > 6:
        tracer(False)
    t.hideturtle()
    # find the width and height of the user's screen
    # use width and height as the starting coordinates: x1, y1, x2, y2
    width = t.screen.window_width() // 2
    height = t.screen.window_height() // 2
    mondrian(t, -width, height, width, -height, level)
    if level > 6:
        update()

if __name__ == "__main__":
    main()

input("boooooo")