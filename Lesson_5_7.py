import json

profit_dir = {}
profit_list = []
base_list = []

with open('L_5_7.txt', 'r') as base:
    for i in base.readlines():
        name, form_ownership, revenue, costs = i.split()
        profit = int(revenue) - int(costs)
        """Если """
        if profit >= 0:
            profit_dir[name] = profit
            profit_list.append(profit)
        else:
            profit_dir[name] = f'Убыток составил: {profit}'

    average_profit = {'Средняя прыбль': round(sum(profit_list) / len(profit_list))}

    base_list.append(profit_dir)
    base_list.append(average_profit)

with open('L_5_7.json', 'w') as new_file:
    json.dump(base_list, new_file)


