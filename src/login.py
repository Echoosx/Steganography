# -*- coding: utf-8 -*-
import csv


def readcsv(csvfilepath):
    user_list = list()
    with open(csvfilepath, 'r', encoding='utf-8') as f:
        f_csv = csv.reader(f)  # 创建csv的reader对象b
        headers = next(f_csv)
        for row in f_csv:
            user_list.append(row)
        return user_list


def loginable(username, password):  # 对登录请求进行处理
    user_list = readcsv("../config/config.csv")
    for user_info in user_list:
        # 用户名密码正确，允许登录
        if (user_info[0] == username and user_info[1] == password):
            return True, 0
        # 用户名正确，密码错误，不允许登录
        if (user_info[0] == username and user_info[1] != password):
            return False, 1
    # 用户名不存在，不允许登录
    return False, 2


if __name__ == "__main__":
    username = input("username:")
    password = input("password:")
    able, error = loginable(username, password)
    if (able):
        print("成功")
    else:
        if (error == 1):
            print("密码错误")
        elif (error == 2):
            print("无此用户")
        else:
            pass
