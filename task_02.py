'''Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) '''

number = int(input('Введите число - '))
summ = 0
while number > 0:
    n = number % 10
    summ += n
    number //= 10
print(summ)   


