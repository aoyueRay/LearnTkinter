#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()
root.title('Entry')

tk.Label(root,text='V1:').pack()

v1 = tk.StringVar()    # 定义变量

def invalid():
    print 'Input invalid!'

def valid():
    print e1.get()
    if e1.get() == '123':
        print 'That\'s right!'
        return True
    else:
        print 'Wrong!'
        return False


e1 = tk.Entry(root,
              # bg='blue',    # 背景颜色
              bd=10,    # 边框宽度
              exportselection=False,    # 指定选中的文本是否可以被复制到剪切板
              fg='blue',    # 文本颜色
              insertbackground='red',   # 指定输入光标的颜色
              insertborderwidth=10,    # 指定输入光标边框的宽度
              insertofftime=10,    # 指定光标的闪烁频率-灭
              insertontime=10,    # 指定光标的闪烁频率-亮
              insertwidth=5,    # 指定光标的宽度
              invcmd=invalid,    # 指定输入非法时调用的函数
              justify=tk.RIGHT,    # 指定输入框中文本的对齐方式，默认LEFT
              relief=tk.FLAT,    # 指定边框样式，默认SUNKEN
              selectbackground='yellow',    # 指定输入框文本被选中时的背景颜色
              selectborderwidth=5,    # 指定输入框被选中时的边框宽度
              selectforeground='red',    # 指定输入框文本被选中时字体的颜色
              # show='$',    # 指定输入框如何显示文本内容
              # state='readonly',    # 指定组件的状态，readonly支持选中和拷贝，但不能修改
              takefocus=False,    # 指定使用Tab键移动焦点到输入框，False时避免焦点到输入框
              textvariable=v1,    # 指定与输入框相关联的变量
              validate='focusout',    # 指定是否启用内容验证，focus,focusin,focusout,key,all,none
              vcmd=valid,    # 指定用于验证输入框是否合法的函数
              width=50,    # 指定输入框的k宽度，默认20,字符为单位
              )
e1.pack()

def show():
    v1 = e1.get()
    print('V1:%s' % v1)
    e1.delete(0,tk.END)    # 删除输入框中的信息

def insert():
    """
    将text参数插入到index指定位置
    insert(INSERT,text)将text插入到光标指定位置
    insert(END,text)将text插入到末尾
    :return:
    """
    e1.insert(0,'hello!')

def selection_range():
    """
    指定选中范围
    selection_range(o,END)选中整个输入框
    :return:
    """
    e1.selection_range(1,3)

def selection_clear():
    """
    取消选中状态
    :return:
    """
    e1.selection_clear()

def selection_present():
    """
    返回输入框是否处于选中状态
    :return:1-选中，2-未选中
    """
    r1 = e1.selection_present()
    print r1
    return r1

def delete():
    """
    删除范围内的值
    :return:
    """
    e1.delete(0,tk.END)

tk.Button(root,text='Click Me',comman=show).pack()
tk.Button(root,text='Delete',comman=delete).pack()
tk.Button(root,text='Insert',comman=insert).pack()
tk.Button(root,text='Selection Range',comman=selection_range).pack()
tk.Button(root,text='Selection Clear',comman=selection_clear).pack()
tk.Button(root,text='Selection Present',comman=selection_present).pack()
tk.Button(root,text='Exit',comman=root.quit).pack()


root.mainloop()