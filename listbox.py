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
list_box = tk.Listbox(root,
                      exportselection=False,    # 指定选中的文本项目是否可以被复制到剪切板，默认为True
                      height=8,    # 显示的行数，默认10
                      listvariable=BEAUTY,    # 指向StringVar类型的变量，存放listbox中所有的项目
                      selectmode=tk.EXTENDED,    # 指定选择模式，SINGLE，BROWSE，MULTIPLE，EXTENDED
                      setgrid=True,    # bool类型，指定是否启用网格控制，默认为False
                      # xscrollcommand,    # 添加水平滚动条，需要与ScrollBar组件关联
                      # yscrollcommand,    # 添加垂直滚动条，需要与ScrollBar组件关联
                      )
list_box.pack()

# 往列表中添加数据
for each in BEAUTY:
    list_box.insert(tk.END,each)

def activate():
    """
    将给定索引号对应的选项激活
    :return:
    """
    list_box.activate(3)

def delete():
    """
    删除列表中的项目
    :return:
    """
    list_box.delete(0,tk.END)    # 删除列表项目，通过索引确定项目

def cur_select():
    """
    返回被选中的选项的序号的元组
    :return:
    """
    r = list_box.curselection()
    print r
    return r

def get():
    """
    返回一个元组，包含参数范围内所有选项的元组
    :return:
    """
    r = list_box.get(1,2)
    print r[0]
    return r

def index():
    """
    返回参数相对应选项的序号
    :return:
    """
    r = list_box.index(2)
    print r
    return r

def nearest():
    """
    返回与给定参数y在垂直坐标上最接近的项目的序号
    :return:
    """
    r = list_box.nearest(1)
    print r
    return r

def selection_set():
    """
    设置参数范围内的选项为选中状态
    :return:
    """
    list_box.selection_set(2,3)

def selection_clear():
    """
    (first,last)
    取消参数范围内的选项的选中状态
    如果忽略后last参数，则只取消first参数指定选项的状态
    :return:
    """
    list_box.selection_clear(2,3)

def selection_includes():
    """
    返回参数指定选项的选中状态
    0-未选中，1-选中
    :return:
    """
    r = list_box.selection_includes(3)
    print r
    return r

tk.Button(root,text='Activate',command=activate).pack()
tk.Button(root,text='Delete all',command=delete).pack()
tk.Button(root,text='Cur Select',command=cur_select).pack()
tk.Button(root,text='Get',command=get).pack()
tk.Button(root,text='Index',command=index).pack()
tk.Button(root,text='Nearest',command=nearest).pack()
tk.Button(root,text='Selection Set',command=selection_set).pack()
tk.Button(root,text='Selection Clear',command=selection_clear).pack()
tk.Button(root,text='Selection Includes',command=selection_includes).pack()

# 删除指定项目，如下时删除装他为ACTIVE的项目
tk.Button(root,text='Delete Active',command=lambda x=list_box: x.delete(tk.ACTIVE)).pack()

tk.Button(root,text='Exit',command=root.quit).pack()


root.mainloop()
