# -*- coding: utf-8 -*-
from PIL import Image

class WriteJpg:

    """
    取得一个PIL图像 并改变所有的RGB值为偶数（最低有效位置0）
    """
    def __rgbEven(self,img, length):
        list_rgb = list(img.getdata())  # 得到RGB列表 [(r,g,b)][(r,g,b)...]
        even_list_rgb = [(r >> 1 << 1, g >> 1 << 1, b) for [r, g, b] in
                         list_rgb[:length // 2]] + list_rgb[length // 2:]  # 通过移位操作将最低有效位置0
        even_img = Image.new(img.mode, img.size)
        even_img.putdata(even_list_rgb)  # 创建一个相同大小的Image类副本对象将新像素放入其中
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
        if len(binary) > len(imgData) * 2:
            raise Exception("Error: Size of the image cannot support more than "
                            + str(len(even_imgData) * 2) + " bits of information")

        # 要隐藏信息的类型长度存储在四字节长度里并加在隐藏信息之前
        img_type = "01"
        data_length_bin = "0" * (30 - (len(bin(data_length)) - 2)) + str(bin(data_length).replace('0b', ''))
        binary = img_type + data_length_bin + binary

        # print(binary)
        # 将 binary 中的二进制字符串信息编码进rgba像素里
        encoded_even_imgColorList = [(r + int(binary[index * 2 + 0]),
                                      g + int(binary[index * 2 + 1]), b)
                                     for index, (r, g, b) in
                                     enumerate(even_imgColorList[:16 + data_length // 2])] \
                                    + even_imgColorList[16 + data_length // 2:]

        encoded_even_img = Image.new(even_img.mode, even_img.size)
        encoded_even_img.putdata(encoded_even_imgColorList)
        return encoded_even_img


    def write(self,filename,data,savename):
        self.__imageEncode(Image.open(filename), data).save(savename)
        return True