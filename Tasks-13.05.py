# Тема: Паттерны проектирования
#
# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса

# class Movie:
#     def __init__(self):
#         self.name = None
#         self.genre = None
#         self.actors = None
#
# class MovieBuilder:
#     def __init__(self):
#         self.movie = Movie()
#
#     def build_name(self):
#         self.movie.name = 'Карты, деньги, два ствола'
#
#     def build_genre(self):
#         self.movie.genre = 'Комедийный криминал'
#
#     def build_actors(self):
#         self.movie.actors = 'Весьма неплохие'
#
#     def get_movie(self):
#         return self.movie
#
# class ActionDirector:
#     def __init__(self, builder):
#         self.builder = builder
#
#     def build_movie(self):
#         self.builder.build_name()
#         self.builder.build_genre()
#         self.builder.build_actors()
#         return self.builder.get_movie()
#
# kino = MovieBuilder()
# director = ActionDirector(kino)
# movie = director.build_movie()
# print(f'Фильм: {movie.name}')
# print(f'Жанр: {movie.genre}')
# print(f'Актеры: {movie.actors}')

# Задание 2
# Создайте приложение для приготовления пасты.
# Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны

# from abc import ABC, abstractmethod
#
# class Paste_app:
#
#     @abstractmethod
#     def paste_type(self):
#         pass
#
#     @abstractmethod
#     def sauсe(self):
#         pass
#
#     @abstractmethod
#     def filling(self):
#         pass
#
#     @abstractmethod
#     def additives(self):
#         pass
#
# class Karbonara(Paste_app):
#
#     def paste_type(self):
#         print('спагетти')
#
#     def sauсe(self):
#         print('оливковое масло')
#
#     def filling(self):
#         print('тертый пармезан')
#
#     def additives(self):
#         print('перец по вкусу')
#
# class Bolognese(Paste_app):
#
#     def paste_type(self):
#         print('томатно-мясной')
#
#     def sauсe(self):
#         print('томат')
#
#     def filling(self):
#         print('мясо')
#
#     def additives(self):
#         print('ветки базилика')
#
# class Alfredo(Paste_app):
#
#     def paste_type(self):
#         print('Фетучини')
#
#     def sauсe(self):
#         print('сливочное масло')
#
#     def filling(self):
#         print('пармезан')
#
#     def additives(self):
#         print('сливки')
#
# class ShapePaste:
#
#     @staticmethod
#     def create_paste(name):
#         if name == 'Карбонара':
#             return Karbonara()
#         elif name == 'Болоньезе':
#             return Bolognese()
#         elif name == 'Альфредо':
#             return Alfredo()
#         else:
#             raise ValueError('Нет такой пасты в системе')
#
# pasta_type = input('Введите вид пасты (Карбонара, Болоньезе, Альфредо): ')
# pasta = ShapePaste.create_paste(pasta_type)
# print('Рецепт ' + pasta_type + ' пасты')
# pasta.paste_type()
# pasta.sauсe()
# pasta.filling()
# pasta.additives()

# Задание 3
# Создайте реализацию паттерна Prototype.
# Протестируйте работу созданного класса

# from abc import ABC, abstractmethod
#
# class Prototype(ABC):
#
#     @abstractmethod
#     def clone(self):
#         pass
#
# class Phone(Prototype):
#     def __init__(self, brand, model, system):
#         self.brand = brand
#         self.model = model
#         self.system = system
#         self.is_clean = False
#
#     def clean(self):
#         self.is_clean = True
#
#     def clone(self):
#         obj = Phone(self.brand, self.model, self.system)
#         obj.is_clean = self.is_clean
#         return obj
#
# phone1 = Phone('Apple', 'iPhone-5','iOS')
# phone1.clean()
# phone2 = phone1.clone()
# print(phone2.brand)
# print(phone2.model)
# print(phone2.system)
#
# phone2.model = 'iPhone-6'
#
# print(phone1.model)
#
# print(phone2.model)

