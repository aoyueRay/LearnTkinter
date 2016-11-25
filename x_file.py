#-*- coding:utf-8 -*-

import Tkinter as tk
import time

class x_file(object):

    root = tk.Tk()
    root.title('X File!')

    def blood_pressure(self):
        def command_calculate():
            diastolic_1 = dia_e_1.get() if dia_e_1.get() else 0
            diastolic_2 = dia_e_2.get() if dia_e_2.get() else 0
            diastolic_3 = dia_e_3.get() if dia_e_2.get() else 0
            systolic_1 = sy_e_1.get() if sy_e_1.get() else 0
            systolic_2 = sy_e_2.get() if sy_e_2.get() else 0
            systolic_3 = sy_e_3.get() if sy_e_3.get() else 0
            pulse_1 = pulse_e_1.get() if pulse_e_1.get() else 0
            pulse_2 = pulse_e_2.get() if pulse_e_2.get() else 0
            pulse_3 = pulse_e_3.get() if pulse_e_3.get() else 0

            # 将计算机过保留小数点后两位
            temp_diastolic = float('%.2f' % ((int(diastolic_1) + int(diastolic_2) + int(diastolic_3)) / 3.00))
            temp_systolic = float('%.2f' % ((int(systolic_1) + int(systolic_2) + int(systolic_3)) / 3.00))
            temp_pulse = float('%.2f' % ((int(pulse_1) + int(pulse_2) + int(pulse_3)) / 3.00))
            average_diastolic.set(temp_diastolic)
            average_systolic.set(temp_systolic)
            average_pulse.set(temp_pulse)
            # average_e_diastolic.insert(0,temp_diastolic)
            # average_e_systolic.insert(0,temp_systolic)
            # average_e_pulse.insert(0,temp_pulse)
            print '搞定了搞定了~！'

        # diastolic_1 = tk.StringVar()    # 舒张压-1
        # diastolic_2 = tk.StringVar()    # 舒张压-2
        # diastolic_3 = tk.StringVar()    # 舒张压-3
        # systolic_1 = tk.StringVar()    # 收缩压-1
        # systolic_2 = tk.StringVar()    # 收缩压-2
        # systolic_3 = tk.StringVar()    # 收缩压-3
        # pulse_1 = tk.StringVar()    # 脉搏-1
        # pulse_2 = tk.StringVar()    # 脉搏-2
        # pulse_3 = tk.StringVar()    # 脉搏-3
        average_diastolic = tk.StringVar()  # 平均值-1
        average_systolic = tk.StringVar()  # 平均值-2
        average_pulse = tk.StringVar()  # 平均值-3

        tk.Label(self.root, text='舒张压:').grid(row=1, column=0)
        tk.Label(self.root, text='收缩压:').grid(row=2, column=0)
        tk.Label(self.root, text='脉  搏:').grid(row=3, column=0)
        tk.Label(self.root, text='平均值:').grid(row=0, column=4)

        dia_e_1 = tk.Entry(self.root)
        sy_e_1 = tk.Entry(self.root)
        pulse_e_1 = tk.Entry(self.root)

        dia_e_2 = tk.Entry(self.root)
        sy_e_2 = tk.Entry(self.root)
        pulse_e_2 = tk.Entry(self.root)

        dia_e_3 = tk.Entry(self.root)
        sy_e_3 = tk.Entry(self.root)
        pulse_e_3 = tk.Entry(self.root)

        average_e_diastolic = tk.Entry(self.root, state='readonly', textvariable=average_diastolic)
        average_e_systolic = tk.Entry(self.root, state='readonly', textvariable=average_systolic)
        average_e_pulse = tk.Entry(self.root, state='readonly', textvariable=average_pulse)

        dia_e_1.grid(row=1, column=1, padx=10, pady=5)
        dia_e_2.grid(row=1, column=2, padx=10, pady=5)
        dia_e_3.grid(row=1, column=3, padx=10, pady=5)
        sy_e_1.grid(row=2, column=1, padx=10, pady=5)
        sy_e_2.grid(row=2, column=2, padx=10, pady=5)
        sy_e_3.grid(row=2, column=3, padx=10, pady=5)
        pulse_e_1.grid(row=3, column=1, padx=10, pady=5)
        pulse_e_2.grid(row=3, column=2, padx=10, pady=5)
        pulse_e_3.grid(row=3, column=3, padx=10, pady=5)
        average_e_diastolic.grid(row=1, column=4, padx=10, pady=5)
        average_e_systolic.grid(row=2, column=4, padx=10, pady=5)
        average_e_pulse.grid(row=3, column=4, padx=10, pady=5)

        b1 = tk.Button(self.root, text='算一下', comman=command_calculate).grid(row=4, column=2, padx=10, pady=5)
        b2 = tk.Button(self.root, text='走了走了', comman=self.root.quit).grid(row=4, column=3, padx=10, pady=5)

    def date_time(self):
        date = tk.StringVar()
        tk.Label(self.root,textvariable=date).grid(row=0,column=0)

        current_time = time.localtime(time.time())
        date_str = time.strftime('%Y-%m-%d', current_time)
        date.set(date_str)


if __name__ == '__main__':
    xfile = x_file()
    xfile.blood_pressure()
    xfile.date_time()
    xfile.root.mainloop()