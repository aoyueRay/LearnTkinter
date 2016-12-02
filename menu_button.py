#-*- coding:utf-8 -*-

# MenuButton-与Menu组件相关联的按钮，可以放在任何位置，按下按钮后弹出菜单

import Tkinter as tk

root = tk.Tk()

def callback():
    print '啦啦啦，被调用啦～'

menu_button = tk.Menubutton(root,
                            text='点我啊！',    # 定义显示的文本
                            relief=tk.RAISED,
                            direction=tk.RIGHT,    # 定义菜单相对按钮的位置
                            )
menu_button.pack()

file_menu = tk.Menu(menu_button,tearoff=False)
file_menu.add_checkbutton(label='Open',command=callback,selectcolor='blue')
file_menu.add_command(label='Save',command=callback)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.quit)

menu_button.config(menu=file_menu)

root.mainloop()