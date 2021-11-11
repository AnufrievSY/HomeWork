from functools import reduce

a_list = [a for a in range(100, 1001) if a % 2 == 0]
multiply_all = reduce(lambda x, y: x * y, a_list)
print(multiply_all)
