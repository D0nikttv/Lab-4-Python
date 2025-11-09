import numpy as np

item_s = {'r': (3,25),
        'p': (2,15),
        'a': (2,15),
        'm': (2,20),
        'k': (1,15),
        'x': (3,20),
        't': (1,25),
        'f': (1,10),
        's': (2,20),
        'c': (2,20),
        'i': (1,5)
        }

a ={'d': (1,10)}
start_points = 10
total_points = sum(value[1] for key, value in item_s.items())

def get_size_value(stuffdict) -> (int|int):
    size = [stuffdict[itm][0] for itm in stuffdict]
    value = [stuffdict[itm][1] for itm in stuffdict]
    return size, value

def get_memtable(stuffdict):
    size, value = get_size_value(stuffdict)
    n = len(value)

    table = np.array([[0 for _ in range(6+1)] for _ in range(n+1)])
     
    for row in range(n+1):
        for colmn in range(6+1):

            if row == 0 or colmn == 0:
                table[row][colmn] = 0
                    
            elif size[row-1] <= colmn:
                table[row][colmn] = max(table[row-1][colmn], value[row-1] + table[row-1][colmn - size[row - 1]])

            else: 
                table[row][colmn] = table[row-1][colmn]
    return table, size, value 

def get_selected_item_list(stuffdict, back=6):
    table, size, value = get_memtable(stuffdict)
    n = len(value)
    colmn = back
    res = table[n][colmn]

    item_list_size_value = []

    for i in range(n, 0, -1):
        
        if res <= 0:
            break

        if res == table[i-1][colmn]:
            continue

        else:
            item_list_size_value.append((size[i-1],value[i-1]))
            res -= value[i-1]
            colmn -= size[i-1]

    key_list = []
    for searh in item_list_size_value:
        for key, value_ in stuffdict.items():
            if searh == value_:
                key_list.append(key)
                stuffdict.pop(key)
                break

    return key_list, item_list_size_value



keys_values_list = get_selected_item_list(item_s)


keys = keys_values_list[0]+list(a.keys())
values = keys_values_list[1]+list(a.values())

d = {keys[i]:values[i] for i in range(len(keys))}

collected_points = sum(i[1] for i in values) + start_points
end_points = collected_points - (total_points - collected_points)

if end_points >= 0: 
    print(f'Итоговое количество очков: {end_points}\nУра! Это больше 0, мы смогли это сделать!')
else:
    print(f'Итоговое количество очков: {end_points}\nЭх, неудача.')   


print(f'Набор предметов для 7 ячеек: {d}')
