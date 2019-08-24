# -*- coding: utf-8 -*-
import csv

def writecsv(csvfilepath,username,password):
    headers=['用户名','密码']
    user_info=[(username,password)]
    with open(csvfilepath,'w',encoding="utf-8") as f:
        f_csv=csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(user_info)

writecsv("../config/config.csv","root","root")
