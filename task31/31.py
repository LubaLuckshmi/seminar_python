#Создайте список из случайных чисел. Найдите второй максимум.

import random

#some_list = [random.randint(1, 100) for _ in range(10)]
some_list = list(set([10, 10, 8, 7, 6, 3]))
print(some_list)
first_max, second_max = some_list[0], some_list[0]

for i in some_list:
    if i > first_max:
        second_max = first_max
        first_max = i
    elif i > second_max:
        second_max = i

print(second_max)