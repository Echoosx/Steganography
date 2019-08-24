# -*- coding: utf-8 -*-
from PIL import Image

class Read:
    """
    从二进制字符串转为utf-8字符
    """

    def __getData(self, binary):
        index = 0
        data = ''
        while index + 1 < len(binary):
            chartype = binary[index:].index('0')  # 存放字符所占字节数，一个字节的字符会存为 0
            if chartype == 0:
                length = 8
            else:
                length = chartype * 8
            data += chr(int(self.__getEffectUTF(binary[index:index + length], chartype), 2))
            index += length
        return data

    """
    对单个utf类型的二进制编码进行解析，获取有效部分
    """

    def __getEffectUTF(self, binary, chartype):
        utfCode = binary[chartype + 1:8]
        if chartype > 0:
            for i in range(1, chartype):
                utfCode += binary[i * 8 + 2:(i + 1) * 8]
        return utfCode

    """
    解码隐藏数据
    """

    def __imageDecode(self, image):
        encode_img_ColorList = list(image.getdata())  # 获得像素列表

        if (len(encode_img_ColorList[0]) == 4):  # 如果是png格式的图片，格式代码‘00’
            img_type = ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g))
                                for (r, g, b, a) in encode_img_ColorList[:1]])
        else:  # 如果是jpg格式的图片 格式代码‘01’
            img_type = ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g))
                                for (r, g, b) in encode_img_ColorList[:1]])
        if (img_type == "00"):
            # 提取前四字节获得数据长度
            data_length = int(
                ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g)) + str(int(b >> 1 << 1 != b)) + str(
                    int(a >> 1 << 1 != a)) for (r, g, b, a) in encode_img_ColorList[:8]]), 2)
            # 提取图片中所有最低有效位中的数据
            binary = ''.join(
                [str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g)) + str(int(b >> 1 << 1 != b)) + str(
                    int(a >> 1 << 1 != a)) for (r, g, b, a) in encode_img_ColorList[8:data_length // 4 + 8]])

            # print(binary)
            data = self.__getData(binary)
            return True, data

        elif (img_type == "01"):
            # 提取前四字节获得数据长度
            length_bin = ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g))
                                  for (r, g, b) in encode_img_ColorList[:16]])
            data_length = int(length_bin[2:], 2)
            # 提取图片中所有最低有效位中的数据
            binary = ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g))
                              for (r, g, b) in encode_img_ColorList[16:data_length // 2 + 16]])

            # print(binary)
            data = self.__getData(binary)
            return True, data

        else:  # 错误处理，如果用户拿一个没有被隐藏过信息的文件
            data = "错误:该文件不是信息隐藏文件"
            return False, data

    """
    接口函数，给函数隐写后文件位置，接口函数便调用imageDecode函数对图片进行读取
    """
    def read(self, path):
        data = self.__imageDecode(Image.open(path))
        return data
