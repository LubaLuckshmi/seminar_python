'''Если ты много лет подряд был воином Белой розы, если ты не раз участвовал в
кровопролитных битвах между индейцами и бледнолицыми, если ты, наконец, был
разведчиком союзников во второй мировой войне, то ты научился двум вещам: ничему
не удивляться и уметь молчать, когда надо.

Напишите программу, которая найдет отличия между индейцами и бледнолицыми (или
Белой розой и Красной розой, кто их разберет).

Из каждых двух наборов целых чисел выбрать общие, оканчивающиеся на 1 или 3, без
повторений. Вывести в порядке убывания через & окруженный пробелами.

Формат ввода

вводится число п - количество наборов из двух строк, в которых целые
числа записаны
через пробел.

Затем 2 * п строк с целыми числами.

Формат вывода

вывести п строк, в которых записаны определенные по указанному
правилу числа через
&, окруженный пробелами.

Пример 1

Ввод. Вывод

з мазал
928 21 23 12 41

621 18 26 41 18 23 53 121 & 31
18425 31 15 22 м1

2 13 19 28 12
'''

n = int(input("Введите количество пар: "))
some_list = [[i for i in input("Введите числа через пробел: ").split()if i[-1] in ('1', '3')] for _ in range(2*n)]

#some_list = []
#for _ in range(2 * n):
 #   temp_list = []
  #  for i in input().split():
   #     if i[-1] in ('1', '3'):
    #        temp_list.append(i)
    #some_list.append(temp_list)
print(some_list)

for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind + 1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True), sep=' & ')