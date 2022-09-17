# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonachi(number):
    if number < 2:
        return number
    else:
        return fibonachi(number - 1) + fibonachi(number - 2)


list_1 = []
number = 5
for i in range(number):
    list_1.append(fibonachi(i))
    list_1.insert(0, fibonachi(i) * (-1) ** (i + 1))
list_1.remove(0)

print(list_1)

