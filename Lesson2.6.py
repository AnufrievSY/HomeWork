base = []
base_analytics = {}
title_analytics = list()
price_analytics = list()
quantity_analytics = list()
u_m_analytics = list()
i = 0

while input('нажмите "ENTER", чтобы добавить новый продукт '
            'или введите "end", чтобы увидеть базу: ') != 'end':
    i += 1
    title = input('наименование товара: ')
    price = input('цена товара: ')
    quantity = input('колличество товара: ')
    u_m = input('единица измерения: ')

    base.append((i, {'название': title, 'цена': price, 'колличество': quantity, 'единица измерения': u_m}))

    if title_analytics.count(title) != 1:
        title_analytics.append(title)
    if price_analytics.count(price) != 1:
        price_analytics.append(price)
    if quantity_analytics.count(quantity) != 1:
        quantity_analytics.append(quantity)
    if u_m_analytics.count(u_m) != 1:
        u_m_analytics.append(u_m)

print('БАЗА ТОВАРОВ')
for j in base:
    print(j)

print('АНАЛИТИКА БАЗЫ')
base_analytics = {'название': title_analytics,
                  'цена': price_analytics,
                  'колличество': quantity_analytics,
                  'единица измерения': u_m_analytics}
for key, value in base_analytics.items():
    print(f'{key} - {value}')
