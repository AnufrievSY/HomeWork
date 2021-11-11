old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

a_list = iter(old_list)
new_list = [b for b in old_list[1:] if b > next(a_list)]
print(new_list)

