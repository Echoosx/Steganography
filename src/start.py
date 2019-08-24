#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wxGui
import wxLoginGui
import wxRegisterGui
import write_control
import read_control
import login
import register
import os

# 用户登录界面
class LoginWindow(wxLoginGui.LoginFrame):
    def __init__(self,parent):
        wxLoginGui.LoginFrame.__init__(self, parent)

    def loginEvent(self, event):
        username=self.usernameInput.GetValue()
        password=self.passwordInput.GetValue()
        able, error = login.loginable(username, password)
        if (able):
            login_win.Close()
            main_win=MainWindow(None)
            main_win.Show()
        else:
            if (error == 1):
                self.message.SetLabel("密码错误！")
            elif (error == 2):
                self.message.SetLabel("无此用户！")
            else:
                pass

    # 打开注册界面
    def registerShow(self, event):
        register_win = RegisterWindow(None)
        register_win.Show()


# 用户注册界面
class RegisterWindow(wxRegisterGui.RegisterFrame):
    def __init__(self, parent):
        wxRegisterGui.RegisterFrame.__init__(self, parent)

    # 注册按钮功能
    def registerEvent(self, event):
        newusername=self.usernameInput.GetValue()
        newpassword1=self.passwordInput1.GetValue()
        newpassword2=self.passwordInput2.GetValue()
        if(newusername==""):
            self.message.SetLabel("用户名不能为空！")
            return
        if(newpassword1!=newpassword2):
            self.message.SetLabel("输入密码不一致！")
            return
        if(newpassword1==""):
            self.message.SetLabel("密码不能为空！")
            return
        else:
            able,temp=register.register(newusername,newpassword1)
            if(able):
                self.message.SetLabel("注册成功！")
            else:
                self.message.SetLabel("用户已存在，注册失败！")

    # 关闭注册框
    def cancle(self, event):
        self.Close()

# 从源文件中将主窗体继承下来
class MainWindow(wxGui.bodyFrame):
    # 初始化函数，初始化窗体并默认选中写入功能
    def __init__(self, parent):
        wxGui.bodyFrame.__init__(self, parent)
        self.writeAbleChoice.SetValue(True)

    # 将写入窗体清空
    def clearwrite(self, event):
        self.choseFile.SetPath('')
        self.dataInput.SetValue('')
        self.saveName.SetValue('')
        self.messageLabel.SetLabel('')

    # 将读取窗体清空
    def clearread(self, event):
        self.choseFile2.SetPath('')
        self.dataOutput.SetValue('')
        self.messageLabel2.SetLabel('')

    # 选中写入功能时，激活写入窗体中的组件，并封锁读取功能组件
    def writeable(self, event):
        self.choseFile.Enable(True)
        self.dataInput.Enable(True)
        self.saveName.Enable(True)
        self.writeButton.Enable(True)
        self.cancleButton.Enable(True)
        self.choseFile2.Enable(False)
        self.readButton.Enable(False)
        self.cancleButton2.Enable(False)
        self.dataOutput.Enable(False)
        self.dataOutput.SetValue('')
        self.messageLabel2.SetLabel('')

    # 同上反之
    def readable(self, event):
        self.choseFile.Enable(False)
        self.dataInput.Enable(False)
        self.saveName.Enable(False)
        self.writeButton.Enable(False)
        self.cancleButton.Enable(False)
        self.choseFile2.Enable(True)
        self.readButton.Enable(True)
        self.cancleButton2.Enable(True)
        self.dataOutput.Enable(True)
        self.messageLabel.SetLabel('')

    # 写入功能，从组件中读取用户输入的信息，异常处理和用户交互
    def writeStart(self, event):
        self.messageLabel.SetLabel('正在写入信息，请稍候。。。')
        path = self.choseFile.GetPath()
        data = self.dataInput.GetValue()
        save = self.saveName.GetValue()
        if (path == ''):
            self.messageLabel.SetLabel('原始图片路径不能为空')
            return 0
        if (not os.path.exists(path)):
            self.messageLabel.SetLabel('原始图片路径不正确')
            return 0
        if (data == ''):
            self.messageLabel.SetLabel('没有输入要隐藏的信息')
            return 0
        if (save == ''):
            self.messageLabel.SetLabel('要保存的文件名不能为空')
            return 0
        if (os.path.splitext(save)[1] != ".png"):
            save = save + ".png"
        if (os.path.splitext(path)[1] == '.png' or '.jpg'):
            write_control.writeStart(path, data, save)
        else:
            self.messageLabel.SetLabel('暂不支持此类文件的信息隐藏')
            return 0

        self.messageLabel.SetLabel('写入成功！保存为与原图片同路径下的 ' + save)

    # 读取功能，同样读取路径，将结果显示并做异常处理和交互
    def readStart(self, event):
        path = self.choseFile2.GetPath()
        if (path == ''):
            self.messageLabel.SetLabel('图片路径不能为空')
            return 0
        if (not os.path.exists(path)):
            self.messageLabel.SetLabel('图片路径不正确')
            return 0
        if (os.path.splitext(path)[1] != ".png"):
            self.messageLabel2.SetLabel('暂不支持此类文件隐藏信息读取')
            return 0

        acc,data = read_control.readStart(path)
        if(acc):
            self.messageLabel2.SetLabel('读取成功!')
            self.dataOutput.SetValue(data)
        else:
            self.messageLabel2.SetLabel(data)


if __name__ == '__main__':
    app = wx.App()
    #main_win = MainWindow(None)
    login_win=LoginWindow(None)
    # register_win = RegisterWindow(None)
    # main_win.init_main_window()
    # main_win.Show()
    login_win.Show()
    app.MainLoop()
