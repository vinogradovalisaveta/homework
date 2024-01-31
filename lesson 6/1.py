n, A = int(input()), int(input())
x1, x2 = 1, 0.1

while round(x1, 4) != round(x2, 4):
    x2 = (1 / n) * (((n - 1) * x1) + (A / x1 ** (n - 1)))
    x1, x2 = x2, x1

print(f'Корень {n}-й степени из числа {A} равен {round(x2, 4)}.')