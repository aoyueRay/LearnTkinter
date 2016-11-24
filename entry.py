#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()
root.title('Entry')

tk.Label(root,text='V1:').grid(row=0)
tk.Label(root,text='V2:').grid(row=1)

v1 = tk.StringVar()    # 定义变量
v2 = tk.StringVar()
# v1.set('我是v1！')

# e1 = tk.Entry(root,textvariable=v1)
# e2 = tk.Entry(root,textvariable=v2)
# e1.pack()
# e2.pack()
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def show():
    v1 = e1.get()
    v2 = e2.get()
    print('V1:%s' % v1)
    print('V2:%s' % v2)
    e1.delete(0,tk.END)    # 删除输入框中的信息
    e2.delete(0,tk.END)

b1 = tk.Button(root,text='点我点我',comman=show).grid(row=2,column=0)
b1 = tk.Button(root,text='走了走了',comman=root.quit).grid(row=2,column=1)

# e2.insert(0,'我是v2啊！')

# e.insert(0,'Hello world!')
# s = e.get()



# print(s)

root.mainloop()