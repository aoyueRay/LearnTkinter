#-*- coding:utf-8 -*-

# Radiobutton，单选按钮，用于实现多选一的问题
# 为了实现‘单选‘的行为，必须确保一组中所有按钮的variable选项均对应同一个变量，并用value指定按钮的值

import Tkinter as tk

root = tk.Tk()

BEAUTY = [
    ('貂蝉',1),
    ('西施',2),
    ('王昭君',3),
    ('杨玉环',4),
]

def callback():
    print 'callback!'

options = tk.IntVar()
beauty_var = tk.IntVar()

rb1 = tk.Radiobutton(root,text='One',variable=options,value=1)
rb1.pack(anchor=tk.W)
rb2 = tk.Radiobutton(root,text='Two',variable=options,value=2)
rb2.pack(anchor=tk.W)
rb3 = tk.Radiobutton(root,text='Three',variable=options,value=3)
rb3.pack(anchor=tk.W)
rb4 = tk.Radiobutton(root,text='Four',variable=options,value=4)
rb4.pack(anchor=tk.W)
rb5 = tk.Radiobutton(root,text='Five',variable=options,value=5)
rb5.pack(anchor=tk.W)

# 按钮选项较多时，通过循环的方式初始化按钮
for beauty,var in BEAUTY:
    tk.Radiobutton(root,
                   text=beauty,    # 按钮显示的文本
                   variable=beauty_var,    # 按钮的变量，每一组中的按钮续保持一致
                   value=var,    # 按钮的值
                   command=callback,    # 按钮相应函数
                   # indicatoron=False,    # 是否绘制按钮前的方框
                   ).pack(anchor=tk.W)

def delete_select():
    """
    取消按钮的选中状态
    :return:
    """
    rb3.deselect()

def flash():
    """
    刷新Radiobutton组件，在ACTIVE和NORMAL状态中切换
    :return:
    """
    rb1.flash()

def select():
    """
    将Radiobutton设置为选中状态
    :return:
    """
    rb3.select()

tk.Button(root,text='Delete',command=delete_select).pack()
tk.Button(root,text='Flash',command=flash).pack()
tk.Button(root,text='Choose NO.3',command=select).pack()
tk.Button(root,text='Exit',command=root.quit).pack()

root.mainloop()