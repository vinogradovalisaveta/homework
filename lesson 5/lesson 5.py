import math

a, b, c = int(input('Введите значения сторон a, b и c: ')), int(input()), int(input())
p = (a + b + c) / 2
A = int(input('Введите значение угла А: '))
R = (p - a) * math.tan(math.radians(A / 2))
S = math.pi * R ** 2

print(f'Площадь круга, вписанного в треугольник со сторонами {a}, {b} и {c} равна {S}.')
