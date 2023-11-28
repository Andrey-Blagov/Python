# Задача №25.  Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# Kоличество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#Для решения данной задачи используйте функцию .split()

# input_data = 'a a a b c a a d c d d'
# input_list = input_data.split()

# 1 variant

# output = ''
# count_dict = {}
# for letter in input_list:
#     output += letter
#     if letter in count_dict:
#         count_dict[letter] += 1
#         output += f'_{count_dict[letter]}'
#     else:
#         count_dict[letter] = 0
#     output += ' '
#
#
# print('a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2')
# print(output)


# input_data = 'a a a b c a a d c d d'.split()
# result = {}
# for letter in input_data:
#     if letter in result:
#         print(f'{letter}_{result[letter]}', end=' ')
#     else:
#         print(letter, end=' ')
#     result[letter] = result.get(letter, 0) + 1


# input_data = 'a a a b c a a d c d d'.split()
# result = {}
# for letter in input_data:
#     print(f'{letter}{result.get(letter, "")}', end=' ')
#     result[letter] = result.get(letter, 0) + 1


# c = 'a a a b c a a d c d d'
# c = c.split()
# dt = {}
# for i in c:
#     if i not in dt:
#         dt[i] = 1 # /=0
#         print(i, end=' ')
#     else:
#         # print(F'{i}_{dt[i]}',  end=' ')
#         dt[i] = dt[i] + 1
#         print(F'{i}_{dt[i]-1}',  end=' ')



# Задача №27.  Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# text_string = '''She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''
# text1 = text_string.lower().split()
# print(len(set(text1)))


# text = "She sells sea shells on the sea shore The shells\
#  that she sells are sea shells I'm sure. So if she sells sea\
#  shells on the sea shore I'm sure that the shells are sea\
#  shore shells"
# words = text.lower().replace('.', ' ').split()
# st = set(words)
# print(len(st))

# print(len(set(words)))


# var2 = '1 3 5 7 9'
# var3 = '2 3 4 5'
#
# for i in var2:
#     if i in var3:
#         print(i, end='')



# var3 = var1.split()
# var4 = var2.split()
# var5 = var3 + var4

# for i in var5:
#     if var5[i]

# print(var3 + var4)
# print(var5[1])
# print(set(var5))






