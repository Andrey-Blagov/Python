# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# a = [2, 3, 5, 3, 4]
#
# max1 = max(a)
# min1 = min(a)
#
# for i in a:
#     if a[i] == max1:
#         a[i] = min1
#
# print(a)



# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# x = int(input())
# print('Yes' if is_prime(x) else 'No')



# Задача №37. Решение в группах
#
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def reverse(n):
#     string1 = input()
#     if n == 1:
#         return string1
#     return reverse(n - 1) + ' ' + string1
#
#
# n = int(input())
# print(reverse(n))

