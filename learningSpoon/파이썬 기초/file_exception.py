#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:34:30 2020

@author: user
"""


"""파일 읽기"""
"""
f = open("C:/Users/hsg2510/Desktop/buy_list.txt", encoding="utf-8")
lines = f.readlines()
f.close()
print(lines)
"""

"""파일 쓰기"""
"""
f = open("C:/Users/hsg2510/Desktop/buy_list.txt", "wt", encoding="utf-8")
f.write("LG전자\n")
f.writelines("삼성전자")
f.close()
"""

"""예외 처리"""
per = "3.0"
print(float(per))

per = ""

try:
    per = float(per)
except:
    per = 0.0
    
print(per)


"""csv 파일 포맷으로 저장"""
data = [
        ("삼성전자", "005930", 10.0),
        ("LG전자", "000020", 15.0),
        ("네이버", "013930", 20.0),
        ]

f = open("/Users/user/Desktop/data.csv", "wt", encoding="cp949") #cp949는 윈도우에서 사용하는 인코딩 방식(엑셀, csv 등을 만들때는 이 방식으로 인코딩 해야됨)
f.write("{}, {}, {}\n".format(data[0][0], data[0][1], data[0][2]))
f.write("{}, {}, {}\n".format(data[1][0], data[1][1], data[1][2]))
f.write("{}, {}, {}".format(data[2][0], data[2][1], data[2][2]))
f.close()
