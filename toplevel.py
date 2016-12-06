#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

def create():
    top = tk.Toplevel(bg='pink')
    top.title('DOTA Teams')

    msg = tk.Message(top,text='Wings,LGD,EHOME,NewBee')
    msg.pack()

tk.Button(root,text='Create',command=create).pack()

root.mainloop()