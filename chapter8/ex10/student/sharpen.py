from images import Image
image = Image("smokey.gif")

def sharpen(image, sharp, edge):
    def average(triple):
        (r, g, b) = triple
        return (r + g + b) // 3
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for x in range(1, image.getWidth()):
        for y in range(image.getHeight() - 1):
            (r, g, b) = image.getPixel(x, y)
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            if abs(oldLum - bottomLum) > edge or abs(oldLum - bottomLum) > edge:
                if r > sharp:
                    r = r - sharp
                else:
                    r = 0
                if g > sharp:
                    g = g - sharp
                else:
                    g = 0
                if b > sharp:
                    b = b - sharp
                else:
                    b = 0
                image.setPixel(x, y, (r, g, b))

def main():
    sharp = int(input("Enter the degree to sharpen the image by (0-255): "))
    edge = 20
    sharpen(image, sharp, edge)
    image.draw()

if __name__ == "__main__":
    main()

input("yeehaw")