#-*- coding:utf-8 -*-

# OptionMenu-下拉菜单的改版
# 一个*号用来打包和解包序列
# 两个*号用来打包和解包字典

import Tkinter as tk

OPTIONS = [
    'Ray',
    '433',
    'HZAU',
    'Hunan',
    "Chenzhou"
]

root = tk.Tk()

variable = tk.StringVar()
variable.set('Infos')

option_menu = tk.OptionMenu(root,variable,*OPTIONS)
option_menu.pack()


def callback():
    print(variable.get())    # 获取变量的值

tk.Button(root,text='Click me!',command=callback).pack()
tk.Button(root,text='Exit',command=root.quit).pack()
root.mainloop()