#-*- coding:utf-8 -*-

import Tkinter as tk
import time

class show_clock():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Clock')

        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        self.label_time = tk.Label(self.root,text=current_time)
        self.label_time.pack()

    def update_clock(self):
        c_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.label_time.config(text=c_time)
        self.root.update()
        self.label_time.after(1000,self.update_clock)

if __name__ == '__main__':
    print __name__
    sc = show_clock()
    sc.update_clock()
    sc.root.mainloop()