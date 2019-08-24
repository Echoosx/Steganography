# -*- coding: utf-8 -*-
from PIL import Image
import os
import write_png
import write_jpg

"""
接口函数，前端调用，向路径path中写入数据data并保存为save文件
"""
def writeStart(path, data, save):
    dirpath, filename = os.path.split(path)
    os.chdir(dirpath)           # 存储位置
    img=Image.open(filename)    # 文件名称
    color_list=list(img.getdata())
    if (len(color_list[0]) == 4):   # png
        write=write_png.WritePng()
    else:
        write=write_jpg.WriteJpg()
    write.write(filename,data,save)