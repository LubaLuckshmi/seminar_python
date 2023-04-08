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

----------
интерполяция

print(a, '-', b, '-', c)
print('{1} - {0} - {2}'.format(a, b, c))
print(f'{a} - {b} - {c}')
/n #Перенос слова
/' #печатает '
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
Операции со множествами:

a = {1,2,3,5,8}
b = {2,5,8,13,21}
c = a.copy()     #c = {1,2,3,5,8}
u = a.union(b)   #u = {1,2,3,5,8,13,21}
i = a.intersection(b)  #i = {8, 2, 5}
dl = a.difference(b)   #dl = {1,3}
dr = b.difference(a)   #dr = {13,21}
q = a.union(b).difference(a.intersection(b)) #q = {1,21, 3,13}


----------
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

-------------
def square(a):
return a**2

some_list = [1, 2, 3, 4, 5]
print(list(map(square, some_list)))

for i in range(len(some_list)):
    some_list[i] = some_list[i] **2

-----------
def square(a):
return a**2

some_list = [1, 2, 3, 4, 5]
print(list(map(lambda a: a ** 2, some_list)))

------------
some_list = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x%2==0, some_list)))

map применяется к каждому обьекту
filter только ддля тех к которому применяется условие
lambda строчное написание простых функций

-----------
some_list = [1, 2, 3, 4, 5]
some_list2 = ['1', '2', '3', '4', '5']
print(list(zip(some_list, some_list2)))

for i, j in zip(some_list, some_list2):
    print(i,j)

обьединяет элементы списков в кортежи

-----------
some_list = [1, 2, 3, 4, 5]
print(list(enumerate(some_list)))

нумерует элементы списка с 0

-----------
создать кортеж число + его куб:
def f(x):
    return x**3

list = [(i, f(i)) for i in range(1,21) if i%2 ==0]
print(list)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data) #res = map(int, data)
res = where(lambda x: not x%2, res) #filter(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res) #res = list(map(lambda x: (x, x**2), res))
print(data)
print(res)

-----
data = list(map(int, input("Вводи числа через , ").split(","))) #Превращает список элементов в список чисел
print(data)

------
data = [x for x in range(10)]
res = list(filter(lambda x: not x%2, data))
print(res)
-----

with open('book.txt', 'w', encoding = 'utf-8') as f:
    f.write('фио | номер телефона)
-----
with open('book.txt', 'r', encoding = 'utf-8') as f:
    print(f.read())

    -----
with open('book.txt', 'a', encoding = 'utf-8') as f:
    f.write(\n'фио | номер телефона1)
-----
f. - короткое обращение к файлу
режимы
a - дозапись
r - чтение
w - записывает данные в файл
-------
'\n'.join - соединяет элементы списка по указанному вначале разделителю
.split('\n') разделяет
'''
