#-*- coding:utf-8 -*-

import Tkinter as tk
import tkMessageBox as tkmb
import tkFileDialog as tkfd
import tkColorChooser


# tkMessageBox
# r1 = tkmb.askokcancel(title='OK-Cancel',message='OK or Cancel?',default=tkmb.OK)
# r2 = tkmb.askquestion(title='Question',message='Question?')
# r3 = tkmb.askretrycancel(title='Retry-Cancel',message='Retry or Cancel?',default=tkmb.CANCEL)
# r4 = tkmb.askyesno(title='Yes-No',message='Yes or No?',default=tkmb.YES)
# r5 = tkmb.askyesnocancel(title='Yes-No-Cancel',message='Yes or No or Cancel?',default=tkmb.YES)
# r6 = tkmb.showerror(title='Error',message='Error!')
# r7 = tkmb.showinfo(title='Info',message='Info!')
# r7 = tkmb.showwarning(title='Warning',message='Warning!')

root = tk.Tk()

def open_file_name():
    """
    打开一个文件名
    :return: 文件路径
    """
    r1 = tkfd.askopenfilename(title='FileOpenName')
    print r1
    return r1

def open_file():
    """
    打开一个文件
    :return: 文件对象
    """
    # r2 = tkfd.askopenfile(mode='r',title='OpenFile')
    return tkfd.askopenfile(mode='r',title='OpenFile')
    # print r2
    # return r2

def directory():
    """
    打开文件夹
    :return: 文件夹路径
    """
    r3 = tkfd.askdirectory(title='Directory')
    print r3
    return r3

def open_file_names():
    """
    打开多个文件名
    :return: 文件路径
    """
    r4 = tkfd.askopenfilenames(title='OpenFileNames')
    print r4
    return r4

def open_files():
    """
    打开多个文件
    :return: 文件对象
    """
    r5 = tkfd.askopenfiles(title='OpenFiles')
    print r5
    return r5

def save_as_file():
    """
    保存文件
    defaultextension:指定文件后缀
    :return:文件对象
    """
    r6 = tkfd.asksaveasfile(defaultextension='.txt',title='SaveAsFile')
    print r6
    return r6

def save_as_file_name():
    """
    保存文件名
    :return: 文件路径
    """
    r7 = tkfd.asksaveasfilename(title='SaveAsFileName')
    print r7
    return r7

tk.Button(root,text='OpenFileName',command=open_file_name).pack()
tk.Button(root,text='OpenFile',command=open_file).pack()
tk.Button(root,text='Directory',command=directory).pack()
tk.Button(root,text='OpenFileNames',command=open_file_names).pack()
tk.Button(root,text='OpenFiles',command=open_files).pack()
tk.Button(root,text='SaveAsFile',command=save_as_file).pack()
tk.Button(root,text='SaveAsFileName',command=save_as_file_name).pack()
tk.Button(root,text='Exit',command=root.quit).pack()

root.mainloop()