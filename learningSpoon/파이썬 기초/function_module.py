#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:36:47 2020

@author: user
"""


"""함수"""
print("*" * 20)

def 프린트(string, num):
    print(string * num)
    #return None 이게 생략되 있는것임 
    
value = 프린트("3233", 4)
print(value)

if (value == None):
    print("value is none")


def average(a, b):
    return (a + b) / 2

print(average(2, 3))



"""모듈(라이브러리)"""
#모듈 = 파이썬 소스코드 파일
#파이썬 기본 모듈 - 파이썬 설치 경로에 기본 모듈들이 위치함

import datetime

cur_time = datetime.datetime.now()
print(cur_time, type(cur_time))

now = datetime.datetime.now()
tommorow = now + datetime.timedelta(days = 1)
print(now, tommorow)
now_str = str(now)
print(now_str[:19])


"""
import os 

flist = os.listdir("c:/Anaconda3")
print(flist)

for i in flist:
    if (i.endswith("exe")):
        print("실행파일이다.")
"""        
        
"""
#matplotlib/pyplot.py
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()
"""

""" import 방식 """
"""
import os -> os.listdir("C:/Anaconda3")
from os import listdir -> listdir("C:/Anaconda3")
from os import * -> listdir("C:/Anaconda3")
import os as myos -> myos.listdir("C:/Anaconda3")

2, 3번째 방식 잘 이용안함
from os import * 
from csv import *

a() 호출 했는데 둘다 a라는 함수가 있으면 어느걸 쓸지 판단못함 
"""
