# Задачи на 15.04.2023.

# модуль ООП. Тема: классы и объекты.
#
# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


# class Car:
#     def __init__(self, model_name, year_of_manufacture, manufacturer, engine_size, car_color, price):
#         self.model_name = model_name
#         self.year_of_manufacture = year_of_manufacture
#         self.manufacturer = manufacturer
#         self.engine_size = engine_size
#         self.car_color = car_color
#         self.price = price
#
#     def set_info(self):
#         self.model_name = input('Введите модель: ')
#         self.year_of_manufacture = input('Введите год выпуска: ')
#         self.manufacturer = input('Введите производителя: ')
#         self.engine_size = input('Введите объем двигателя: ')
#         self.car_color = input('Введите цвет машины: ')
#         self.price = input('Введите цену: ')
#
#     def print_info(self):
#         print(f'Модель: {self.model_name}\n'
#               f'Год выпуска: {self.year_of_manufacture} г\n'
#               f'Производитель: {self.manufacturer}\n'
#               f'Объем двигателя: {self.engine_size} л\n'
#               f'Цвет машины: {self.car_color}\n'
#               f'Цена: {self.price} руб\n')
#
#
# Car1 = Car('Лада-Гранта',
#            '2015',
#            'Россия',
#            '1.6',
#            'Белый',
#            '300 000')
#
# Car1.print_info()
# Car1.set_info()
# Car1.print_info()


# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class Book:
#     def __init__(self, title_of_the_book, year_of_issue, publisher, genre, author, price):
#         self.title_of_the_book = title_of_the_book
#         self.year_of_issue = year_of_issue
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#     def set_info(self):
#         self.title_of_the_book = input('Введите название книги: ')
#         self.year_of_issue = input('Введите год выпуска: ')
#         self.publisher = input('Введите издателя: ')
#         self.genre = input('Введите Жанр: ')
#         self.author = input('Введите Автора: ')
#         self.price = input('Введите цену: ')
#     def print_info(self):
#         print(f'Название книги: {self.title_of_the_book}\n'
#               f'Год выпуска: {self.year_of_issue}\n'
#               f'Издательство: {self.publisher}\n'
#               f'Жанр: {self.genre}\n'
#               f'Автор: {self.author}\n'
#               f'Цена: {self.price}\n')
#
# Book1 = Book('Сицилиец',
#              '1969',
#               'Random House',
#               'Зарубежная классика',
#               'Марио Пьюзо',
#               '550')
# Book1.print_info()
# Book1.set_info()
# Book1.print_info()

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class Stadium:
#     def __init__(self, stadium_name, opening_date, country, city, capacity):
#         self.stadium_name = stadium_name
#         self.opening_date = opening_date
#         self.country = country
#         self.city = city
#         self.capacity = capacity
#
#     def set_info(self):
#         self.stadium_name = input('Введите Название стадиона: ')
#         self.opening_date = input('Введите Дату открытия: ')
#         self.country = input('Введите Страну: ')
#         self.city = input('Введите Город: ')
#         self.capacity = input('Введите вместимость: ')
#
#     def print_info(self):
#         print(f'Название стадиона: {self.stadium_name}\n'
#         f'Год открытия: {self.opening_date}\n'
#         f'Страна: {self.country}\n'
#         f'Город: {self.city}\n'
#         f'Вместимость: {self.capacity}\n')
#
# Stadium1 = Stadium('Краснодар',
#                    '2016',
#                    'Россия',
#                    'Краснодар',
#                    '35 179')
# Stadium1.print_info()
# Stadium1.set_info()
# Stadium1.print_info()

# Задачи 16.04 Тема: Статические методы

#  К уже реализованному классу «Дробь» добавьте статический метод,
#  который при вызове возвращает количество созданных объектов класса «Дробь».

# class Fraction:
#     count = 0
#
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#         Fraction.count += 1
#
#     @staticmethod
#     def get_count():
#         return Fraction.count
#
#     def __add__(self, other):
#         if isinstance(other, int):
#             other = Fraction(other, 1)
#         common_denominator = self.denominator * other.denominator
#         common_numerator = self.numerator * other.denominator + other.numerator * self.denominator
#         return Fraction(common_numerator, common_denominator)
#
#     def __sub__(self, other):
#         if isinstance(other, int):
#             other = Fraction(other, 1)
#         common_denominator = self.denominator * other.denominator
#         common_numerator = self.numerator * other.denominator - other.numerator * self.denominator
#         return Fraction(common_numerator, common_denominator)
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             other = Fraction(other, 1)
#         numerator = self.numerator * other.numerator
#         denominator = self.denominator * other.denominator
#         return Fraction(numerator, denominator)
#
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             other = Fraction(other, 1)
#         numerator = self.numerator * other.denominator
#         denominator = self.denominator * other.numerator
#         return Fraction(numerator, denominator)
#
# f1 = Fraction(1, 2)
# f2 = Fraction(3, 4)
# f3 = Fraction(2, 5)
#
# print(Fraction.get_count())

# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температуры и
# возвращать это значение с помощью статического метода.

# class UnitConverter:
#     @staticmethod
#     def meters_to_feet(meters):
#         return meters * 3.28084
#     @staticmethod
#     def feet_to_meters(feet):
#         return feet / 3.28084
#     @staticmethod
#     def meters_to_yards(meters):
#         return meters * 1.09361
#     @staticmethod
#     def yards_to_meters(yards):
#         return yards / 1.09361
#     @staticmethod
#     def meters_to_miles(meters):
#         return meters / 1609.344
#     @staticmethod
#     def miles_to_meters(miles):
#         return miles * 1609.344
#
# print(UnitConverter.meters_to_feet(10))
# print(UnitConverter.feet_to_meters(32.8084))
# print(UnitConverter.meters_to_yards(100))

# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

# class TemperatureConverter:
#     count = 0
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         TemperatureConverter.count += 1
#         return celsius * 1.8 + 32
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         TemperatureConverter.count += 1
#         return (fahrenheit - 32) / 1.8
#     @staticmethod
#     def get_conversion_count():
#         return TemperatureConverter.count
#
# print(TemperatureConverter.celsius_to_fahrenheit(0))
# print(TemperatureConverter.fahrenheit_to_celsius(32))
# print(TemperatureConverter.celsius_to_fahrenheit(100))