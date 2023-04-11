'''
A
abAcdeAfghijkAlmno
pqrsAcdeAAtuvwxyzA
ВЕЧЕР
о
Солнце низенько, вечiр близенько,
Вийди до мене, мое серденько!
ВЕЧЕР
'''


result = []
first_letter = input("Введите 1 символ: ")
stop = False
while not stop:
    input_str = input("Введите строку: ")
    if input_str == "ВЕЧЕР":
        stop = True
    part_list = input_str.split(first_letter)
    if len(part_list) > 1:
        result.append(part_list[1])

print(*set(result), sep='\n')