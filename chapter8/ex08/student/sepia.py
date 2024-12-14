# This program makes an image into sepia color.
# First it changes the image to grayscale, then sets it to sepia.

from images import Image

def sepia(image):
    grayscale(image)
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            (r, g, b) = image.getPixel(x, y)
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
            image.setPixel(x, y, (r, g, b))

def grayscale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            gray = r + g + b
            # average = (r + g + b) // 3 - this is using the "crude" averages
            image.setPixel(x, y, (gray, gray, gray))

def main():
    filename = input("Enter the file name: ")
    image = Image(filename)
    sepia(image)
    image.draw()

if __name__ == "__main__":
    main()