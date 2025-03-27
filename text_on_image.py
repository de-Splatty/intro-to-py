from PIL import Image, ImageDraw, ImageFont

image = Image.open("images/cruiser.jpg")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("fonts/DancingScript-VariableFont_wght.ttf", 80)

text = "Desert Safari"
text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]

x = (image.width - text_width) // 2
y = (image.height - text_height) // 2

draw.text((x, y), text, font=font, fill="black")

output_path = "images/desert_safari.jpg"
image.show()
