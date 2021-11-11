my_list = list(input()[::-1])
a = len(my_list)
b = a - 2

new_list = list()

while a > 0:
    new_list.extend((my_list[b:a]))
    a = a - 2
    b = b - 2

if a % 2 == 1:
    i = my_list[:1]
    new_list.extend(i)

print(new_list)
