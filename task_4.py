# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('-->'))

drob = ""

while number > 0:
    drob = str(number % 2) + drob
    number = number // 2

print(drob)

# print(bin(4))