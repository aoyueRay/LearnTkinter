#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

w = tk.Canvas(root,width=200,height=200)
w.pack()

# 画一条黄色的横线
w.create_line(0,50,200,50,fill='yellow')

# 画一条红色的竖线-虚线
w.create_line(100,0,100,100,fill='red',dash=(4,4))

# 画一个粉色的矩形
w.create_rectangle(50,25,150,75,fill='pink')

root.mainloop()