# ООП - 3. 22.04.23
#
# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■ Проверка на равенство радиусов двух окружностей
# (операция = =);
# ■ Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# ■ Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __lt__(self, other):
#         return self.radius < other.radius
#
#     def __gt__(self, other):
#         return self.radius > other.radius
#
#     def __le__(self, other):
#         return self.radius <= other.radius
#
#     def __ge__(self, other):
#         return self.radius >= other.radius
#
#     def __add__(self, other):
#         return Circle(self.radius + other.radius)
#
#     def __sub__(self, other):
#         return Circle(self.radius - other.radius)
#
#     def __iadd__(self, other):
#         self.radius += other
#         return self
#
#     def __isub__(self, other):
#         self.radius -= other
#         return self
#
# c1 = Circle(5)
# c2 = Circle(7)
#
# print(c1 == c2)
# print(c1 < c2)
# print(c1 > c2)
# print(c1 <= c2)
# print(c1 >= c2)
#
# c3 = c1 + c2
# print(c3.radius)

# Задание 2
# Создайте класс Complex (комплексное число). Более
# подробно ознакомиться с комплексными числами можно
# по ссылке.
# Создайте перегруженные операторы для реализации
# арифметических операций для по работе с комплексными
# числами (операции +, -, *, /).

# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)
#
#     def __mul__(self, other):
#         return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
#
#     def __truediv__(self, other):
#         d = other.real ** 2 + other.imag ** 2
#         return Complex((self.real * other.real + self.imag * other.imag) / d, (self.imag * other.real - self.real * other.imag) / d)
#
#     def __str__(self):
#         return f"{self.real} + {self.imag}i"
#
#
# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
#
# c3 = c1 + c2
# print(c3)
#
# c4 = c2 - c1
# print(c4)

# Задание 3
# Вам необходимо создать класс Airplane (самолет).
# ■ Проверка на равенство типов самолетов (операция = =);
# ■ Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■ Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции >
# < <= >=).

# class Airplane:
#     def __init__(self, airplane_type, max_passengers, current_passengers):
#         self.airplane_type = airplane_type
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers
#
#     def __eq__(self, other):
#         return self.airplane_type == other.airplane_type
#
#     def __add__(self, other):
#         return Airplane(self.airplane_type, self.max_passengers + other, self.current_passengers + other)
#
#     def __iadd__(self, other):
#         self.max_passengers += other
#         self.current_passengers += other
#         return self
#
#     def __sub__(self, other):
#         return Airplane(self.airplane_type, self.max_passengers - other, self.current_passengers - other)
#
#     def __isub__(self, other):
#         self.max_passengers -= other
#         self.current_passengers -= other
#         return self
#
#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers
#
#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers
#
#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers
#
#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers
#
# airplane1 = Airplane("Boeing 737", 200, 100)
# airplane2 = Airplane("Boeing 747", 300, 200)
#
# print(airplane1 == airplane2)
# print(airplane1 == Airplane("Boeing 737", 150, 75))
#
# airplane1 += 50
# print(airplane1.max_passengers)
# print(airplane1.current_passengers)


# Задание 4
#Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■ Проверка на равенство площадей квартир (операция
# ==);
# ■ Проверка на неравенство площадей квартир (операция !=);
# ■ Сравнение двух квартир по цене (операции > < <= >=).
# class Flat:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#
#     def __eq__(self, other):
#         return self.area == other.area
#
#     def __ne__(self, other):
#         return self.area != other.area
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __le__(self, other):
#         return self.price <= other.price
#
#     def __gt__(self, other):
#         return self.price > other.price
#
#     def __ge__(self, other):
#         return self.price >= other.price
#
# flat1 = Flat(50, 100000)
# flat2 = Flat(60, 120000)
# flat3 = Flat(50, 90000)
#
# print(flat1 == flat2)
# print(flat1 == flat3)
# print(flat1 != flat2)
# print(flat1 > flat2)
>>>>>>> c4cf159 (Tasks for chek - 22.04)
