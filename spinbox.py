#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

sb = tk.Spinbox(root,
                values=('Wings','LGD','EHOME','NewBee'))
sb.pack()

root.mainloop()