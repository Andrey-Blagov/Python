# import this
# import math
# n = int(input("Введите скорость автомобиля: "))
# m = int(input("Введитие общее расстояние: "))


# print(math.ceil(m/n))

# print(m//n + (m % n > 0))

# print((m + n - 1) // n)


# x = int(input("Qty of student in 1 class: "))
# y = int(input("Qty of student in 2 class: "))
# z = int(input("Qty of student in 3 class: "))

# print(f"It is required to buy {(-(-x//2) - (-y//2) - (-z//2))} scool desks")
# print(f"It is required to buy {((x+1)//2) + ((y+1)//2) + ((z+1)//2))} scool desks")


# x = int(input("В какой сел: "))
# y = int(input("Сколько прошёл: "))

# if x == y:
#     print("Невозможно подсчитать колличество вагонов!")
# else:
#     print("Всего ", x + y - 1, " вагонов")


# year = int(input("Input the year to check: "))
# if year % 4 == 0 and year % 100 != 0:
#     print("YES")
# else:
#     print("NO")



# n = int(input())
# if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
#     print("год високосный")
# else:
#     print("год не високосный")




# n = 1900
# if n % 10 == 0:
#     if n // 10 % 10 == 0:
#         print('YES')
# else:
#     print('NO')
# n = int(str(input('Add number: ')))
# print(n + n)


# m = int(input())
# n = int(input())
# for i in range(m % 2 + m - 1, n - 1, -2):
#     print(i)

# from math import *
# n = 100   # int(input())
# total = 0
# for i in range(1, n + 1):
#     total = total + 1 / i
#     # print(total)
# print(total)
# print(log(n))
# print(total - log(n))


# Нахождение факториала

# n = input('Input number: ')
#
# while not n.isdigit() or n == '0':
#     print('Error input: ')
#     n = input('Input number: ')
#
# n = int(n)
# fact = 1
# count = 1
# while count <= n:
#     fact, count = fact * count, count + 1
# print(fact)

# n = int(n)
# fact = 1
#
# while n > 1:
#     fact *= n
#     n -= 1
#
# print(fact)


# Задача №11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
#
# Input:     21
#
# Output:  9
#
# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …

# a = input('Input number: ')
#
# while not a.isdigit() or a == '0' or a == '1':
#     print('Error input: ')
#     a = input('Input number: ')
#
# a = int(a)
#
# pos = 3
# p1 = 1
# p2 = 1
#
# while p1 < a:
#     p1, p2 = p1 + p2, p1
#     pos += 1

# pos = 3
# p1 = 1
# p2 = 1
#
# while p1 < a:
#     temp = p1
#     p1 = p1 + p2
#     p = temp
#     pos += 1

# if p1 != a:
#     print('-1')
# else:
#     print(pos)


# Задача №13 1) Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
#
# 2) Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. Нужно вывести наибольшее количество идущих подряд положительных чисел.
#
#
# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

# import random

# days_num = int(input('Input days: '))
#
# max_thaw_days = 0
# thaw_days = 0
#
# for i in range(days_num):
#     temperature = random.randint(-50,50)
#     print(temperature, end=' ')
#     if temperature > 0:
#         thaw_days += 1
#     else:
#         if thaw_days > max_thaw_days:
#             max_thaw_days = thaw_days
#         thaw_days = 0
# print()
# print(f'{max_thaw_days=}')


# days_num = int(input('Input days: '))
#
# max_thaw_days = 0
# thaw_days = 0
#
# for i in range(days_num):
#     temperature = random.randint(-50,50)
#     print(temperature, end=' ')
#     if temperature > 0:
#         thaw_days += 1
#         if thaw_days > max_thaw_days:
#             max_thaw_days = thaw_days
#     else:
#         thaw_days = 0
# print()
# print(f'{max_thaw_days=}')



# Задача №15. Пользователь вводит одно число N.
# Далее идут N чисел, записанных на новой строчке каждое.
# Вывести максимальное и минимальное (циклы)
# Input:	5 -> 5 1 6 5 9

# num = int(input('Enter a number: '))
# min_weight = 1000
# max_weight = 0

# for _ in range(num):
#     weight = int(input('Enter a number: ', end=' '))

#     if weight > max_weight:
#         max_weight = weight

#     if weight < min_weight:
#         min_weight = weight

# print()
# print(min_weight, max_weight)


# 2
# from random import randint
#
# num = randint(1, 20)
# weight = randint(5, 15)
# print(weight, end=' ')
# min_weight = weight
# max_weight = weight
#
# for _ in range(num - 1):
#     weight = randint(5, 15)
#     print(weight, end=' ')
#     max_weight = max(max_weight, weight)
#     min_weight = min(min_weight, weight)
#
# print()
# print(min_weight, max_weight)

# num = 21111
# x = num % 10
#
# while num >= 1:
#     last_digit = num % 10
#     if last_digit == x:
#         num = num // 10
#     else:
#         print('NO')
#
#
# print('YES')

# x = 0
# y = 0
#
# for i in range(2, p + 1):
#     if p % i == 0:
#         y = p / i
#         x = i
#         if x + y == s and x <= y:
#             print(int(x), int(y))

# solutions = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solutions.append((min(i, j), max(i, j)))
# solutions = list(set(solutions))
#
# for solution in solutions:
#     print(solution[0], solution[1])




