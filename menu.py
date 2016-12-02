#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()
root.title('Menu')

def callback():
    print '啦啦啦，被调用～'

def call_post():
    print 'I\'m postcommand!'


# 创建一个顶级菜单
main_menu = tk.Menu(root)

# 创建一个下拉菜单‘文件’，然后将它添加到顶级菜单中
file_menu = tk.Menu(main_menu,
                    tearoff=False,    # 值为True时，菜单可以被’撕下来‘
                    postcommand=call_post,    # 菜单被打开时，方法自动被调用
                    title='I\'m title!'    # 菜单被‘撕下来’时窗口的标题，默认与主菜单一致
                    )
file_menu.add_command(label='Open',command=callback)
file_menu.add_command(label='Save',command=callback)
file_menu.add_separator()    # 添加一条分割线
file_menu.add_command(label='Exit',command=root.quit)
main_menu.add_cascade(label='File',menu=file_menu)    # 添加一个父菜单

# 创建一个下拉菜单’编辑‘，然后将它添加到顶级菜单中
edit_menu = tk.Menu(main_menu,tearoff=False)
edit_menu.add_command(label='Cut',command=callback)
edit_menu.add_command(label='Copy',command=callback)
edit_menu.add_command(label='Paste',command=callback)
main_menu.add_cascade(label='Edit',menu=edit_menu)

# 创建一个多选按钮的菜单项
button_menu = tk.Menu(main_menu,tearoff=False,selectcolor='blue')
button_menu.add_checkbutton(label='CheckButton-1',command=callback)
button_menu.add_checkbutton(label='CheckButton-2',command=callback)
button_menu.add_checkbutton(label='CheckButton-3',command=callback)
button_menu.add_separator()
button_menu.add_radiobutton(label='RadioButton-1',command=callback)
button_menu.add_radiobutton(label='RadioButton-2',command=callback)
main_menu.add_cascade(label='Button',menu=button_menu)



# frame = tk.Frame(root,width=512,height=512)
# frame.pack()

def popup(event):
    # 将菜单弹出
    main_menu.post(event.x,event.y)

# # 绑定鼠标右键
# frame.bind('<Button-3>',popup)


# 显示菜单
root.config(menu=main_menu)


root.mainloop()