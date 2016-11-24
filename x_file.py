#-*- coding:utf-8 -*-

import Tkinter as tk

root = tk.Tk()
root.title('X File!')


tk.Label(root,text='舒张压:').grid(row=1,column=0)
tk.Label(root,text='收缩压:').grid(row=2,column=0)
tk.Label(root,text='脉  搏:').grid(row=3,column=0)
tk.Label(root,text='平均值:').grid(row=0,column=4)

dia_e_1 = tk.Entry(root)
dia_e_2 = tk.Entry(root)
dia_e_3 = tk.Entry(root)
sy_e_1 = tk.Entry(root)
sy_e_2 = tk.Entry(root)
sy_e_3 = tk.Entry(root)
pulse_e_1 = tk.Entry(root)
pulse_e_2 = tk.Entry(root)
pulse_e_3 = tk.Entry(root)
average_e_diastolic = tk.Entry(root)
average_e_systolic = tk.Entry(root)
average_e_pulse = tk.Entry(root)

diastolic_1 = tk.StringVar()    # 舒张压-1
diastolic_2 = tk.StringVar()    # 舒张压-2
diastolic_3 = tk.StringVar()    # 舒张压-3
systolic_1 = tk.StringVar()    # 收缩压-1
systolic_2 = tk.StringVar()    # 收缩压-2
systolic_3 = tk.StringVar()    # 收缩压-3
pulse_1 = tk.StringVar()    # 脉搏-1
pulse_2 = tk.StringVar()    # 脉搏-2
pulse_3 = tk.StringVar()    # 脉搏-3
average_diastolic = tk.StringVar()    # 平均值-1
average_systolic = tk.StringVar()    # 平均值-2
average_pulse = tk.StringVar()    # 平均值-3

dia_e_1.grid(row=1,column=1,padx=10,pady=5)
dia_e_2.grid(row=1,column=2,padx=10,pady=5)
dia_e_3.grid(row=1,column=3,padx=10,pady=5)
sy_e_1.grid(row=2,column=1,padx=10,pady=5)
sy_e_2.grid(row=2,column=2,padx=10,pady=5)
sy_e_3.grid(row=2,column=3,padx=10,pady=5)
pulse_e_1.grid(row=3,column=1,padx=10,pady=5)
pulse_e_2.grid(row=3,column=2,padx=10,pady=5)
pulse_e_3.grid(row=3,column=3,padx=10,pady=5)
average_e_diastolic.grid(row=1,column=4,padx=10,pady=5)
average_e_systolic.grid(row=2,column=4,padx=10,pady=5)
average_e_pulse.grid(row=3,column=4,padx=10,pady=5)

def calculate():
    diastolic_1 = dia_e_1.get()
    diastolic_2 = dia_e_2.get()
    diastolic_3 = dia_e_3.get()
    systolic_1 = sy_e_1.get()
    systolic_2 = sy_e_2.get()
    systolic_3 = sy_e_3.get()
    pulse_1 = pulse_e_1.get()
    pulse_2 = pulse_e_2.get()
    pulse_3 = pulse_e_3.get()
    temp_diastolic = (int(diastolic_1) + int(diastolic_2) + int(diastolic_3)) / 3.00
    temp_systolic = (int(systolic_1) + int(systolic_2) + int(systolic_3)) / 3.00
    temp_pulse = (int(pulse_1) + int(pulse_2) + int(pulse_3)) / 3.00
    average_e_diastolic.insert(0,temp_diastolic)
    average_e_systolic.insert(0,temp_systolic)
    average_e_pulse.insert(0,temp_pulse)
    print '搞定了搞定了~！'

b1 = tk.Button(root,text='算一下',comman=calculate).grid(row=4,column=2,padx=10,pady=5)
b2 = tk.Button(root,text='走了走了',comman=root.quit).grid(row=4,column=3,padx=10,pady=5)



root.mainloop()