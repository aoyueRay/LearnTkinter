#-*- coding:utf-8 -*-

import Tkinter as tk

def click_me():
    print('别点了。。别点了。。。')

root = tk.Tk()
root.title('Button')

var = tk.StringVar()
var.set('点我啊！！')

photo = tk.PhotoImage(file='songjihyo.gif')

the_button = tk.Button(root,
                       text='点我点我',
                       textvariable=var,  # 文本变量，优先级高于text
                       image=photo,    # 图片
                       command=click_me,    # 调用方法
                       activebackground='green',    # Buttom处于活动状态时的背景色
                       activeforeground='white',    # Buttom处于活动状态时的前景色
                       anchor=tk.NW,    # 文本或图像在Button中的位置 N NE E SE S SW W NW CENTER
                       bg='pink',    # 背景色
                       fg='blue',    # 前景色
                       bd=10,    # 边框宽度
                       padx=10,  # 水平方向，内容与边框的距离
                       pady=10,  # 垂直方向，内容与边框的距离
                       compound=tk.CENTER,  # 指定图像在文本的位置，CENTER时文本显示在图像上 BOTTOM LEFT RIGHT TOP
                       cursor='heart',    # 鼠标在Button上飘过时的样式
                       # default=tk.DISABLED,    # NORMAL时，会被绘制成默认按钮。NORMAL DISABLE
                       font='bold',    # 字体
                       disabledforeground='grey',    # Button不可用时的前景色
                       # height=10,    # Button的高度
                       # width=10,    # Button的宽度
                       highlightbackground='blue',  # Button没有获得焦点时高亮边框颜色
                       highlightcolor='red',  # Button获得焦点时高亮边框颜色
                       highlightthickness=5,  # 指定高亮边框的宽度
                       justify=tk.CENTER,  # 多行文本对齐方式LEFT RIGHT CENTER
                       relief=tk.RAISED,  # 边框的样式 SUNKEN RAISED GROOVE RIDGE 默认FLAT
                       overrelief=tk.FLAT,    # 鼠标飘过时，Button的样式。不设置时默认为relief的样式
                       repeatdelay=1000,    # 重复延迟。重复延迟时间后，按重复时间间隔持续触发按钮时间。
                       repeatinterval=300,    # 重复间隔。持续按下按钮时，按一定的时间间隔触发按钮事件。
                       state=tk.NORMAL,  # 指定Button的状态 NORMAL ACTIVE DISABLED
                       takefocus=True,  # 指定使用Tab键可将焦点移到Button上。
                       underline=0,  # 下划线，为1时表示第二个字符位置处标注下划线
                       # wraplength=100,    # 决定Button文本分为多少行，指定每行的长度，单位时屏幕单元
                       )
move_button = tk.Button(root,text='我是用来转移焦点的！')
the_button.pack()
move_button.pack()



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