# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# transformation = lambda i: i
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# lst = [1, 4, 6, 7, 8, 10, 12]
# print(lst)

# объяснение функций map, filter and lambda:

# filter
# def is_even(number):
#     return number % 2 == 0
#
#
# result = []
# for i in range(len(lst)):
#     if is_even(lst[i]):
#         result.append(lst[i])
#
# result_filter = list(filter(is_even, lst))
#
# result_filter_lambda = list(filter(lambda x: x % 2 == 0, lst))
#
# print(result)
# print(result_filter)
# print(result_filter_lambda)
#
#
# # map
# def get_square(number):
#     return number ** 2
#
#
# result2 = []
# for i in range(len(lst)):
#     result2.append(get_square(lst[i]))
#
# result_map = list(map(get_square, lst))
#
# result_map_lambda = list(map(lambda x: x ** 2, lst))
#
# print(result2)
# print(result_map)
# print(result_map_lambda)


# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# 1 optoin code:

# def find_farthest_orbit(orbits):
#     max = 1
#     index = 0
#     for i in range(len(orbits)):
#         lst = list(orbits[i])
#         if lst[0] * lst[1] > max and lst[0] != lst[1]:
#             max = lst[0] * lst[1]
#             index = i
#     return orbits[index]


# 2 optoin code:

# def find_farthest_orbit(orbits):
#     filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
#     squares = list(map(lambda orbit: orbit[0] * orbit[1], filtered_orbits))
#     maximum = max(squares)
#     result = list(filter(lambda orbit: orbit[0]*orbit[1] == maximum, filtered_orbits))
#     return result[0]
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# find_farthest_orbit(orbits)
#
# print(*find_farthest_orbit(orbits))

# 3 optoin code:

# def find_farthest_orbit(orbits):
#     filtered_orbits = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
#     return max(filtered_orbits, key=lambda orbit: orbit[0] * orbit[1])
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# find_farthest_orbit(orbits)
#
# print(*find_farthest_orbit(orbits))

# 4 option code:

# def find_farthest_orbit(orbits):
#     return max(filter(lambda orbit: orbit[0] != orbit[1], orbits),
#                key=lambda orbit: orbit[0] * orbit[1])
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# find_farthest_orbit(orbits)
#
# print(*find_farthest_orbit(orbits))


# dz task 2:
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row))



# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     lst = list(map(characteristic, objects))
#     n = len(set(lst))
#     return n == 1 or n == 0
#     # return len(set(lst)) in (0, 1)
#
#
# values = ['hello', 'pyton', [1, 2, 3, 4, 5]]
#
# if same_by(lambda x: len(x), values):
#     print('same')
# else:
#     print('different')

# values = [1, 7, 11, 13]
# lambda x: x % 2
#
# 15:26
# values = [3, 24, 60, 15]
# lambda x: x % 3



# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8,
#            2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# del numbers[0]
# del numbers[-1]
# print(numbers)


s_find = input()
s_finder = s_find.lower()
print(s_finder)



