#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

l = tk.Label(root,text='DOTA')

group = tk.LabelFrame(root,
                      bd=5,    # 边框宽度，默认2
                      fg='red',    # 指定LabelFrame文本颜色
                      height=1000,    # 高度
                      width=1000,   # 宽度
                      labelanchor=tk.NE,    # 控制文本在LabelFrame的显示位置，默认NW
                      labelwidget=l,    # 指定组件替代默认的Label，text存在时，忽略text属性
                      text='DOTA Team',
                      padx=50,    # 水平方向，内容与边框的间距
                      pady=50,    # 垂直方向，内容与边框的间距
                      relief=tk.RIDGE,    # 指定边框样式
                      )
group.pack(padx=10,pady=10)

var = tk.IntVar()
r1 = tk.Radiobutton(group,text='Wings',variable=var,value=1).pack(anchor=tk.W)
r2 = tk.Radiobutton(group,text='LGD',variable=var,value=2).pack(anchor=tk.W)
r3 = tk.Radiobutton(group,text='EHOME',variable=var,value=3).pack(anchor=tk.W)
r4 = tk.Radiobutton(group,text='LFY',variable=var,value=4).pack(anchor=tk.W)
r5 = tk.Radiobutton(group,text='IG.V',variable=var,value=5).pack(anchor=tk.W)
r5 = tk.Radiobutton(group,text='NewBee',variable=var,value=6).pack(anchor=tk.W)

def callback():
    print var.get()

tk.Button(group,text='Print',command=callback).pack()
tk.Button(group,text='Exit',command=root.quit).pack()


root.mainloop()