# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""문자열 인덱스 """
str1 = "abc"
print(str1[0])
print(str1[-1])
print(str1[-3])
str2 = "hello world"
print(str2[0:5])
print(str2[6:11])
print(str2[6:])
print(str2[:11])
print(str2[0:-5])
print(str2[-5:])
print(str2[:-6])


"""문자열 합치기 / 쪼개기"""
year = "2020"
month = "07"
day = "26"
print(year + "/" + month + "/" + day)

date = "2020/07/26"
date_split = date.split("/")
print(date_split)
print(type(date_split))

name = "KAKAO"
new_name = "T" + name[1:]
print(new_name)

"""문자열 replace / length / 공백제거"""
new_name2 = name.replace('K', 'T', 1) #K를 T로 1번 변경해라 
print(new_name2)
print(len(new_name2))
code = "  1234  "
print(code)
code = code.strip()
print(code)


"""리스트"""
stock_list = ["Samsung", "LG", "SK"]
print(stock_list[:2])
stock_list.append("씨젠")
print(stock_list)
stock_list.insert(2, "코나아이")
print(stock_list)
del stock_list[3]
print(stock_list)

a = [1, 2, 3]
print(max(a))
print(min(a))
print(sum(a))


"""튜플"""
"""수정 불가능(Immutable : append, insert, del 사용 불가능"""
코스피 = (1717, 1754, 1802, 2204)
print(코스피)
print(코스피[0], 코스피[1])
print(코스피[:2])
print(len(코스피))

"""unpacking"""
data = ("NAVER", 10, 1700000, (2020, 4, 4)) 
종목이름, 수량, 현재가, 날짜 = data
print(종목이름)

"""*"""
volume = (2245673, 3489493, 4329002, 4233444, 3249802)
last_vol, *trailing_vol = volume
print(last_vol)
print(trailing_vol)
"""리스트 타입임, 튜플 아님"""
print(type(trailing_vol)) 



"""형변환"""
"""int, string, float"""
str_val = "2"
int_val = int(str_val)
print(int_val)
float_val = float(str_val)
print(float_val)
str_val = str(float_val)
print(str_val)

"""리스트, 튜플"""
리스트1 = [10, 20, 30]
튜플1 = tuple(리스트1)
print(튜플1)
리스트1 = list(튜플1)
print(리스트1)


"""딕셔너리"""
"""mutable"""
현재가 = { "삼성전자" : 47000, "현대차" : 86300 }
print(현재가)
print(현재가["삼성전자"])
"""get() 메서드를 사용하면 key가 없는 경우 None을 리턴(Key로 접근했다가 없으면 에러가 발생함)"""
print(현재가.get("삼성전자"))
print(현재가.get("LG전자"))
del 현재가["현대차"]
print(현재가)
현재가["LG전자"] = 140000
print(현재가.keys())
print(type(현재가.keys()))
print(현재가.values())
print(type(현재가.values()))
print(sum(현재가.values()))
list_keys = list(현재가.keys())
list_values = list(현재가.values())
"삼성전자" in 현재가
