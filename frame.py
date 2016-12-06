#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

tk.Label(root,text='月黑风高夜').pack()

separator = tk.Frame(height=20,    # 设置frame的高度
                     bd=10,    # 指定frame边框宽度，默认为0
                     relief=tk.SUNKEN,    # 指定边框样式
                     container=True,    # 该窗口作为容器，用于嵌入其他应用程序，默认False
                     padx=100,    # 水平方向上的边距
                     pady=100,    # 垂直方向上的份额边距
                     width=2,    # 指定frame的狂度，默认为0
                     )
separator.pack(fill=tk.X)

tk.Label(root,text='杀人放火时').pack()

tk.Button(root,text="Exit",command=root.quit).pack()

root.mainloop()