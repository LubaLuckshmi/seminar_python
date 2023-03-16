# 11. Дано натуральное число A > 1. Определите, каким по счету 
# числом Фибоначчи оно является, то есть выведите такое
# число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.

A = int(input("Введите натуральное число A "))
fib1 = 0
fib2 =1
temp_fibo = fib1+fib2
index =2
while temp_fibo < A:
    fib1 = fib2
    fib2 = temp_fibo
    temp_fibo = fib1+fib2
    index +=1
if temp_fibo == A:
    print(index+1)
else:
    print(-1)