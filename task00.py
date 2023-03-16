'''
Вводятся числа, пока не введется 0. Найти сумму чисел, кратных 3.

summa = 0
while True:
    number = int(input())
    if number == 0:
        break
    elif number % 3 == 0:
        summa +=number
print(summa)


----------


number = int(input())
summa = 0
while number > 0:
    summa += number % 10
    number //= 10
print(summa)

----------

for letter in 'привет'
    print(letter)

-----------
Переменная - итерратор используется:
for i in range(1, 11):
    print(i ** 2)

Переменная - итерратор не используется:
for _ in range(5):
    print('Hello')

-------
a = 'hello'
for a in range(0, len(a), 2)
    print(a[i], end = '/n')
    '''

