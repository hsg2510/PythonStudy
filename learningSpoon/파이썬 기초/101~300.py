# 111 ~ 130(분기문)
"""
data = input("숫자를 입력하세요")
print(data, type(data)) # 무엇을 입력하던 항상 문자열 타입으로 입력 받는다.
"""

data = 'a'

if (data.islower()):
    print(str.upper(data))
else:
    print(str.lower(data))

# 131 ~ 200(반복문)
for i in range(4) : #[0, 1, 2, 3]
    print(i)

# 201 ~ 240(함수)
def my_print(a, b):
    print("왼쪽 :", a)
    print("오른쪽 :", b)

my_print(a = 100, b = 200)
my_print(b = 100, a = 200)

# 241 ~ 250(모듈)
# import 모듈명 이라는 뜻은 모듈명에 정의되어 있는 코드를 한번 실행하라는 뜻

import datetime

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

day = "2020-08-02"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

import os

ret = os.getcwd()
print(ret, type(ret))

#os.rename("/Users/user/Desktop/before.txt", "/Users/user/Desktop/after.txt")

"""
import numpy

for i in numpy.arange(0, 5, 0.1):
    print(i)
"""

# 251 ~ 260(클래스1)
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지 말라.")

    def who(self):
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))

human = Human("홍성곤", 34, "남자")
human.who()
del human

"""
class OMG:
    def print():
        print("Oh My God")

myStock = OMG()
myStock.print() #인터프리터가 myStock.print(myStock) 으로 바꿔서 호출하기 때문에 실제 함수 정의는 파라미터가 없어서 에러가 남.
"""

# 261 ~ 270(클래스2)
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_code(self, name, code):
        self.name = name
        self.code = code

my_stock = Stock(None, None)
my_stock.set_code("삼성전자", "005930")
print(my_stock.name)
print(my_stock.code)

# 271 ~ 280(클래스3)
import random

class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_count(cls):
        return cls.account_count

    def deposit(self, amount):
        self.balance += amount

hong = Account("홍성곤", 10000000000)
print(hong.account_number)
lee = Account("이예지", 9999999999)
print(Account.get_account_count())

# 281 ~ 290(클래스4)
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수 ", self.바퀴)
        print("가격 ", self.가격)


car = 자동차(4, 1000)
car.정보()

class 부모:
    def __init__(self):
        print("부모생성")

    def 호출(self):
        print("부모호출")

class 자식(부모):
    def __init__(self):
        super().__init__()
        print("자식생성")

    def 호출(self):
        print("자식호출")

parent = 부모()
parent.호출()
child = 자식()
child.호출()

# 291 ~ 300(파일 입출력과 예외처리)
try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")

""" 에러발생시 에러 메시지를 변수로 바인딩
    try:
        실행코드
    except 예외 as 변수:
        예외처리코드
"""
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

"""
    try:
        실행 코드
    except:
        예외가 발생했을 때 수행할 코드
    else:
        예외가 발생하지 않았을 때 수행할 코드
    finally:
        예외 발생 여부와 상관없이 항상 수행할 코드
"""
per = ["10.31", "", "9.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변한 완료")