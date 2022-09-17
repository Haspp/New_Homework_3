# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from typing import Any

from math import ceil

import random


def array():
    element = int(input("--> "))
    list_number = []
    list_number = random.sample(range(15), element)
    return list_number


def multiplication(list_number):
    result = []
    for i in range(int(ceil(len(list_number) / 2))):
        result.append(list_number[i] * list_number[-1 - i])
    return result


a = array()
print(a)
res = multiplication(a)
print(res)
