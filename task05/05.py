#В некоторой школе решили набрать три новых математических 
#класса и оборудовать кабинеты для них новыми партами. 
#За каждой партой может сидеть два учащихся.
#Известно количество учащихся в каждом из трех классов. 
#Выведите наименьшее число парт, которое нужно приобрести для них.

first = int(input("Введите количество учеников в первом классе: "))
second = int(input("Введите количество учеников во втором классе: "))
third = int(input("Введите количество учеников в третьем классе: "))

class1 = first // 2 + first % 2
class2 = second // 2 + second % 2
class3 = third // 2 + third % 2
sum = class1 + class2 + class3

print(f"Нужно приобрести {sum} парт")
