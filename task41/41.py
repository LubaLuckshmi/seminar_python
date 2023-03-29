'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг 
другу. Считается, что любые два элемента, равные друг другу образуют 
одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
'''

import random

def count_couple(input_list):
    find_couple = 0
    number_dict = {}
    for i in input_list:
        if i in number_dict:
            number_dict[i] += 1
        else:
            number_dict[i] = 1     
    for i in number_dict.values():
        find_couple += i // 2
    return find_couple


some_list = [random.randint(1, 20) for _ in range(10)]

print(some_list)
print(count_couple(some_list))