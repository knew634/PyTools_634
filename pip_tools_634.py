# -- coding: utf-8 --
import os


# 获取pip版本
def get_pip_version():
    pip_version = os.system("pip -V")
    return pip_version


# 换源安装库
def install_lib(lib_name, source="https://pypi.douban.com/simple"):
    os.system("pip install -i " + source + " " + "--trusted-host pypi.douban.com " + lib_name)


# 列出所有库并且装进列表
def list_lib(remove_file=True):
    ls = []
    os.system("pip list > pip_list.txt")
    with open("pip_list.txt", "r") as f:
        for line in f.readlines():
            ls.append(line.split(" ")[0])
    if remove_file:
        os.remove("pip_list.txt")
    return ls[2:]


# 更新库
def update_lib(lib_name, source="https://pypi.douban.com/simple"):
    # 判断库是否存在
    if lib_name in list_lib():
        os.system("pip install --upgrade " + lib_name + " -i " + source + " " + "--trusted-host pypi.douban.com")
    else:
        print("库不存在")


# 更新所有库
def update_all_lib(source="https://pypi.douban.com/simple"):
    for lib_name in list_lib():
        os.system("pip install --upgrade " + lib_name + " -i " + source + " " + "--trusted-host pypi.douban.com")


# 卸载库
def uninstall_lib(lib_name):
    # 判断库是否存在
    if lib_name in list_lib():
        os.system("pip uninstall " + lib_name)
        print(f"卸载{lib_name}成功")
    else:
        print("库不存在")


# 安装所有库（requirements.txt）
def install_all_lib(source="https://pypi.douban.com/simple"):
    os.system("pip install -r requirements.txt -i " + source + " " + "--trusted-host pypi.douban.com")


# 生成requirements.txt
def generate_requirements():
    os.system("pip freeze > requirements.txt")


# 列出库的信息
def list_lib_info(lib_name):
    os.system("pip show " + lib_name)


if __name__ == '__main__':
    install_lib("FuzzyTM")
    # install_lib("ctypes")
    # install_lib("pyqt5")
    # install_lib("pyqt5-tools")
    # install_lib("pyqt6")
    # install_lib("pyqt6-tools")
    # update_lib("scipy")
    # install_lib("pyvista")
    # list_lib(remove_file=False)
    # list_lib_info("numpy")
    # opencv-contrib-python
    # opencv-python-headless
    # uninstall_lib("urllib3")