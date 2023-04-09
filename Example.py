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
