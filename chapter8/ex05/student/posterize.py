# This program changes an image to use 2 colors

from images import Image

def posterize(image, color = (0, 0 ,0)):
    whitePixel = (255, 255, 255)
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average > 127:
                image.setPixel(x, y, whitePixel)
            else:
                image.setPixel(x, y, color)

def main():
    filename = input("Enter the image name: ")
    red = int(input("Enter the red (0-255): "))
    green = int(input("Enter the blue (0-255): "))
    blue = int(input("Enter the green (0-255): "))
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()

if __name__ == "__main__":
    main()

input("wack")