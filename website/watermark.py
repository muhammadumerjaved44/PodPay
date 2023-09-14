from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io


def watermark_text(image_list, text, pos):
    # Create an Image Object from an Image
    watermark_list = []
    for i in range(len(image_list)):
        if image_list[i]:
            im = Image.open(image_list[i])
            width, height = im.size
            draw = ImageDraw.Draw(im)
            text = str(text)
            # print("text :", text)
            font = ImageFont.load_default()

            # font = ImageFont.truetype('arial.ttf', 36)
            textwidth, textheight = draw.textsize(text, font)

            # calculate the x,y coordinates of the text
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin
            # draw watermark in the bottom right corner
            black = (3, 8, 12)
            draw.text((x, y), text, fill=black, font=font)
            im.save(f"media/watermark-{image_list[i]}")
            watermark_list.append(f"watermark-{image_list[i]}")

        else:
            watermark_list.append("")
    return watermark_list
