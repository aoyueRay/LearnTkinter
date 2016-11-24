#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()
root.title('Label')    # 窗口标题

long_text = """
这是一段很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
的文本！！！
"""
short_text = 'Hello World!'

# 显示变量的内容
var = tk.StringVar()
var.set('这是一个变量！')   # set方法设置变量内容
# var.set(long_text)   # set方法设置变量内容

# 显示图片内容(gif,bmp)
photo = tk.PhotoImage(file='songjihyo.gif')

# font 字体
the_Label = tk.Label(root,
                     textvariable=var,    # 文本变量，优先级高于text
                     text='我是text',  # 文本
                     image=photo,    # 图像
                     # bitmap=photo,    # 位图
                     fg='green',    # 前景色
                     bg='pink',    # 背景色
                     anchor=tk.W,    # 文本或图像在Label中的位置 N NE E SE S SW W NW CENTER
                     compound=tk.CENTER,    # 指定图像在文本的位置，CENTER时文本显示在图像上 BOTTOM LEFT RIGHT TOP
                     cursor = 'spider',    # 指定鼠标在Label上飘过时的样式
                     font=('Bold',20),    # 字体格式，字体大小
                     # height=400,    # Label的高度
                     # width=400,    # Label的宽度
                     highlightbackground='blue',    # Label没有获得焦点时高亮边框颜色
                     highlightcolor='red',    # Label获得焦点时高亮边框颜色
                     highlightthickness=5,    # 指定高亮边框的宽度
                     justify=tk.CENTER,    # 多行文本对齐方式LEFT RIGHT CENTER
                     padx=10,    # 水平方向，内容与边框的距离
                     pady=10,    # 垂直方向，内容与边框的距离
                     bd=5,  # 指定边框宽度
                     relief=tk.RAISED,    # 边框的样式 SUNKEN RAISED GROOVE RIDGE 默认FLAT
                     state=tk.NORMAL,    # 指定Label的状态 NORMAL ACTIVE DISABLED
                     activeforeground='yellow',    # Label处于活动状态时的前景色
                     activebackground='black',    # Label处于活动状态时的背景色
                     takefocus=True,    # 为True时接受输入焦点
                     underline=1,    # 下划线，为1时表示第二个字符位置处标注下划线
                     # wraplength=100,    # 决定Label文本分为多少行，指定每行的长度，单位时屏幕单元
                     )
the_Label.pack()

root.mainloop()

"""
cursor的样式：
    "arrow"

    "circle"

    "clock"

    "cross"

    "dotbox"

    "exchange"

    "fleur"

    "heart"

    "heart"

    "man"

    "mouse"

    "pirate"

    "plus"

    "shuttle"

    "sizing"

    "spider"

    "spraycan"

    "star"

    "target"

    "tcross"

    "trek"

    "watch"

"""