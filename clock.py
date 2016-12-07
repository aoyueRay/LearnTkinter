#-*- coding:utf-8 -*-

import Tkinter as tk
import time,sys

root = tk.Tk()
root.title('Clock')
# root.minsize(500,500)    # 定义最小的窗口

current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
l1 = tk.Label(text=current_time)
l1.pack()

def update_clock():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    l1.config(text=current_time)
    root.update()
    l1.after(1000,update_clock)
l1.after(1000,update_clock)

root.mainloop()