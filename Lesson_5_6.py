with open('L_5_6.txt', 'r') as base:
    for i in base.readlines():
        print(f"{i.split(':')[0]}"
              f": общее колличество часов - "
              f"{sum(map(int, ''.join([a for a in i.split(':')[1] if a == ' ' or '9' >= a >= '0']).split()))}")
