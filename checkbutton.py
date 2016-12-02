#-*- coding:utf-8 -*-

# Checkbutton通常被用做二选一的按钮，通常为选择开或管的状态

import Tkinter as tk

root = tk.Tk()

result = tk.StringVar()
result.set('False')

def callback():
    print 'variable is %s!' % result.get()

check_button = tk.Checkbutton(root,
                              text='I\'m a checkbutton',
                              variable=result,
                              command=callback(),
                              # indicatoron=False,    # 定义选择方块是否绘制，False时无选择方块，按钮会变化
                              onvalue='True',    # 默认情况下1-选中，0-未选中
                              offvalue='False',    # 可通过onvalue,offvalue修改值
                              selectcolor='blue',    # 选择时方框的颜色
                              )
check_button.pack()
check_button.var = result

tk.Button(root,text='Print',command=callback).pack()
tk.Button(root,text='Exit',command=root.quit).pack()



root.mainloop()