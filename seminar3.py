# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# numbers = [2, 3, 5, 9, 3]
# print(sum(numbers[1::2]))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# spisok = [2, 3, 4, 5, 6]
# result_sp = []
# for i in range((len(spisok)+1)//2):
#      result_sp.append(spisok[i]*spisok[len(spisok)-1-i])
# print(result_sp)

# Задайте список из вещественных чисел. Напишите программу, которая 
# найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# spisok = [1.1, 1.2, 3.1, 5, 10.01]
# max = 0
# min = 0
# for i in spisok:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i -int(i)) >= max:
#         max = i - int(i)
# print(max - min)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# print(bin(3))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

print('Введите k: ');     
k = int(input()) 
f1 = f2 = 1
print(f1, f2, end=' ')
i = 2
while i < k:
	f1, f2 = f2, f1 + f2 
	print(f2, end=' ') 
	i += 1
print()


