import numpy as np

"""ndarray"""

arr = [1, 2, 3, 4]
a = np.array(arr)
print(a)
print(type(a))

arr = [ [1, 2], [3, 4] ]
a = np.array(arr)
print(a)

a = np.zeros(3)
print(a) #[0. 0. 0.]
a = np.ones(3)
print(a) #[1. 1. 1.]
a = np.zeros((4, 3))
a = np.arange(5) #[0 1 2 3 4]
a = np.arange(1, 5) #[1 2 3 4]
a = np.arange(1, 5, 2) #[1, 3]

arr = [1, 2, 3, 4]
a = np.array(arr)
a = a.reshape(2, 2)
print(a) # [[1 2] [3 4]]

arr = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(arr)
result = arr.reshape(1, 8) #[[1 2 3 4 5 6 7 8]]
print(len(result)) #1
result = arr.reshape(8) #[1 2 3 4 5 6 7 8]
print(len(result)) #8


""" 
데이터 타입 
bool                                  ---- Boolean형
int8 / int16 / int32 / int64          ---- 정수형
unit8 / unit16 / unit32 / unit64      ---- 정수형
float8 / float16 / float32 / float64  ---- 부동소수형
complex64 / complex128                ---- 복소수형
string                                ---- 문자형

1Byte는 2^8개의 데이터 표현 가능 
-> 부호 있는 정수 : -128 ~ 127 표현
-> 부호 없는 정수 : 0 ~ 255 표현
-> 부호 있는 수는 최상위 비트를 MBS(부호 비트)로 사용, 1은 -를 뜻함 
-> 음수 표현은 2의 보수를 사용(1의 보수취한 후 1을 더함)
"""

a = np.zeros( (2, 3) )
print(a.dtype) #데이터 타입(float64)
print(a.shape) #몇행 몇열인지((2, 3))
print(a.ndim) #몇차원 배열인지(2)
print(a.itemsize) #데이터 타입의 메모리상에서 차지하는 바이트 크기(8)

a = np.array( [1, 2, 3, 4] )
print(a.dtype) #int64(os에 따라 달라지는 듯, int32일 수도 있고. int64일 수도 있다)
print(a.shape) #(4, ) -> 4행인데 1차원이기 때문에 열 정보가 비어있음
print(a.ndim) #1
print(a.itemsize) #8

a = np.zeros(3, dtype=np.int32)
print(a)
print(a.dtype)

a = np.zeros(3)
print(a.dtype)
a = np.int32(a) #형변환 방법1
print(a.dtype)
a = a.astype(np.int8) #형변환 방법2
print(a.dtype)