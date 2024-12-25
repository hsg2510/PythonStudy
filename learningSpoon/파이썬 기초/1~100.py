#1 ~ 10(기초)
print("C:\\windows")  #C:\windows
print("안녕하세요\n반갑다.\tㅋㅋ")
print("오늘은","일요일")
print("naver", "kakao", sep=";")

print("first");print("second")
print("first", end="");print("second")


#21 ~ 30(문자열1)
letters = "홀짝홀짝홀짝"
print(letters[0:6:2]) #2는 offset, 2칸씩 건너띄어라
print(letters[::2])

string = "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace("-", ""))

url = "http://sharebook.kr"
split_url = url.split(".")
print(split_url[-1])

string = "abcd"
string.replace("b", "B")
print(string) #abcd 출력됨
string = string.replace("b", "B")
print(string) #aBcd 출력됨

#31 ~ 40(문자열2)
name1 = "김민수"
age1 = 10
name2 = "이민희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2)) #%f는 실수
print("이름: {} 나이: {}".format(name1, age1)) #python3 부터 사용 가능한 문법
print("이름: {} 나이: {}".format(name2, age2))
print(f"이름: {name1} 나이: {age1}") #python3.6 부터 사용 가능한 문법
print(f"이름: {name2} 나이: {age2}") 

data = "    삼성전자     "
data = data.strip()
print(data)

#41 ~ 50(문자열3)
a = "hello"
a = a.capitalize()
print(a)

file_name = "보고서.xlsx"
if (file_name.endswith(("xlsx", "xls"))):
    print("exel!!")

file_name = "2020_보고서.xlsx"
if (file_name.startswith("2020")):
    print("start with 2020!")

data = "  123  "
print(data.rstrip()) #오른쪽 공백만 제거
print(data.lstrip()) #왼쪽 공백만 제거

#61 ~ 70(리스트2)
interest = ["삼성전자", "LG전자", "Naver"]
result = "/".join(interest)
print(result)

data = [2, 4, 1, 0, -3, 10]
data.sort() #오름차순 정렬, 원본 변경됨.
print(data)

unsorted_data = [2, 4, 1, 0, -3, 10]
data2 = sorted(unsorted_data) #원본은 그대로 보존하고 정렬된 리스트를 반환
print(data2)

#71 ~ 80(튜플)
a = (1)
print(type(a))
a = (1,) #튜플인지 아닌지는 ","로 판단
print(type(a))
t = 1, 2, 3, 4
print(type(t))

tuple_value = ("apple", "babana", "mango")
a, b, c = tuple_value
print(a, b, c)

a = range(2, 99, 2)
t = tuple(a)
print(t)

#81 ~ 100(딕셔너리)
a, b, *c = [1, 2, 3, 4]
print(c)
*a, b, c = [1, 2, 3, 4]
print(a)
a, *b, c = [1, 2, 3, 4]
print(b)
_, *b, _ = [1, 2, 3, 4]
print(b)

icecream = { "빠삐코" : 100, "폴라포" : 120 }
new_product = { "아맛나" : 120, "팥빙수" : 1000 }
icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach")
values = (300, 120, 500)
#zip에게 두개의 리스트 또는 튜플을 주면 2개의 쌍을 묶어줌(type은 zip 이라는 type)
zip_value = zip(keys, values)
zip_value2 = zip(keys, values)
zip_value3 = zip(keys, values)
tuple_result = tuple(zip_value)
print(tuple_result) #(('apple', 300), ('pear', 120), ('peach', 500))
dict_result = dict(zip_value)
print(dict_result) #{} -> 뭔가 한번 zip 타입에서 다른 타입으로 변환이 되면, 값이 보존 안되고 다 지워지는듯?
dict_result = dict(zip_value2)
print(dict_result) #{'apple': 300, 'pear': 120, 'peach': 500}
list_result = list(zip_value2)
print(list_result) #-> 뭔가 한번 zip 타입에서 다른 타입으로 변환이 되면, 값이 보존 안되고 다 지워지는듯?
list_result = list(zip_value3)
print(list_result) #[('apple', 300), ('pear', 120), ('peach', 500)]
