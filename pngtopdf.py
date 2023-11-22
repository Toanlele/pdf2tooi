import os
import fitz  # pip install PyMuPDF
from tqdm import tqdm

def GetFileName(dir_path):
    file_list = [os.path.join(dirpath, filesname) \
                 for dirpath, dirs, files in os.walk(dir_path) \
                 for filesname in files]
    file_list.sort()
    return file_list

def pic2pdf(img_dir, filename):
    doc = fitz.open()
    file_lt = GetFileName(img_dir)
    for img in tqdm(file_lt):
        file_type = img.split('\\')[-1].split('.')[-1]
        if file_type not in ['jpg', 'png']:
            continue
        imgdoc = fitz.open(img)  # 打开图片
        # pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        pdfbytes = imgdoc.convert_to_pdf()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)  # 将当前页插入文档
    if os.path.exists("{}".format(filename)):
        os.remove("{}".format(filename))
    doc.save("{}".format(filename))  # 保存pdf文件
    print("保存 {} 成功".format(filename))
    doc.close()


if __name__ == '__main__':
    img_dir = r"./朱先陶获奖情况"
    #这里填写需要把图片转成PDF文件的目录
    filename = "朱先陶个人简历15736369491.pdf"
    pic2pdf(img_dir, filename)
