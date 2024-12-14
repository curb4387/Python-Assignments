from images import Image
image = Image("smokey.gif")

def invert(image, r, g, b):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = 255 - r
            g = 255 - g
            b = 255 - b
            image.setPixel(x, y, (r, g, b))

# 2 color testing
# def posterize(image, color = (0, 0 ,0)):
#     whitePixel = (255, 255, 255)
#     for x in range(image.getWidth()):
#         for y in range(image.getHeight()):
#             (r, g, b) = image.getPixel(x, y)
#             average = (r + g + b) // 3
#             if average > 127:
#                 image.setPixel(x, y, whitePixel)
#             else:
#                 image.setPixel(x, y, color)

def main():
    # grayscale testing
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            image.setPixel(x, y, (average, average, average))
    invert(image, r, g, b)
    image.draw()

if __name__ == "__main__":
    main()

input("booo")