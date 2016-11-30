#-*- coding:utf-8 -*-

import Tkinter as tk

class mouse_event(tk.Frame):

    def __init__(self,root):

        # options for buttons
        options_button = {}
        options_button['padx'] = 5
        options_button['pady'] = 5

        frame = tk.Frame(root,width=200,height=200,bd=2,relief=tk.SUNKEN,**options_button)
        frame.bind('<Button-1>',self.click_position)
        frame.grid(row=0,column=0)
        tk.Button(root,text='Exit',command=root.quit,width=15,**options_button).grid(row=1,column=0)

    def click_position(self,event):
        print('点击位置：%d,%d' % (event.x, event.y))

class key_event(tk.Frame):

    def __init__(self,root):

        # options for buttons
        options_button = {}
        options_button['padx'] = 5
        options_button['pady'] = 5

        frame = tk.Frame(root, width=200, height=200, bd=2, relief=tk.SUNKEN, **options_button)
        frame.bind('<Key>', self.key_position)
        frame.focus_set()
        frame.grid(row=0, column=0)
        tk.Button(root,text='Exit',command=root.quit,width=15,**options_button).grid(row=1,column=0)

    def key_position(self,event):

        print('按键对应字符：%s' % (repr(event.char))),
        print('按键名：%s' % (repr(event.keysym))),
        print('按键码：%s' % (repr(event.keycode))),
        print('事件产生的组件：%s' % (repr(event.widget))),
        print('事件类型：%s' % (repr(event.type)))
        print('鼠标位置(相对窗口)：%d,%d' % (event.x,event.y))
        print('鼠标位置(相对屏幕)：%d,%d' % (event.x_root,event.y_root))


class motion_event(tk.Frame):

    def __init__(self,root):

        # options for buttons
        options_button = {}
        options_button['padx'] = 5
        options_button['pady'] = 5

        frame = tk.Frame(root, width=200, height=200, bd=2, relief=tk.SUNKEN, **options_button)
        frame.bind('<Motion>', self.mouse_motion)
        frame.grid(row=0, column=0)
        tk.Button(root, text='Exit', command=root.quit,width=15, **options_button).grid(row=1, column=0)

    def mouse_motion(self,event):
        print('当前位置：%d,%d' % (event.x, event.y))

if __name__ == '__main__':
    root = tk.Tk()

    options = {}
    options['padx'] = 10
    options['pady'] = 10

    mouse_frame = tk.LabelFrame(root,text='Mouse Area',**options)
    key_frame = tk.LabelFrame(root,text='Keyboard Area',**options)
    motion_frame = tk.LabelFrame(root,text='Motion Area',**options)
    mouse_frame.grid(row=0,column=0)
    key_frame.grid(row=0,column=1)
    motion_frame.grid(row=0,column=2)

    mouse = mouse_event(mouse_frame)
    key = key_event(key_frame)
    motion = motion_event(motion_frame)

    root.mainloop()