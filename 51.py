# Напшите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковые значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то Falseю Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:                                  Вывод:
# values = [0, 2, 10, 6]                 same
# if same_by(lambda x: x%2, values):
#     print('same')
# else:
#     print('different')


values = [0, 2, 10, 6]
def same_by(a, values):
    l = []
    for i in values:
        l.append(a(i))
    for i in l:
        if i==l[0]:
            pass
        else:
            return False
    return 1
if same_by(lambda x: x%2, values):
    print('same')
else:
    print('different')