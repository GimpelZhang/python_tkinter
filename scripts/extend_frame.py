# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
# Python 2.x使用这行
#from Tkinter import *
# Python 3.x使用这行
from tkinter import * 

# 定义继承Frame的Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 调用initWidgets()方法初始化界面
        self.initWidgets()
    def initWidgets(self):
        # 创建Label对象，第一个参数指定该Label放入root
        w = Label(self)
        # 创建一个位图
        bm = PhotoImage(file = './images/LOGO.png')
        # 必须用一个不会被释放的变量引用该图片，否则该图片会被回收
        w.x = bm
        # 设置显示的图片是bm
        w['image'] = bm
        w.pack()
        # 创建Button对象，第一个参数指定该Button放入root
        okButton = Button(self, text="确定")
#        okButton['background'] = 'yellow'
        okButton.configure(background='yellow')
        okButton.pack()
# 创建Application对象
app = Application()
# Frame有个默认的master属性，该属性值是Tk对象（窗口）
print(type(app.master))
# 通过master属性来设置窗口标题
app.master.title('窗口标题')
# 启动主窗口的消息循环
app.mainloop()
