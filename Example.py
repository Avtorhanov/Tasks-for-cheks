# Задача - нахождение суммы чисел по диагонали в матрице

import random

matrix = [[random.randint(1, 10) for j in range(4)] for i in range(4)]

print("Matrix:")
for row in matrix:
    print(row)

left_right_sum = 0
right_left_sum = 0

for i in range(len(matrix)):
    left_right_sum += matrix[i][i]
    right_left_sum += matrix[i][len(matrix)-i-1]

print("Sum of diagonal (left to right):", left_right_sum)
print("Sum of diagonal (right to left):", right_left_sum)

# В этом примере мы создаем матрицу 4x4, заполненную случайными числами от 1 до 10.
# Затем мы выводим матрицу на экран и вычисляем сумму элементов по диагонали
# с лева на право и с права на лево с помощью цикла.
# Для вычисления суммы элементов по диагонали с лева на право мы используем индексы,
# равные номеру строки и номеру столбца, то есть `matrix[i][i]`.
# Для вычисления суммы элементов по диагонали с права на лево мы используем индексы,
# равные номеру строки и общему количеству столбцов минус номер столбца минус 1,
# то есть `matrix[i][len(matrix)-i-1]`.