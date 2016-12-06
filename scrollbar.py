#-*- coding:utf-8 -*-

import Tkinter as tk

# Listbox组件的可视范围发生改变时，Listbox通过调用set()通知Scrollbar
# 用户操作Scrollbar滚动条滚动时，自动调用Listbox的yview()方法

root = tk.Tk()

scroll = tk.Scrollbar(root,
                      activebackground='red',    # 鼠标划过时，滑块和箭头的背景颜色
                      activerelief=tk.FLAT,    # 鼠标划过时，滑块的样式
                      bg='yellow',    # 背景色
                      bd=1,    # 边框宽度
                      elementborderwidth=1,    # 指定滚动条和箭头饿边框宽度，默认-1
                      jump=False,    # 用户拖曳滚动条时的行为，默认为False
                      orient=tk.VERTICAL,    # 指定绘制水平滚动条(HORIZONTAL)或垂直滚动条(VERTICAL)，默认水平
                      repeatdelay=10,    # 指定鼠标左键点击滚动条凹槽的相应时间，默认300
                      repeatinterval=1000,    # 指定鼠标左键按紧滚动条凹槽的相应时间，默认100
                      troughcolor='white',    # 指定凹槽的颜色
                      )
scroll.pack(side=tk.RIGHT,fill=tk.Y)

listbox = tk.Listbox(root,yscrollcommand=scroll.set)
listbox.pack(side=tk.LEFT,fill=tk.BOTH)

for each in range(1000):
    listbox.insert(tk.END,str(each))

# 滚动条更新时的回调函数，通常为xview()或yview()方法
scroll.config(command=listbox.yview)    # 配置yview()方法

def set():
    """
    设置当前滚动条的位置
    :return:
    """
    location = (0.1,0.7)
    scroll.set(*location)


def get():
    """
    返回当前滑块的位置
    :return:
    """
    r = scroll.get()
    print r
    return r

tk.Button(root,text='Set',command=set).pack()
tk.Button(root,text='Get',command=get).pack()
tk.Button(root,text='Exit',command=root.quit).pack()

root.mainloop()