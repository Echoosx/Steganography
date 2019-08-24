# -*- coding: utf-8 -*-
import csv

def readcsv(csvfilepath):
    user_list = list()
    with open(csvfilepath, 'r',encoding='utf-8') as f:
        f_csv = csv.reader(f)
        headers=next(f_csv)
        for row in f_csv:
            user_list.append(row)
        return user_list

# 将新的注册用户信息写入csv文件
def writecsv(csvfilepath,username,password):
    user_info=[(username,password)]
    with open(csvfilepath,'a+',encoding="utf-8") as f:
        f_csv=csv.writer(f)
        f_csv.writerows(user_info)

# 判断注册请求是否合法
def register(username,password):
    user_list=readcsv("../config/config.csv")
    for user_info in user_list:
        if(len(user_info)==0):
            continue
        # 系统中已存在该用户，请求不合法
        if(username==user_info[0]):
            return False,1
    # 请求合法，写入新用户信息
    writecsv("../config/config.csv",username,password)
    return True,0

if __name__=="__main__":
    username=input("username:")
    password=input("password:")
    register(username,password)
