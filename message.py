#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

w1 = tk.Message(root,
                text='This is a message!',
                width=100
                )
w1.pack()

# 自动换行
w2 = tk.Message(root,text='This is a long long long long long long long message',
                width =100)
w2.pack()

root.mainloop()