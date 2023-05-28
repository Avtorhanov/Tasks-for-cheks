# Модульное тестирование
#
# Задание 1
# Создайте класс, содержащий набор целых чисел.
# В классе должна быть реализована следующая функциональность:
# ■ Сумма элементов набора.
# ■ Среднеарифметическое элементов набора.
# ■ Максимум из элементов набора.
# ■ Минимум из элементов набора.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

import unittest

class SetOfNumbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def maximum(self):
        return max(self.numbers)

    def minimum(self):
        return min(self.numbers)


class TestSetOfNumbers(unittest.TestCase):
    def setUp(self):
        self.set_of_numbers = SetOfNumbers([1, 2, 3, 4, 5])

    def test_sum(self):
        result = self.set_of_numbers.sum()
        self.assertEqual(result, 15)

    def test_average(self):
        result = self.set_of_numbers.average()
        self.assertEqual(result, 3)

    def test_maximum(self):
        result = self.set_of_numbers.maximum()
        self.assertEqual(result, 5)

    def test_minimum(self):
        result = self.set_of_numbers.minimum()
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()


# Задание 2
# Создайте класс для числа. В классе должна быть ре-
# ализована следующая функциональность:
# ■ Запись и чтение значения.
# ■ Перевод числа в восьмеричную систему исчисления.
# ■ Перевод числа в шестнадцатеричную систему исчис-
# ления.
# ■ Перевод числа в двоичную систему исчисления.
# Протестируйте все возможности созданного класса
# с помощью модульного тестирования(unittest).

import unittest

class Number:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def to_octal(self):
        return oct(self.value)

    def to_hexadecimal(self):
        return hex(self.value)

    def to_binary(self):
        return bin(self.value)


class TestNumber(unittest.TestCase):
    def setUp(self):
        self.number = Number(42)

    def test_set_value(self):
        self.number.set_value(99)
        self.assertEqual(self.number.get_value(), 99)

    def test_to_octal(self):
        result = self.number.to_octal()
        self.assertEqual(result, '0o52')

    def test_to_hexadecimal(self):
        result = self.number.to_hexadecimal()
        self.assertEqual(result, '0x2a')

    def test_to_binary(self):
        result = self.number.to_binary()
        self.assertEqual(result, '0b101010')

if __name__ == '__main__':
    unittest.main()
