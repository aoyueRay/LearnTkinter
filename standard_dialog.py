#-*- coding:utf-8 -*-

import Tkinter as tk
import tkMessageBox as tkmb
import tkFileDialog as tkfd
import tkColorChooser as tkcc


class message_box(tk.Frame):

    def __init__(self,root):

        # options for buttons
        options_button = {}
        options_button['padx'] = 5
        options_button['pady'] = 5
        options_button['width'] = 15

        tk.Button(root,text='OK-Cancel',command=self.ask_ok_cancel,**options_button).pack()
        tk.Button(root,text='Question',command=self.ask_question,**options_button).pack()
        tk.Button(root,text='Retry-Cancel',command=self.ask_retry_cancel,**options_button).pack()
        tk.Button(root,text='Yes-No',command=self.ask_yes_no,**options_button).pack()
        tk.Button(root,text='Yes-No-Cancel',command=self.ask_yes_no_cancel,**options_button).pack()
        tk.Button(root,text='Error',command=self.show_error,**options_button).pack()
        tk.Button(root,text='Info',command=self.show_info,**options_button).pack()
        tk.Button(root,text='Warning',command=self.show_warning,**options_button).pack()
        tk.Button(root,text='Exit',command=root.quit,**options_button).pack()

    def ask_ok_cancel(self):
        r1 = tkmb.askokcancel(title='OK-Cancel',message='OK or Cancel?',default=tkmb.OK)
        print r1
        return r1

    def ask_question(self):
        r2 = tkmb.askquestion(title='Question',message='Question?')
        print r2
        return r2

    def ask_retry_cancel(self):
        r3 = tkmb.askretrycancel(title='Retry-Cancel',message='Retry or Cancel?',default=tkmb.CANCEL)
        print r3
        return r3

    def ask_yes_no(self):
        r4 = tkmb.askyesno(title='Yes-No',message='Yes or No?',default=tkmb.YES)
        print r4
        return r4

    def ask_yes_no_cancel(self):
        r5 = tkmb.askyesnocancel(title='Yes-No-Cancel',message='Yes or No or Cancel?',default=tkmb.YES)
        print r5
        return r5

    def show_error(self):
        r6 = tkmb.showerror(title='Error',message='Error!')
        print r6
        return r6

    def show_info(self):
        r7 = tkmb.showinfo(title='Info',message='Info!')
        print r7
        return r7

    def show_warning(self):
        r8 = tkmb.showwarning(title='Warning',message='Warning!')
        print r8
        return r8

class file_dialog(tk.Frame):

    def __init__(self,root):

        # options for buttons
        options_button = {}
        options_button['padx'] = 5
        options_button['pady'] = 5
        options_button['width'] = 15

        # define options for opening or saving a file
        self.options_file = {}
        self.options_file['defaultextension'] = '.txt'    # 文件后缀
        self.options_file['filetypes'] = [('all files', '.*'), ('text files', '.txt')]    # 筛选文件类型
        self.options_file['initialdir'] = '/usr/projects/venv/learnTkinter'    # 默认路径
        self.options_file['initialfile'] = 'ljx.txt'    # 默认文件
        self.options_file['parent'] = root    # 对话框显示窗口
        # self.options_file['title'] = 'This is a title'    # 标题

        # defining options for opening a directory
        self.options_directory = {}
        self.options_directory['initialdir'] = '/usr/projects/venv/learnTkinter'
        self.options_directory['mustexist'] = False
        self.options_directory['parent'] = root
        # self.options_directory['title'] = 'This is a title'

        tk.Button(root, text='OpenFileName', command=self.open_file_name,**options_button).pack()
        tk.Button(root, text='OpenFile', command=self.open_file,**options_button).pack()
        tk.Button(root, text='Directory', command=self.directory,**options_button).pack()
        tk.Button(root, text='OpenFileNames', command=self.open_file_names,**options_button).pack()
        tk.Button(root, text='OpenFiles', command=self.open_files,**options_button).pack()
        tk.Button(root, text='SaveAsFile', command=self.save_as_file,**options_button).pack()
        tk.Button(root, text='SaveAsFileName', command=self.save_as_file_name,**options_button).pack()
        tk.Button(root, text='Exit', command=root.quit,**options_button).pack()

    def open_file_name(self):
        """
        打开一个文件名
        :return: 文件路径
        """
        r1 = tkfd.askopenfilename(title='FileOpenName',**self.options_file)
        # if r1:
        #     return open(r1,'r')
        print r1
        return r1

    def open_file(self):
        """
        打开一个文件
        :return: 文件对象
        """
        r2 = tkfd.askopenfile(mode='r',title='OpenFile',**self.options_file)
        print r2
        return r2

    def directory(self):
        """
        打开文件夹
        :return: 文件夹路径
        """
        r3 = tkfd.askdirectory(title='Directory',**self.options_directory)
        print r3
        return r3

    def open_file_names(self):
        """
        打开多个文件名
        :return: 文件路径
        """
        r4 = tkfd.askopenfilenames(title='OpenFileNames',**self.options_file)
        print r4
        return r4

    def open_files(self):
        """
        打开多个文件
        :return: 文件对象
        """
        r5 = tkfd.askopenfiles(title='OpenFiles',**self.options_file)
        print r5
        return r5

    def save_as_file(self):
        """
        保存文件
        defaultextension:指定文件后缀
        :return:文件对象
        """
        r6 = tkfd.asksaveasfile(defaultextension='.txt',title='SaveAsFile',**self.options_file)
        print r6
        return r6

    def save_as_file_name(self):
        """
        保存文件名
        :return: 文件路径
        """
        r7 = tkfd.asksaveasfilename(title='SaveAsFileName',**self.options_file)
        print r7
        return r7

class color_chooser(tk.Frame):

    def __init__(self,root):
        # options for buttons
        options_button = {}
        options_button['padx'] = 5
        options_button['pady'] = 5
        options_button['width'] = 15

        tk.Button(root,text='ColorChooser',command=self.choose_color,**options_button).pack()
        tk.Button(root,text='Exit',command=root.quit,**options_button).pack()

    def choose_color(self):
        """
        颜色选择对话框
        :return:(RGB颜色值，16进制颜色值) or (None,None)
        """
        r = tkcc.askcolor(title='ColorChooser')
        print r
        return r



if __name__ == '__main__':
    root = tk.Tk()

    options = {}
    options['padx'] = 10
    options['pady'] = 10

    mb_frame = tk.LabelFrame(root,text='Message Box',**options)
    fd_frame = tk.LabelFrame(root,text='File Dialog',**options)
    cc_frame = tk.LabelFrame(root,text='Color Chooser',**options)
    mb_frame.grid(row=0,column=0)
    fd_frame.grid(row=0,column=1)
    cc_frame.grid(row=0,column=2)

    fd = file_dialog(fd_frame)
    mb = message_box(mb_frame)
    cc = color_chooser(cc_frame)
    root.mainloop()