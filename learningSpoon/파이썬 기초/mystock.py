#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 23:41:47 2020

@author: user
"""

def get_upper(price):
    return price * 1.3

def get_lower(price):
    return price * 0.7

print(__name__) #__main__ (이 파일을 직접 실행하면 이 문자열이 찍힘), mystock(다른 파일에서 이 파일을 import해서 실행시키면 파일 이름이 찍힘)

if (__name__ == "__main__"):    
    print(get_upper(10000)) 
    print(get_lower(10000))
    