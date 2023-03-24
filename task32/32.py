# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

# 0, 1, 1, 2, 3, 5, 8, 13...

import time


def fibo_recursion(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fibo_recursion(num - 1) + fibo_recursion(num -2)



def fibo_iteration(num):
    first = 0
    second = 1
    if num == 1:
        return first
    if num == 2:
        return second
    
    count = 2
    while num != count:
        third =first + second
        first = second
        second = third
        count +=1
    return third

start = time.perf_counter()
print(fibo_recursion(15))
end = time.perf_counter()
first_time = end - start

start = time.perf_counter()
print(fibo_iteration(15))
end = time.perf_counter()
second_time = end - start

print(f"Метод быстрее в {round(first_time/second_time, 2)} раз(а)")