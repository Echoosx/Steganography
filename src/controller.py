# -*- coding: utf-8 -*-
import write_control
import read_control

filename='../img/orign.jpg'
savename='encodeImage.png'

if __name__ == "__main__":
    while (True):
        choice = str(input("请输入服务类型（1：信息写入  2：信息读取  0：退出）"))
        if (choice == '0'):
            print("已退出")
            break
        elif (choice == '1'):
            # path = input("请输入图片路径：")
            # path=path.replace(" ",'')
            data = input("请输入要隐藏的信息：")
            print(data)
            print("正在写入信息，请稍候。。。")
            write_control.writeStart(filename,data,savename)
            print("信息写入成功，保存为副本图片%s" %savename)
        elif (choice == '2'):
            print("正在读取隐藏信息。。。")
            data=read_control.readStart(savename)[1]
            print("隐藏信息为\"",data, "\"")
        else:
            print("服务选择有误")
            continue
