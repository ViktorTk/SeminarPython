# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# input: a a a b c a a d c d d

# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2



# ПРИМЕР РЕШЕНИЯ

# st = ['a', 'b', 'c']
# i = 1
# h = ''
# for j in st:
#     h = h+ j +'_'+ str(i)
#     i = i + 1
# print(h)





# РЕШЕНИЕ ЗАДАЧИ

# text = input("Введите строку: ").split()
# print(text)
# newText = set(text)
# text_a = text
# for i in newText:
#     count = 0
#     text_b = []
#     for j in text_a:
#         if j == i:
#             text_b.append(i + '_' + str(count))
#             count+=1
#         else:
#             text_b.append(j)
#     text_a = text_b
# print(text_a)



# РЕШЕНИЕ ОТ ПРЕПОДАВАТЕЛЯ

text = input("Введите строку: ").split()
print(text)
textDict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
text1 = ''
for i in text:
    if i in textDict:
        text1 = text1 + i + '_' + str(textDict[i]) + ' '
        textDict[i] = textDict[i] + 1
    else:
        text1 = text1 + i + ' '
        textDict[i] = 1
print(text1)







