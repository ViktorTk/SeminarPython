# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи (Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной.

# with open('data_first_cariant.csv', 'a', encoding='utf-8') as file:
#     file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')


# Решение: (процесс 1)

#menu = ['first name', 'last name', 'number']
#save = ['Иванов', 'Иван', '89516784598']
#memory = ['Долгов', 'Андрей', '895164367890']

# dict = {1: ['Иванов', 'Иван', '89516784598'], 2: ['Долгов', 'Андрей', '895164367890']}
# for i in dict:
#     #print(*dict[i])
#     for j in range(3):
#         if "89" in dict[i][j]:
#     #    print(dict[i][0])
#             #if dict[i][0]=="Иванов":
#                 print(*dict[i])
# print("Здравствуйте!")
# print("Вывести телефонную книжку - 1")
# print("Добавить записи")
# print("1 Показать записи")
# print("2 Добавить записи")
# print("3 Добавить номер телефона")
# print("Введите число от 1 до 3")
# n = input()
# if n == '1':
#     print(dict)
# if n =='2':




# Решение: (процесс 2)
menu = ['first_name', 'last_name', 'number']
# save = ['Иванов', 'Иван', '89515784598']
collect = {}
d=1
with open('phonebook(forZ49).txt', 'r', encoding='utf-8') as file:
    for l in file:
        l=l.replace('\n','')
        collect[d]=list(l.split(';'))
        d=d+1
dictPhone = collect
def findNumber(dict):
    find = sTr(input('Введите ваш запрос для поиска: '))
    for i in dict:
        for j in range(len(dict[i])):
            if find in dict[i][j]:
                print(dict[i])
def getPhone(dictP):
    for i in dictP:
        print(dictP[i])
def choice(n, dict):
    if n==1:
        getPhone(dict)
    if n==2:
        findNumber(dict)
    if n==3:
        addPhone()
        getPhone(dict)


def addPhone():
    s = 1
    save = list(input('Введите фамилию, имя и номер телефона (через пробел): ').split())
    while True:
        if s in dictPhone:
            s=s+1
        else:
            dictPhone[s] =  save
            break





print('Здравствуйте!')
print('Выберите действие с телефонным справочником о 1 до 3:')
print('Показать справочник - 1')
print('Произвести поиск по запросу - 2')
print('Добавить данные в справочник - 3')
n = int(input())
choice(n, dictPhone)

# созданный фаил для дописывания; 'a' - функция дописывания в фаил, "а+" чтение и дописывание

with open('phonebook(forZ49).txt', 'w', encoding='utf-8') as file:
    for k in dictPhone:
        file.write(f'{dictPhone[k][0]};{dictPhone[k][1]};{dictPhone[k][2]}\n')

print(collect)

# print(menu, end='\f')
# getPhone(dictPhone)



