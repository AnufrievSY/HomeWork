for i, value in enumerate(input().split(), 1):
    if len(value) > 10:
        print(i, value[:10])
    else:
        print(i, value)
