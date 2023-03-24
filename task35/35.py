'''
Дан список интов, повторяющихся элементов в списке нет. 
Нужно преобразовать это множество в строку, сворачивая соседние 
по числовому ряду числа в диапазоны.

Примеры:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4"
'''
import random

def a(some_list):
    some_list.append(1.9)
    result_temp = []
    result = []
    for i in range(len(some_list) - 1):
        if some_list[i + 1] == some_list[i] + 1:
            result_temp.append(some_list[i])
        else:
            if some_list[i] not in result_temp:
                result_temp.append(some_list[i])
            result.append(result_temp)
            result_temp = []

    result_str = []
    for i in result:
        if len(i) >= 2:
            result_str.append(f"{i[0]} - {i[-1]}") 
        else:
            result_str.append(f"{i[0]}")
    return result_str

list1 = sorted({random.randint(1, 15) for _ in range(10)})
print(list1)

print(*a(list1), sep=', ')
