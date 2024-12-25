#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 23:54:05 2020

@author: user
"""

class Stock:
    #pass #아무것도 정의하지 않을 때는 pass 키워드
    
    def __init__(self, 종목명):
        self.종목명 = 종목명
    
    def 출력(self): #메서드의 첫번째 인자는 무조건 self 이다. 
        print(self.종목명)
        
    def 입력(self, 종목명):
        self.종목명 = 종목명

"""
a = Stock()
a.종목명 = "삼성전자"
b = Stock()
b.종목명 = "LG전자"

Stock.출력(a)
a.출력() # interpreter가 Stock.출력(a)로 바꿔줌
b.출력()

c = Stock()
c.입력("네이버")
c.출력()
"""

d = Stock("씨젠")
d.출력()



"""상속"""
class Parent:
    def sing(self):
        print("sing a song")
        
class LuckyChild(Parent):
    def dance(self):
        print("shuffle dance")
        
luckyBoy = LuckyChild()
luckyBoy.sing()
luckyBoy.dance()


