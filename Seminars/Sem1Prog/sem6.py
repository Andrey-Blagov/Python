# (пользовательский ввод можно заменить на рандомный ввод)
# Пользователь вводит  размер первого массива – N
# и элементы первого массива.
# затем размер второго массива M
# и элементы второго массива
# Нужно вывести те элементы первого массива, которых нет во втором массиве,
# при этом порядок последовательности сохранить исходный
# Ввод: 			Вывод:
# 7			3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# from random import randint
#
#
# def get_array(size):
#     # res = []
#     # for _ in range(size):
#     #     res.append(randint(0, 5))
#
#     return [randint(0, 5) for _ in range(size)]
#
#
# def arr_diff(array1, array2):
#     # res = []
#     # for num in array1:
#     #     if num not in array2:
#     #         res.append(num)
#     return [num for num in array1 if num not in array2]
#
#     # return [num if num not in array2 else 0 for num in array1]
#
#
# size_1 = int(input('Введите размер первого массива: '))
# size_2 = int(input('Введите размер второго массива: '))
#
# arr_1 = get_array(size_1)
# print(f'{arr_1=}')
# arr_2 = get_array(size_2)
# print(f'{arr_2=}')
#
# res_arr = arr_diff(arr_1, arr_2)
# print(*res_arr)


# (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа).
# нужно из этого массива вывести количество элементов,
# у которых ближайшие соседние элементы меньше самого элемента.
#
# Ввод: 			Ввод:
# 5			5
# 1 2 3 4 5			1 5 1 5 1
#
# Вывод:			Вывод:
# 0			2

# from random import randint
#
# size_arr_new = int(input('Введите размер массива: '))
#
# arr_new = [randint(0, 5) for _ in range(size_arr_new)]
#
# print(arr_new)
#
# count = 0
#
# for i in range(1, len(arr_new)-1):
#     if arr_new[i-1]<arr_new[i]>arr_new[i+1]:
#         count+=1
# print(count)
# #var2
# print(sum([1 for i in range(1, len(arr_new)-1) if arr_new[i-1]<arr_new[i]>arr_new[i+1]]))


# (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  размер массива – N
# и элементы массива (целые числа).
# нужно посчитать сколько повторений у каждого числа
# посчитанные числа можно посчитать повторно в паре с другими числами
#
# Ввод:			Вывод:
# 1 2 3 2 3 2			4

# arr_size = int(input('Введите размер массива: '))
# arr_new = [randint(0, 5) for _ in range(arr_size)]
# print(arr_new)
#
# # 1
# count = 0
# for i in range(arr_size - 1):
#     for j in range(i + 1, arr_size):
#         if arr_new[i] == arr_new[j]:
#             count += 1
#
# print(count)
#
# # 2
# count = 0
# for num in set(arr_new):
#     count_num = arr_new.count(num)
#     count += count_num * (count_num - 1) // 2
#
# print(count)


# 220 и 284. Найдём их делители
# Делители 220 – (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110)
# 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110  = 284
# Делители 284 – (1, 2, 4, 71, 142 )
# 1 + 2 + 4 + 71 + 142 = 220
# 			Ввод:			Вывод:
# 			300			220 284

# def get_sum_div(num):
#     sum_div = 1
#     for div in range(2, num):
#         if num % div == 0:
#             sum_div += div
#     return sum_div
#
#
# def check_friend_num(number):
#     for first_num in range(2, number):
#         second_num = get_sum_div(first_num)
#         if get_sum_div(second_num) == first_num and first_num < second_num:
#             print(first_num, second_num)
#
#
# k = int(input("Введите число: "))
# check_friend_num(k)


# семинар в 13-00

# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# import random
# a = int(input())
# b = int(input())
# list_1 = [0]*a
# list_2 = [0]*b
# answer = []
# for i in range(a):
#      list_1[i] = random.randint(1, 10)
# for i in range(b):
#     list_2[i] = random.randint(1, 10)
# print(list_1, list_2)
# for i in list_1:
#     if i not in list_2:
#         answer.append(i)
# print(*answer)


# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:
# 5
# 1 2 3 4 5
# Вывод:
# 0
#
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2

# lst = [1, 5, 1, 5, 1]
# count =0
# for i  in range (1,len(lst)-1):
#     if lst[i] > lst[i+1] and lst[i] > lst[i -1]:
#         count += 1
# print(count)


# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

# list_n = [1, 2, 3, 2, 3, 3, 3]
# count = 0
#
# for i in range(len(list_n) - 1):
#     for j in range(i + 1, len(list_n)):
#         if list_n[i] == list_n[j]:
#             count += 1
#
# print(count)


# var 2

# from collections import Counter
#
# list_n = [1, 2, 3, 2, 3, 3, 3]
# count = 0
#
# cnt = dict(Counter(list_n))
# print(cnt)
#
# for n in cnt.values():
#     count += (n * (n - 1)) // 2
#
# print(count)


# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300
# Вывод: 220 284

# def get_divisors_sum(number):
#     result = [1]
#     for divisors in range(2, number // 2 + 1):
#         if number % divisors == 0:
#             result.append(divisors)
#     return sum(result)
#
# k = int(input())
# st = set()
# for number in range(k + 1):
#     kandidat = get_divisors_sum(number)
#     if get_divisors_sum(kandidat) == number and kandidat != number:
#         st.add(tuple(sorted((number, kandidat))))
#
# for a, b in st:
#     print(a, b)

# a = 65  # int(input())
# b = 70  # int(input())
# # for i in range(a, b + 1):
# print([chr(i) for i in range(a, b + 1)])

# s = 'Hello world!'
# for i in range(len(s)):
#     print(ord(s[i]), end=' ')
# print()
# print(*[c for c in s], sep='\n')


s = [''1 2 3 4 5
