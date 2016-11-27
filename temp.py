#-*- coding:utf-8 -*-

from Tkinter import *

master = Tk()

group = LabelFrame(master, text="你从哪里得知鱼C？", padx=5, pady=5)
group.pack(padx=10, pady=10)

l1 = Label(group,text='User:').pack()
e1 = Entry(group).pack()

# v = IntVar()
# r1 = Radiobutton(group, text="同学/同事介绍", variable=v, value=1).pack(anchor=W)
# r2 = Radiobutton(group, text="老婆大人介绍", variable=v, value=2).pack(anchor=W)
# r3 = Radiobutton(group, text="老师/学长介绍", variable=v, value=3).pack(anchor=W)

mainloop()