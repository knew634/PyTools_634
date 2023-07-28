# -- coding: utf-8 --
import os


def install_lib(lib_name, source="https://pypi.douban.com/simple"):
    os.system("pip install -i " + source + " " + "--trusted-host pypi.douban.com " + lib_name)


try:
    from PyPDF2 import PdfMerger
except ImportError:
    install_lib("PyPDF2")


def merge_pdfs(folder_path, output_filename):
    # 创建一个PdfFileMerger对象来处理合并操作
    merger = PdfMerger()

    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)

    # 只处理PDF文件
    pdf_files = [f for f in files if f.endswith('.pdf')]

    # 遍历每个PDF文件并合并
    for file in pdf_files:
        file_path = os.path.join(folder_path, file)

        # 将文件添加到合并器中
        merger.append(file_path)

    # 构建输出文件的完整路径
    output_path = os.path.join(folder_path, output_filename)

    # 保存合并后的PDF文件
    merger.write(output_path)

    # 关闭合并器
    merger.close()


# 获取当前文件所在目录
current_directory = os.getcwd()

# 指定包含单页PDF文件的文件夹路径和输出文件名
folder_path = current_directory
output_filename = 'merged.pdf'

# 调用函数进行合并
merge_pdfs(folder_path, output_filename)
