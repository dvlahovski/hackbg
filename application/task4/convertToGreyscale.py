from PIL import Image


def convertToGreyscale(imgPath):
    image = Image.open(imgPath)
    width, height = image.size

    for x in range(0, width):
        for y in range(0, height):
            color = image.getpixel((x, y))
            val = int(0.2126*color[0] + 0.7152*color[1] + 0.0722*color[2])
            new_color = (val, val, val)
            image.putpixel((x, y), new_color)

    image.save("grayscale_" + imgPath)
