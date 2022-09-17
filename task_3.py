# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов
import array as arr

list_number = arr.array('f', [1.1, 1.2, 3.1, 5.1, 10.01])
array_new = []

for i in range(len(list_number)):
    b = 0
    array_new.append(list_number[i] - int(list_number[i]))
    array_new[-1] = round(array_new[-1], 4)

maxar = array_new[0]
minar = array_new[0]

for i in range(1, len(array_new)):
    if array_new[i] > maxar:
        maxar = array_new[i]
    elif array_new[i] < minar:
        minar = array_new[i]

print(maxar - minar)
