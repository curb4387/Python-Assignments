from images import Image
image = Image("smokey.gif")

for y in range(image.getHeight()):
    for x in range(image.getWidth()):
        (r, g, b) = image.getPixel(x, y)
        average = (r + g + b) // 3
        image.setPixel(x, y, (average, average, average))

image.draw()

input("wack")