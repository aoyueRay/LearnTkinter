#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

var = tk.IntVar()

s1 = tk.Scale(root,from_ =0,    # 滑块顶端或左端的位置，默认0
              to=1000,   # 滑块右端或底端的位置，默认100
              resolution=2,    # 指定步长，默认1
              tickinterval=5,    # 指定刻度，默认不显示
              digits=3,    # 设置最多显示多少位数字，默认0-不开启
              fg='red',    # 左侧Label和刻度文字的颜色
              length=200,    # 滑块长度，默认100
              orient=tk.VERTICAL,  # 指定绘制水平滚动条(HORIZONTAL)或垂直滚动条(VERTICAL)，默认水平
              showvalue=True,    # 设置是否显示滑块旁的数字，默认True
              sliderlength=50,    # 设置滑块的长度，默认30像素
              sliderrelief=tk.FLAT,    # 设置滑块的样式
              # state=tk.DISABLED,    # 设置滑块是否支持鼠标事件和键盘事件，默认NORMAL
              troughcolor='green',    # 指定凹槽的颜色
              variable=var,    # 指定一个与组件关联的Tkinter变量
              width=30,    # 指定滑块的宽度,默认15
              bg='pink',    # 组件外部的背景颜色
              activebackground='blue',    # 鼠标在上方飘过时滑块的背景颜色
              )
s1.pack()
s2 = tk.Scale(root,from_=0,to=100,orient=tk.HORIZONTAL)
s2.pack()

def get():
    """
    获取滑块当前的位置
    :return:
    """
    r = s1.get()
    print r
    return r

def set():
    """
    设置滑块的值
    :return:
    """
    s2.set(90)

def show():
    r = var.get()
    print r
    return r

def identify():
    """
    返回字符串表示指定的位置下的部件
    :return:slider-滑块 trough1-左或上侧的凹槽 trough2-右或下侧的凹槽 ‘’-空
    """
    r = s1.identify(84,100)
    print r
    return r

def coords():
    """
    获取当前滑块位置对应Scale组件左上角的相对坐标
    :return:
    """
    r = s1.coords()
    print r
    return r

tk.Button(root,text='Get',command=get).pack()
tk.Button(root,text='Set',command=set).pack()
tk.Button(root,text='Show',command=show).pack()
tk.Button(root,text='Identify',command=identify).pack()
tk.Button(root,text='Coords',command=coords).pack()
tk.Button(root,text='Exit',command=root.quit).pack()

root.mainloop()