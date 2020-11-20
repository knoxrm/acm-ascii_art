import PIL.Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",","."]

def resize(image, new_width=100):
    height, width = image.size
    new_height = int(new_width*(height/width))
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel2ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for i in pixels:
        ascii_str += ASCII_CHARS[i//25]
    return ascii_str


def main():
    path = "wallhaven-nkpmo1.jpg"

    try:
        image = PIL.Image.open(path)
    except:
        print(path + "not found")

    image = resize(image)
    greyscale_image = to_greyscale(image)

    ascii_string = pixel2ascii(greyscale_image)

    img_width = greyscale_image.width
    ascii_str_len = len(ascii_string)
    ascii_img = ""

    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_string[i:i+img_width] + "\n"

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

main()
    
