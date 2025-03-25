def square(x):
    return x * x


a = (square(i) for i in range(5))
print(a)
a = list(a)
print(a)
