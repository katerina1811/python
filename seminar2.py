# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# str_n = input('Введите число: ')
# str_n = str_n.replace('.', '').replace(',' , '')
# lst_str = list(str_n)
# lst_num = map(int, lst_str)
# s = sum(lst_num)
# print(s)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите число: '))
# pr = 1
# A = []
# for i in range(1, N + 1):
#     pr *= i
#     A.append(pr)

# print(A)

# Реализуйте алгоритм перемешивания списка.

# import random

# list = [2 , 5 , 7 , 18]
# print('Оригинальный список' + str(list))

# for i in range(len(list)-1, 0, -1):
#     r = random.randint(0, i + 1) 
#     list[i], list[r] = list[r], list[i]
# print('Перемешанный список' + str(list))    

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))