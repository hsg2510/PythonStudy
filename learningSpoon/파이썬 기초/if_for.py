# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""조건문"""
samsung = 51000

if (samsung > 50000):
    print("삼성전자 매수") #앞에 2칸이상(일반적으로 4칸, Tab) 들여쓰기 해야됨.
    
kospi = 2100
if (samsung >= 50000 and kospi > 2000):
    print("장 좋다")
elif (samsung < 30000 or kospi < 1000):
    print("장 무지 안좋다")
else:
    print("장 나쁘다")


"""반복문"""
카트 = ["고기", "오이", "음료수"]

for i in 카트:
    print(i)
    
for 물건 in 카트:
    print(물건)
    
dict1 = { "btc" : 142442, "xrp" : 342044 }

for i in dict1:
    print(i, dict1[i])  
    
for key, value in dict1.items():
    print(key, value)
    
for i in range(0, 5):
    print(i) #0 ~ 4까지 출력
    
rangeValue = range(0, 5)
print(type(rangeValue))
print(list(rangeValue))

for i in range(0, 10, 2): # start, end, step
    print(i) 
    
data = [
        ("삼성전자", 144289),
        ("LG전자", 174289),
        ("현대차", 174289),
        ("SK", 124289),
        ]
result = []

for i in data :
    if (i[1] > 150000) :
        result.append(i[0])

print(result)    
#break, continue 있음

num = 1

while (num < 5) :
    print(num)
    num += 1
    
"""
import time 

while True:
    print("돈 버는중")
    time.sleep(1) #1초, ctrl+c 눌러서 탈출 가
"""

import random 

lotto = []

while len(lotto) < 6 :    
    num = random.randint(1, 45) # 1~45중에 하나 뽑힘
    
    if (num not in lotto) :
        lotto.append(num)

print(lotto)        
