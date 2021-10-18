from itertools import count
from math import factorial


def fact(n):
    end = n
    for i in count(1):
        if i == end:
            break
        else:
            yield factorial(i)


for result in fact(abs(int(input('Введите число: '))) + 1):
    print(result)



