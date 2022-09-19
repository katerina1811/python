# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = float(input('Введите степень точности в формате 0.0...  >> '))
# number = float(input('Введите число для округления в формате x.x...>>  '))

# dig_after = abs(str(d).find('.') - len(str(d)))
# print(str(number)[:-dig_after])

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число: '))
# deliteli = []

# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#      deliteli.append(i)

# print(f'Делители числа {n}: {deliteli}')

# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
# numbers = input('Введите числа через пробел:  ').split()

# num = []
# for i in range(len(numbers)):
#     if numbers[i] not in num:
#      num.append(numbers[i])

# print(num)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def file(st):
    with open('sem4.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
     wr = 'x = 0'
    else:
     for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
             wr += f'{lst[i]}x^{len(lst) - i - 1}'
             if lst[i + 1] != 0:
                wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                 wr += f'{lst[i]}x'
                 if lst[i + 1] != 0:
                     wr += ' + '
                 elif i == len(lst) - 1 and lst[i] != 0:
                  wr += f'{lst[i]} = 0'
                 elif i == len(lst) - 1 and lst[i] == 0:
                  wr += ' = 0'
     return wr


k = int(input("Введите натуральную степень k = "))
kof = create_mn(k)
file(create_str(kof))
