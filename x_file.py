#-*- coding:utf-8 -*-

import Tkinter as tk
import time
import MySQLdb

class x_file(object):

    root = tk.Tk()
    root.title('X File!')

    # 初始化血压脉搏参数
    diastolic_db = 0.0
    systolic_db = 0.0
    pulse_db = 0.0
    diastolic_1_db = 0.0
    diastolic_2_db = 0.0
    diastolic_3_db = 0.0
    diastolic_4_db = 0.0
    diastolic_5_db = 0.0
    diastolic_6_db = 0.0
    systolic_1_db = 0.0
    systolic_2_db = 0.0
    systolic_3_db = 0.0
    systolic_4_db = 0.0
    systolic_5_db = 0.0
    systolic_6_db = 0.0
    pulse_1_db = 0.0
    pulse_2_db = 0.0
    pulse_3_db = 0.0
    pulse_4_db = 0.0
    pulse_5_db = 0.0
    pulse_6_db = 0.0

    # 初始化体重参数
    weight = tk.IntVar()  # 体重
    frame_weight = tk.LabelFrame(root, text='体重', padx=10, pady=10)
    weight_e = tk.Entry(frame_weight, width=5)

    # 初始化日期参数
    date_str = ''



    def __init__(self):
        """
        初始化数据库
        DB:myHealthData
        table:my_health_data
        """
        try:
            self.conn = MySQLdb.connect(
                host = 'localhost',
                user = 'root',
                passwd = '433280',
                db = 'myHealthData',
                charset = 'utf8',
                use_unicode = True
            )
            self.cur = self.conn.cursor()
        except MySQLdb.Error as err:
            print('唉呀，连接数据库出错了！')
            print('Error %d : %s ' % (err.args[0], err.args[1]))

    def closeDB(self):
        """
        关闭数据库游标
        :return:
        """
        self.cur.close()
        self.conn.close()
        return None

    def blood_pressure_frame(self):
        def command_calculate():
            diastolic_1 = dia_e_1.get() if dia_e_1.get() else 0
            diastolic_2 = dia_e_2.get() if dia_e_2.get() else 0
            diastolic_3 = dia_e_3.get() if dia_e_3.get() else 0
            diastolic_4 = dia_e_4.get() if dia_e_4.get() else 0
            diastolic_5 = dia_e_5.get() if dia_e_5.get() else 0
            diastolic_6 = dia_e_6.get() if dia_e_6.get() else 0
            systolic_1 = sy_e_1.get() if sy_e_1.get() else 0
            systolic_2 = sy_e_2.get() if sy_e_2.get() else 0
            systolic_3 = sy_e_3.get() if sy_e_3.get() else 0
            systolic_4 = sy_e_4.get() if sy_e_4.get() else 0
            systolic_5 = sy_e_5.get() if sy_e_5.get() else 0
            systolic_6 = sy_e_6.get() if sy_e_6.get() else 0
            pulse_1 = pulse_e_1.get() if pulse_e_1.get() else 0
            pulse_2 = pulse_e_2.get() if pulse_e_2.get() else 0
            pulse_3 = pulse_e_3.get() if pulse_e_3.get() else 0
            pulse_4 = pulse_e_4.get() if pulse_e_4.get() else 0
            pulse_5 = pulse_e_5.get() if pulse_e_5.get() else 0
            pulse_6 = pulse_e_6.get() if pulse_e_6.get() else 0

            self.diastolic_1_db = float(diastolic_1)
            self.diastolic_2_db = float(diastolic_2)
            self.diastolic_3_db = float(diastolic_3)
            self.diastolic_4_db = float(diastolic_4)
            self.diastolic_5_db = float(diastolic_5)
            self.diastolic_6_db = float(diastolic_6)
            self.systolic_1_db = float(systolic_1)
            self.systolic_2_db = float(systolic_2)
            self.systolic_3_db = float(systolic_3)
            self.systolic_4_db = float(systolic_4)
            self.systolic_5_db = float(systolic_5)
            self.systolic_6_db = float(systolic_6)
            self.pulse_1_db = float(pulse_1)
            self.pulse_2_db = float(pulse_2)
            self.pulse_3_db = float(pulse_3)
            self.pulse_4_db = float(pulse_4)
            self.pulse_5_db = float(pulse_5)
            self.pulse_6_db = float(pulse_6)

            # 将计算机过保留小数点后两位
            temp_diastolic = float('%.2f' % ((int(diastolic_1) + int(diastolic_2) + int(diastolic_3)
                                              + int(diastolic_4) + int(diastolic_5) + int(diastolic_6))
                                             / 6.0))
            temp_systolic = float('%.2f' % ((int(systolic_1) + int(systolic_2) + int(systolic_3)
                                             + int(systolic_4) + int(systolic_5) + int(systolic_6)
                                             ) / 6.0))
            temp_pulse = float('%.2f' % ((int(pulse_1) + int(pulse_2) + int(pulse_3)
                                          + int(pulse_4) + int(pulse_5) + int(pulse_6)
                                          ) / 6.0))

            self.diastolic_db = temp_diastolic
            self.systolic_db = temp_systolic
            self.pulse_db = temp_pulse

            average_diastolic.set(temp_diastolic)
            average_systolic.set(temp_systolic)
            average_pulse.set(temp_pulse)

            print '搞定了搞定了~！'

        # diastolic_1 = tk.IntVar()    # 舒张压-1
        # diastolic_2 = tk.IntVar()    # 舒张压-2
        # diastolic_3 = tk.IntVar()    # 舒张压-3
        # systolic_1 = tk.IntVar()    # 收缩压-1
        # systolic_2 = tk.IntVar()    # 收缩压-2
        # systolic_3 = tk.IntVar()    # 收缩压-3
        # pulse_1 = tk.IntVar()    # 脉搏-1
        # pulse_2 = tk.IntVar()    # 脉搏-2
        # pulse_3 = tk.IntVar()    # 脉搏-3
        average_diastolic = tk.IntVar()  # 平均值-1
        average_systolic = tk.IntVar()  # 平均值-2
        average_pulse = tk.IntVar()  # 平均值-3

        frame_blood_pressure = tk.LabelFrame(self.root,text='血压脉搏',padx=5,pady=5)
        frame_blood_pressure.grid(row=0,column=0,padx=10,pady=10)

        tk.Label(frame_blood_pressure, text='舒张压:').grid(row=1, column=0)
        tk.Label(frame_blood_pressure, text='收缩压:').grid(row=2, column=0)
        tk.Label(frame_blood_pressure, text='脉  搏:').grid(row=3, column=0)
        tk.Label(frame_blood_pressure, text='平均值').grid(row=0, column=7)
        tk.Label(frame_blood_pressure, text='  1  ').grid(row=0, column=1)
        tk.Label(frame_blood_pressure, text='  2  ').grid(row=0, column=2)
        tk.Label(frame_blood_pressure, text='  3  ').grid(row=0, column=3)
        tk.Label(frame_blood_pressure, text='  4  ').grid(row=0, column=4)
        tk.Label(frame_blood_pressure, text='  5  ').grid(row=0, column=5)
        tk.Label(frame_blood_pressure, text='  6  ').grid(row=0, column=6)

        dia_e_1 = tk.Entry(frame_blood_pressure,width=5)
        sy_e_1 = tk.Entry(frame_blood_pressure,width=5)
        pulse_e_1 = tk.Entry(frame_blood_pressure,width=5)

        dia_e_2 = tk.Entry(frame_blood_pressure,width=5)
        sy_e_2 = tk.Entry(frame_blood_pressure,width=5)
        pulse_e_2 = tk.Entry(frame_blood_pressure,width=5)

        dia_e_3 = tk.Entry(frame_blood_pressure,width=5)
        sy_e_3 = tk.Entry(frame_blood_pressure,width=5)
        pulse_e_3 = tk.Entry(frame_blood_pressure,width=5)

        dia_e_4 = tk.Entry(frame_blood_pressure, width=5)
        sy_e_4 = tk.Entry(frame_blood_pressure, width=5)
        pulse_e_4 = tk.Entry(frame_blood_pressure, width=5)

        dia_e_5 = tk.Entry(frame_blood_pressure, width=5)
        sy_e_5 = tk.Entry(frame_blood_pressure, width=5)
        pulse_e_5 = tk.Entry(frame_blood_pressure, width=5)

        dia_e_6 = tk.Entry(frame_blood_pressure, width=5)
        sy_e_6 = tk.Entry(frame_blood_pressure, width=5)
        pulse_e_6 = tk.Entry(frame_blood_pressure, width=5)

        average_e_diastolic = tk.Entry(frame_blood_pressure,
                                       state='readonly',
                                       textvariable=average_diastolic,
                                       width=5)
        average_e_systolic = tk.Entry(frame_blood_pressure,
                                      state='readonly',
                                      textvariable=average_systolic,
                                      width=5)
        average_e_pulse = tk.Entry(frame_blood_pressure,
                                   state='readonly',
                                   textvariable=average_pulse,
                                   width=5)

        dia_e_1.grid(row=1, column=1)
        dia_e_2.grid(row=1, column=2)
        dia_e_3.grid(row=1, column=3)
        dia_e_4.grid(row=1, column=4)
        dia_e_5.grid(row=1, column=5)
        dia_e_6.grid(row=1, column=6)
        sy_e_1.grid(row=2, column=1)
        sy_e_2.grid(row=2, column=2)
        sy_e_3.grid(row=2, column=3)
        sy_e_4.grid(row=2, column=4)
        sy_e_5.grid(row=2, column=5)
        sy_e_6.grid(row=2, column=6)
        pulse_e_1.grid(row=3, column=1)
        pulse_e_2.grid(row=3, column=2)
        pulse_e_3.grid(row=3, column=3)
        pulse_e_4.grid(row=3, column=4)
        pulse_e_5.grid(row=3, column=5)
        pulse_e_6.grid(row=3, column=6)
        average_e_diastolic.grid(row=1, column=7)
        average_e_systolic.grid(row=2, column=7)
        average_e_pulse.grid(row=3, column=7)

        button_calculate = tk.Button(frame_blood_pressure, text='算一下', command=command_calculate)
        button_calculate.grid(row=4, column=7)

    def weight_frame(self):
        """
        体重区域
        :return:
        """

        self.frame_weight.grid(row=0,column=1,padx=10,pady=10)

        tk.Label(self.frame_weight,text='体重:',padx=10,pady=10).grid(row=0,column=0)
        tk.Label(self.frame_weight, text='kg').grid(row=0, column=2)

        self.weight_e.grid(row=0,column=1)

    def date_time_frame(self):
        """
        日期区域
        :return:
        """

        date = tk.StringVar()

        frame_date = tk.LabelFrame(self.root,text='日期',padx=10,pady=10)
        frame_date.grid(row=0,column=2,padx=10,pady=10)
        tk.Label(frame_date,textvariable=date).grid(row=0,column=0)

        current_time = time.localtime(time.time())
        self.date_str = time.strftime('%Y-%m-%d', current_time)
        date.set(self.date_str)

    def operator_frame(self):

        def save_datas():
            self.weight = float(self.weight_e.get())    # 体重

            sql = 'insert into my_health_data (key_date,diastolic,systolic,pulse,weight,' \
                  'diastolic_1,diastolic_2,diastolic_3,diastolic_4,diastolic_5,diastolic_6,' \
                  'systolic_1,systolic_2,systolic_3,systolic_4,systolic_5,systolic_6,' \
                  'pulse_1,pulse_2,pulse_3,pulse_4,pulse_5,pulse_6)' \
                  ' values ("%s","%f","%f","%f","%f","%f","%f","%f","%f","%f","%f",' \
                  '"%f","%f","%f","%f","%f","%f","%f","%f","%f","%f","%f","%f")' % \
                  (self.date_str,self.diastolic_db,self.systolic_db,self.pulse_db,self.weight,
                   self.diastolic_1_db,self.diastolic_2_db,self.diastolic_3_db,self.diastolic_4_db,
                   self.diastolic_5_db,self.diastolic_6_db,self.systolic_1_db,self.systolic_2_db,
                   self.systolic_3_db,self.systolic_4_db,self.systolic_5_db,self.systolic_6_db,
                   self.pulse_1_db,self.pulse_2_db,self.pulse_3_db,self.pulse_4_db,self.pulse_5_db,self.pulse_6_db)
            print sql
            try:
                count = 0
                count = self.cur.execute(sql)
                self.conn.commit()
            except MySQLdb.Error as err:
                print('新增记录的时候出错了。。。')
                print('Error %d : %s' % (err.args[0], err.args[1]))

            if count == 0:
                print('居然没有添加成功。。。')
            else:
                print('新增了%d条记录。' % count)

            print self.weight
            print self.date_str
            print 'save datas!'

        frame_operator = tk.LabelFrame(self.root)
        frame_operator.grid(row=0,column=3,padx=10,pady=10)

        button_quit = tk.Button(frame_operator,text='EXIT',command=self.root.quit)
        button_quit.grid(row=1,column=0,padx=10,pady=10)

        button_save = tk.Button(frame_operator,text='SAVE',command=save_datas)
        button_save.grid(row=0,column=0,padx=10,pady=10)

    def history_frame(self):

        frame_history = tk.LabelFrame(self.root,text='历史记录',padx=10,pady=10)
        frame_history.grid(row=1,column=0)

        tk.Label(frame_history,text='日  期').grid(row=0,column=0)
        tk.Label(frame_history,text='舒张压').grid(row=0,column=1)
        tk.Label(frame_history,text='收缩压').grid(row=0,column=2)
        tk.Label(frame_history,text='脉  搏').grid(row=0,column=3)
        tk.Label(frame_history,text='体  重').grid(row=0,column=4)

        # 历史数据变量-日期
        h_l_date_1,h_l_date_2,h_l_date_3 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_date_4,h_l_date_5,h_l_date_6 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_date_7,h_l_date_8 = tk.StringVar(),tk.StringVar()
        h_l_date_9,h_l_date_10 = tk.StringVar(),tk.StringVar()

        # 历史数据变量-舒张压
        h_l_diastolic_1,h_l_diastolic_2,h_l_diastolic_3 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_diastolic_4,h_l_diastolic_5,h_l_diastolic_6 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_diastolic_7,h_l_diastolic_8 = tk.StringVar(),tk.StringVar()
        h_l_diastolic_9,h_l_diastolic_10 = tk.StringVar(),tk.StringVar()

        # 历史数据变量-收缩压
        h_l_systolic_1,h_l_systolic_2,h_l_systolic_3 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_systolic_4,h_l_systolic_5,h_l_systolic_6 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_systolic_7,h_l_systolic_8 = tk.StringVar(),tk.StringVar()
        h_l_systolic_9,h_l_systolic_10 = tk.StringVar(),tk.StringVar()

        # 历史数据变量-脉搏
        h_l_pulse_1,h_l_pulse_2,h_l_pulse_3 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_pulse_4,h_l_pulse_5,h_l_pulse_6 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_pulse_7,h_l_pulse_8 = tk.StringVar(),tk.StringVar()
        h_l_pulse_9,h_l_pulse_10 = tk.StringVar(),tk.StringVar()

        # 历史数据变量-体重
        h_l_weight_1,h_l_weight_2,h_l_weight_3 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_weight_4,h_l_weight_5,h_l_weight_6 = tk.StringVar(),tk.StringVar(),tk.StringVar()
        h_l_weight_7,h_l_weight_8 = tk.StringVar(),tk.StringVar()
        h_l_weight_9,h_l_weight_10 = tk.StringVar(),tk.StringVar()

        # 历史记录-日期
        tk.Label(frame_history,textvariable=h_l_date_1).grid(row=1,column=0)
        tk.Label(frame_history,textvariable=h_l_date_2).grid(row=2,column=0)
        tk.Label(frame_history,textvariable=h_l_date_3).grid(row=3,column=0)
        tk.Label(frame_history,textvariable=h_l_date_4).grid(row=4,column=0)
        tk.Label(frame_history,textvariable=h_l_date_5).grid(row=5,column=0)
        tk.Label(frame_history,textvariable=h_l_date_6).grid(row=6,column=0)
        tk.Label(frame_history,textvariable=h_l_date_7).grid(row=7,column=0)
        tk.Label(frame_history,textvariable=h_l_date_8).grid(row=8,column=0)
        tk.Label(frame_history,textvariable=h_l_date_9).grid(row=9,column=0)
        tk.Label(frame_history,textvariable=h_l_date_10).grid(row=10,column=0)

        # 历史记录-舒张压
        tk.Label(frame_history, textvariable=h_l_diastolic_1).grid(row=1, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_2).grid(row=2, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_3).grid(row=3, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_4).grid(row=4, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_5).grid(row=5, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_6).grid(row=6, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_7).grid(row=7, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_8).grid(row=8, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_9).grid(row=9, column=1)
        tk.Label(frame_history, textvariable=h_l_diastolic_10).grid(row=10, column=1)

        # 历史记录-收缩压
        tk.Label(frame_history, textvariable=h_l_systolic_1).grid(row=1, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_2).grid(row=2, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_3).grid(row=3, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_4).grid(row=4, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_5).grid(row=5, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_6).grid(row=6, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_7).grid(row=7, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_8).grid(row=8, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_9).grid(row=9, column=2)
        tk.Label(frame_history, textvariable=h_l_systolic_10).grid(row=10, column=2)

        # 历史记录-脉搏
        tk.Label(frame_history, textvariable=h_l_pulse_1).grid(row=1, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_2).grid(row=2, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_3).grid(row=3, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_4).grid(row=4, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_5).grid(row=5, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_6).grid(row=6, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_7).grid(row=7, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_8).grid(row=8, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_9).grid(row=9, column=3)
        tk.Label(frame_history, textvariable=h_l_pulse_10).grid(row=10, column=3)

        # 历史记录-体重
        tk.Label(frame_history, textvariable=h_l_weight_1).grid(row=1, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_2).grid(row=2, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_3).grid(row=3, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_4).grid(row=4, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_5).grid(row=5, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_6).grid(row=6, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_7).grid(row=7, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_8).grid(row=8, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_9).grid(row=9, column=4)
        tk.Label(frame_history, textvariable=h_l_weight_10).grid(row=10, column=4)

        self.query_record()

    def query_record(self):

        sql = 'select * from my_health_data'
        count = 0    # 初始化计数器
        try:
            count = self.cur.execute(sql)
            self.conn.commit()
            results = self.cur.fetchall()
            for each in results:
                print each[0]
        except MySQLdb.Error as err:
            print('查询记录的时候出错了。。。')
            print('Error %s ' % err.args[0])

        if count == 0:
            print('什么都没有找到。。。')
        else:
            print('找到%d条记录。。。' % count)
        return None




if __name__ == '__main__':
    xfile = x_file()
    xfile.blood_pressure_frame()    # 血压脉搏
    xfile.date_time_frame()    # 日期
    xfile.weight_frame()    # 体重
    xfile.operator_frame()    # 操作区
    xfile.history_frame()    # 历史记录
    xfile.root.mainloop()
    xfile.closeDB()