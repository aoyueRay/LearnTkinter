#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()

text = tk.Text(root,width=20,height=20)
text.pack()

# 设置tag
text.tag_config('tag_1',background='pink',foreground='green')

text.insert(tk.INSERT,'Wings')
text.insert(tk.END,'NewBee','tag_1')

# 插入按钮
def callback():
    print 'Callback!'

b1 = tk.Button(text,text='Click!',command=callback)
text.window_create(tk.INSERT,window=b1)

root.mainloop()