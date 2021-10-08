a = [1, 2, 3]
b = (1, 2, 3)
c = set('set')
d = frozenset('frozenset')
e = {'key_1': 'value_1', 'key_2': 'value_2'}

my_list = ['t', 1, 1.2, None, True, a, b, c, d, e]
for i in my_list:
    print(type(i))
