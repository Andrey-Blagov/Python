# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# lst = [1, 2, 3, 4, 5]
# k = int(input())
# lst_1 = lst[:k]
# del lst[:k]
# lst.extend(lst_1)
# print(lst)
#
#
# lst = [1, 2, 3, 4, 5]
# lst1 = lst[0:3]
# lst2 = lst[3:5]
# print(lst1, lst2)
#
# k = 502
# if k >= len(lst):
#     k = k%len(lst)
# lst1 = lst[:k]
# lst2 = lst[k:]
# print(lst1, lst2)
# print(lst2 + lst1)


# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# st = set()
#
# for d in lst:
#     value = list(d.values())[0]
#     print(value)
#     st.add(value)
#
# print(st)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# lst = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(lst)):
#     if lst[i-1] < lst[i]:
#         count += 1
# print(count)


# dt = {
#     'A, E, I, O, U, L, N, S, T, R': 1,
#     'D, G': 2,
# }
#
# word = 'tuple'
#
# word = word.upper()
#
# for ch in word:
#     for key in dt.keys():
#         if ch in key:
#             print(dt[key])
#
# 'A, E, I, O, U, L, N, S, T, R'.split(', ') # -> список букв
# for ch in 'A, E, I, O, U, L, N, S, T, R'.split(', '):
# dt[ch] = 1



