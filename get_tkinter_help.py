#-*- coding:utf-8 -*-

import Tkinter
import sys

tmp = sys.stdout
fp = open('Tkinter.txt','w')
sys.stdout = fp    # 重定向stdout
help(Tkinter)
sys.stdout = tmp   # 重定向stdout
fp.close()