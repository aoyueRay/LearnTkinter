#-*- coding:utf-8 -*-

# Listbox，选择列表，智能包含文本项目，可从列表中选择一个或多个，列表的形式
# 创建Listbox组件时是空的，需要用insert()方法添加文本

import Tkinter as tk

root = tk.Tk()

BEAUTY = [
    '貂蝉',
    '西施',
    '王昭君',
    '杨玉环'
]

# 创建一个空列表
list_box = tk.Listbox(root)
list_box.pack()

# 往列表中添加数据
for each in BEAUTY:
    list_box.insert(tk.END,each)

def delete():
    """
    删除列表中的项目
    :return:
    """
    list_box.delete(0,tk.END)    # 删除列表项目，通过索引确定项目

tk.Button(root,text='Delete all',command=delete).pack()

# 删除指定项目，如下时删除装他为ACTIVE的项目
tk.Button(root,text='Delete Active',command=lambda x=list_box: x.delete(tk.ACTIVE)).pack()

tk.Button(root,text='Exit',command=root.quit).pack()


root.mainloop()
