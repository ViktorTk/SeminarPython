# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Outpit: 6

# ОБЫЧНЫЙ ВАРИАНТ РЕШЕНИЯ

# list_a = [1, 1, 2, 0, -1, 3, 4, 4]
# list_b = []

# for i in range(8):
#     c = 0
#     for j in range(i+1, 8):
#         if list_a[i] == list_a[j]:
#             c = 1
#             break
#     if c == 0: 
#         list_b.append(list_a[i])

# print(list_b)



# УПРОЩЕННЫЙ ВАРИАНТ РЕШЕНИЯ

list_a = [1, 1, 2, 0, -1, 3, 4, 4]

list_b = []
for i in list_a:
    if i in list_b:
        pass
    else:
        list_b.append(i)
        
print(list_b)
    






