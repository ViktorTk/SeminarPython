# Дано натуральное числр A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что ф(n) = A. Если A не
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6



A = int(input('Введите число: '))
fib1 = 1
fib2 = 1
i = 3
if A == fib1: print('номер числа по счету чисел Фибоначчи ')
while A >= i:
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
    if fibsum == A:
        print(f'является {i+1} числом Фибоначчи')
        break
    elif A < fibsum:
        print('-1')
        break
    else: i += 1





