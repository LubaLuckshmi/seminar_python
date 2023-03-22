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

    
-------
Списки

some_list = [1, '1', True, [1,2], {1,2}]
some_list.append(10)
some_list.insert(3,100)

for el in some_list:
    print(el)

------
Кортеж

some_touple = (1, 3 , 4 , 7 ,6)
print(list(some_touple))

------
Множества

some_set = { 1, 3, 4, 7, 9}

--------
import random

1. some_list = [random.randint(1, 50) for _ in range(100)]

2. some_list = []
for _ in range(100):
    some_list.append(random.randint(1,50))

1. print(40 in some_list)

2. for i in some_list:
       if i == 40:
           print(True)
           break
   else:
      print(False)

----------
some_list = {random.randint(1, 50) for _ in range(100)}

----------
словари

some_dict = {'name' : 'Alex', 'surname' : 'Ivanov'}
some_dict = {frozenset({1,2,3}) : 'Alex', 'surname' : 'Ivanov'}   

неизменяемые
int bool str float frozenset tuple

изменяемые
set list dict

some_dict = {'name' : 'Alex', 'surname' : 'Ivanov'}
print(some_dict['name'])
some_dict['age']= '21'
print(some_dict.get['adress', 'Такого ключа нет'])

print(some_dict.values()) список значений
print(some_dict.keys()) список ключей

-----------
вложенные списки

a = [1,2[3,4[5,6]]]
print(a[2][2][0]) #5

-----------
перевод значений в числа

a = ['1', '2', '3']
for ind in range(0, len(a)):
    a[ind] = int(a[ind])
print(a)

-----------
проверка словаря на ключ
a = {1: 2, 3: 4, 5: 6}
print(a.get(6, 'такого ключа нет'))

print(a.items())
for key, value in a.items():
    if value == 6:
    print(key)
--------------

задать рандомный список 
some_list = [random.randint(300,400) for _ in range (100)]


'''

