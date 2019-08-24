# -*- coding: utf-8 -*-
from PIL import Image

class WritePng:
    """
    取得一个PIL图像 并改变所有的RGBA值为偶数（最低有效位置0）
    """
    def __rgbEven(self,img, length):
        list_rgba = list(img.getdata())  # 得到RGBA列表 [(r,g,b,a)][(r,g,b,a)...]
        even_list_rgba = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1, a >> 1 << 1)
                          for [r, g, b, a] in list_rgba[:length // 4]] + list_rgba[length // 4:]  # 通过移位操作将最低有效位置0
        even_img = Image.new(img.mode, img.size)
        even_img.putdata(even_list_rgba)  # 创建一个相同大小的Image类副本对象将新像素放入其中
        return even_img  # 返回Image类副本

    """
    将二进制int型转化成string
    """
    def __binStr(self, int):
        # 去掉 bin() 返回的二进制字符串中的 '0b'，并在左边补足 '0' 直到字符串长度为 8
        binary = "0" * (8 - (len(bin(int)) - 2)) + str(bin(int)).replace('0b', '')
        return binary

    """
    将字符串编码到图片中
    """
    def __imageEncode(self,img, data):
        # img信息
        imgData = img.getdata()

        # 将需要被隐藏的字符串转换成二进制字符串
        binary = ''.join(map(self.__binStr, bytearray(data, 'utf-8')))
        data_length = len(binary)

        # 获取Image类图片副本
        even_img = self.__rgbEven(img, 32 + data_length)
        even_imgData = even_img.getdata()
        even_imgColorList = list(even_imgData)

        # 如果不能编码全部数据， 抛出异常
        if len(binary) > len(imgData) * 4:
            raise Exception("Error: Size of the image cannot support more than "
                            + str(len(even_imgData) * 4) + " bits of information")

        # 要隐藏信息的长度存储在四字节长度里并加在隐藏信息之前
        img_type = "00"
        data_length_bin = "0" * (30 - (len(bin(data_length)) - 2)) + str(bin(data_length).replace('0b', ''))
        binary = img_type + data_length_bin + binary

        # 将 binary 中的二进制字符串信息编码进rgba像素里
        encoded_even_imgColorList = [(r + int(binary[index * 4 + 0]), g + int(binary[index * 4 + 1]),
                                      b + int(binary[index * 4 + 2]), a + int(binary[index * 4 + 3]))
                                     for index, (r, g, b, a) in
                                     enumerate(even_imgColorList[:8 + data_length // 4])] + even_imgColorList[
                                                                                            8 + data_length // 4:]
        encoded_even_img = Image.new(even_img.mode, even_img.size)
        encoded_even_img.putdata(encoded_even_imgColorList)
        return encoded_even_img

    """
    接口函数，给函数原文件位置，隐藏数据以及隐写后文件名称，接口函数便调用imageEncode函数进行隐写
    """
    def write(self,filename,data,savename):
        self.__imageEncode(Image.open(filename), data).save(savename)
        return True
