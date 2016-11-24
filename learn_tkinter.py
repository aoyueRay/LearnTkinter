#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

li_1 = ['C','python','php','html','SQL','java']
li_2 = ['CSS','jQuery','Bootstrap']

# 创建两个列表组件
listb_1 = tk.Listbox(root)
listb_2 = tk.Listbox(root)

# 在列表组件中插入数据
for each in li_1:
    listb_1.insert(0,each)
for each in li_2:
    listb_2.insert(0,each)

# 将列表组件放置到主窗口
listb_1.pack()
listb_2.pack()

# 进入消息循环
root.mainloop()