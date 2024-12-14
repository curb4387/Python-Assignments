from images import Image
image = Image("smokey.gif")

def lighten(image, value):
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            (r, g, b) = image.getPixel(x, y)
            if r + value < 255:
                r = r + value
            else:
                r = 255
            if g + value < 255:
                g = g + value
            else:
                g = 255
            if b + value < 255:
                b = b + value
            else:
                b = 255
            image.setPixel(x, y, (r, g, b))

def darken(image, value):
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            (r, g, b) = image.getPixel(x, y)
            if r - value > 0:
                r = r - value
            else:
                r = 0
            if g - value > 0:
                g = g - value
            else:
                g = 0
            if b - value > 0:
                b = b - value
            else:
                b = 0
            image.setPixel(x, y, (r, g, b))

def colorFilter(image, red, green, blue):
    whitePixel = (255, 255, 255)
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            (r, g, b) = image.getPixel(x, y)
            if r + red < 255:
                r = r + red
            else:
                r = 255
            if g + green < 255:
                g = g + green
            else:
                g = 255
            if b + blue < 255:
                b = b + blue
            else:
                b = 255
            image.setPixel(x, y, (r, g, b))

def main():
    choice = input("""Choose an option (1-3):
1) lighten
2) darken
3) color
""")
    if choice == "1":
        value = int((input("Enter the value to lighten the image by (0-255): ")))
        lighten(image, value)
    elif choice == "2":
        value = int((input("Enter the value to darken the image (0-255): ")))
        darken(image, value)
    elif choice == "3":
        red = int(input("Enter the red value to color the image (0-255): "))
        green = int(input("Enter the green value to color the image (0-255): "))
        blue = int(input("Enter the blue value to color the image (0-255): "))
        colorFilter(image, red, green, blue)
    image.draw()

if __name__ == "__main__":
    main()

input("yeehaw")