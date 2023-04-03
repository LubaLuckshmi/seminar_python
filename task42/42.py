'''
Два различных натуральных числа n и m называются дружественными, 
если сумма делителей числа n (включая 1, но исключая само n) равна 
числу m и наоборот. Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных чисел, каждое из 
которых не превосходит k. Программа получает на вход одно натуральное 
число k, не превосходящее 10 ** 5. Программа должна вывести  все пары 
дружественных чисел, каждое из которых не превосходит k. Пары необходимо
выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую пару не дает).
'''
def sum_of_div(input_number):
    sum_result = 0
    for i in range(1, input_number//2 + 1):
        if input_number % i == 0:
            sum_result += i
    return sum_result

def friendly_nums(input_num):
    find = set()
    for i in range (1, input_num + 1):
        sum_temp_number = sum_of_div(i)
        sum2 = sum_of_div(sum_temp_number)
        if sum2 == i and sum_temp_number != i and i not in find and sum_temp_number not in find:
            print(sum_temp_number, i)
            find.add(i)


input_k = int(input("Введите число K: "))

friendly_nums(sum_of_div(input_k))