# Тема: Упаковка данных часть - 2
# Задание 1
# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

# import json
# import pickle
#
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def to_json(self):
#         return json.dumps(self.__dict__)
#
#     @staticmethod
#     def from_json(json_string):
#         car_data = json.loads(json_string)
#         return Car(**car_data)
#
#     def to_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def from_pickle(filename):
#         with open(filename, 'rb') as f:
#             return pickle.load(f)
#
# my_car = Car('Toyota', 'Camry', 2021)
#
# with open('car.json', 'w') as f:
#     f.write(my_car.to_json())
#
# with open('car.json', 'r') as f:
#     car_json = f.read()
#     my_car_from_json = Car.from_json(car_json)
#     print(my_car_from_json.make)
#     print(my_car_from_json.model)
#     print(my_car_from_json.year)
#
# my_car.to_pickle('car.pickle')
# my_car_from_pickle = Car.from_pickle('car.pickle')
# print(my_car_from_pickle.make)
# print(my_car_from_pickle.model)
# print(my_car_from_pickle.year)

# Задание 2
# К уже реализованному классу «Книга» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

# import json
# import pickle
#
#
# class Book:
#     def __init__(self, author, name, publish_year):
#         self.author = author
#         self.name = name
#         self.publish_year = publish_year
#
#     def to_json(self):
#         return json.dumps(self.__dict__)
#
#     @staticmethod
#     def from_json(json_string):
#         book_data = json.loads(json_string)
#         return Book(**book_data)
#
#     def to_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def from_pickle(filename):
#         with open(filename, 'rb') as f:
#             return pickle.load(f)
#
#
# my_book = Book('Joanne Kathleen Rowling', 'Harry Potter', '1997 year')
#
# with open('car.json', 'w') as f:
#     f.write(my_book.to_json())
#
# with open('car.json', 'r') as f:
#     book_json = f.read()
#     my_book_from_json = Book.from_json(book_json)
#     print(my_book_from_json.author)
#     print(my_book_from_json.name)
#     print(my_book_from_json.publish_year)
#
# my_book.to_pickle('car.pickle')
# my_book_from_pickle = Book.from_pickle('car.pickle')
# print(my_book_from_pickle.author)
# print(my_book_from_pickle.name)
# print(my_book_from_pickle.publish_year)

# Задание 3
# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.

# import json
# import pickle
#
#
# class Stadium:
#     def __init__(self, city, name, opening_year):
#         self.city = city
#         self.name = name
#         self.opening_year = opening_year
#
#     def to_json(self):
#         return json.dumps(self.__dict__)
#
#     @staticmethod
#     def from_json(json_string):
#         stadium_data = json.loads(json_string)
#         return Stadium(**stadium_data)
#
#     def to_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def from_pickle(filename):
#         with open(filename, 'rb') as f:
#             return pickle.load(f)
#
#
# my_stadium = Stadium('Melbourne', 'Melbourne Cricket Ground', 1854)
# with open('car.json', 'w') as f:
#     f.write(my_stadium.to_json())
#
# with open('car.json', 'r') as f:
#     stadium_json = f.read()
#     my_stadium_from_json = Stadium.from_json(stadium_json)
#     print(my_stadium_from_json.city)
#     print(my_stadium_from_json.name)
#     print(my_stadium_from_json.opening_year)
#
# my_stadium.to_pickle('car.pickle')
# my_stadium_from_pickle = Stadium.from_pickle('car.pickle')
# print(my_stadium_from_pickle.city)
# print(my_stadium_from_pickle.name)
# print(my_stadium_from_json.opening_year)

