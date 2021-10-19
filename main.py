from PIL import ImageDraw, ImageFont
import PIL.Image  # Used to avoid name conflict
from tkinter import *
from tkinter import filedialog


window = Tk()
window.title("Watermark Maker")
window.minsize(width=300, height=150)

user_text = Entry(width=30)
user_text.place(x=70, y=30)
user_text.focus()
user_text.insert(0, "Enter your text here")


def open_file_name():
    file_name = filedialog.askopenfilename(title="Select an Image")
    return file_name


def open_logo():
    file_name = filedialog.askopenfilename(title="Select an Image")
    return file_name


def add_watermark_text(image, text):
    opened_image = PIL.Image.open(image)

    image_width, image_height = opened_image.size

    draw = ImageDraw.Draw(opened_image)
    font_size = int(image_width / 10)
    font = ImageFont.truetype("arial.ttf", font_size)

    x, y = int(image_width / 2), int(image_height / 2)

    draw.text((x, y), text, font=font, fill="#fff", stroke_width=10, stroke_fill="#222", anchor="ms")

    opened_image.show()
    opened_image.save("output_text.png")


def add_watermark_logo(image, logo, position):
    opened_image = PIL.Image.open(image).convert("RGBA")
    watermark_image = PIL.Image.open(logo).convert("RGBA")

    opened_image.paste(watermark_image, position, mask=watermark_image)
    opened_image.show()
    opened_image.save("output_image.png")


add_text_button = Button(text="Add Text", command=lambda: add_watermark_text(open_file_name(), user_text.get()),
                              bg="yellow", highlightthickness=0)
add_text_button.place(x=115, y=70)

add_image_button = Button(text="Watermark Image", command=lambda: add_watermark_logo(open_file_name(), open_logo(), position=(0, 0)),
                          bg="yellow", highlightthickness=0)
add_image_button.place(x=90, y=110)

exit_button = Button(window, text="Exit", command=window.destroy)
exit_button.place(x=125, y=150)


window.mainloop()
