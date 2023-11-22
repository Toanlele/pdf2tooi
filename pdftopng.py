import fitz
import os
from PIL import Image

def convert_pdf2img(file_relative_path):

    page_num = 1
    filename = file_relative_path.split('.')[-2]
    if not os.path.exists(filename):
        os.makedirs(filename)

    pdf = fitz.open(file_relative_path)
    num_page = len(pdf)
    print(num_page)
    # image width , height
    image_width = 1080
    image_height = 1920
    images = []

    for page in pdf:
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x,zoom_y)
        pixmap = page.get_pixmap(matrix=mat, alpha=False)

        # image = Image.fromqpixmap(pixmap)
        # image = Image.open(image_file)
        # image = image.resize((image_width,image_height))
        # images.append(image)
        image_file = f"{filename}/{page_num}.png"
        pixmap.pil_save(image_file)

        image = Image.open(image_file)
        image = image.resize((image_width,image_height))
        images.append(image)
        print(f"第{page_num}保存图片完成")
        page_num += 1


    new_image = Image.new('RGB',(image_width,num_page*image_height))

    for index in range (0,num_page):

        start_height = index * image_height
        print(index,start_height)
        # new_image.paste(images[index],(0,0))
        new_image.paste(images[index],(0,start_height))
        # break

    new_image.save(f"{filename}.png")


if __name__ == "__main__":
    file_relative_path = "朱先陶获奖情况.pdf"

    convert_pdf2img(file_relative_path)