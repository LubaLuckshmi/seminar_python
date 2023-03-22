# 25. Напишите программу, которая принимает на вход строку, и 
# отслеживает количество повторов каждого символа.

input_str = input("Введите строку: ")
character_count = {}
for i in input_str:
    if i in character_count:
        character_count[i] += 1
    else:
        character_count[i] = 1

print(character_count)
