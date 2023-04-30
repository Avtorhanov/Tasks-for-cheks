# Тема: Структура данных часть - 2
# Задание 1
# Пользователь вводит с клавиатуры набор чисел. Полученные
# числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует
# в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от выбора
# пользователя список нужно показать с начала или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь определяет заменить
# или только первое вхождение или все вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.

# number_list = []
# while True:
#     print("1. Добавить число в список")
#     print("2. Удалить все вхождения числа из списка")
#     print("3. Показать содержимое списка")
#     print("4. Проверить есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     print("0. Выход")
#     choice = input("Ваш выбор: ")
#     if choice == '0':
#         break
#     elif choice == '1':
#         number = int(input("Введите число: "))
#         if number in number_list:
#             print("Это число уже есть в списке")
#         else:
#             number_list.append(number)
#         print(number_list)
#     elif choice == '2':
#         number = int(input("Введите число для удаления: "))
#         if number in number_list:
#             number_list = [x for x in number_list if x != number]
#             print("Число удалено")
#         else:
#             print("Этого числа нет в списке")
#         print(number_list)
#     elif choice == '3':
#         order = input("Выберите порядок вывода:\n"
#                       "1. С начала\n"
#                       "2. С конца\n"
#                       "Ваш выбор: ")
#         if order == '1':
#             print(number_list)
#         elif order == '2':
#             print(number_list[::-1])
#         else:
#             print("Неверный выбор")
#     elif choice == '4':
#         number = int(input("Введите число: "))
#         if number in number_list:
#             print("Это число есть в списке")
#         else:
#             print("Этого числа нет в списке")
#     elif choice == '5':
#         number = int(input("Введите число, которое нужно заменить: "))
#         if number in number_list:
#             new_number = int(input("Введите новое число: "))
#             mode = input("Выберите режим замены:\n"
#                          "1. Заменить первое вхождение\n"
#                          "2. Заменить все вхождения\n"
#                          "Ваш выбор: ")
#             if mode == '1':
#                 index = number_list.index(number)
#                 number_list[index] = new_number
#             elif mode == '2':
#                 number_list = [new_number if x == number else x for x in number_list]
#             else:
#                 print("Неверный выбор")
#         else:
#             print("Этого числа нет в списке")
#         print(number_list)

# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.

# class StringStack:
#     def __init__(self, size):
#         self.size = size
#         self.stack = []
#
#     def push(self, string):
#         if len(self.stack) < self.size:
#             self.stack.append(string)
#         else:
#             print("Стек полный")
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             print("Стек пустой")
#
#     def count(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def is_full(self):
#         return len(self.stack) == self.size
#
#     def clear(self):
#         self.stack = []
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Стек пустой")
#
# stack = StringStack(3)
# stack.push("строка 1")
# stack.push("строка 2")
# stack.push("строка 3")
#
# print(stack.pop())
# print(stack.pop())

# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.

# class StringStack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, string):
#         self.stack.append(string)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             print("Стек пустой")
#
#     def count(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def clear(self):
#         self.stack = []
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Стек пустой")
#
# stack = StringStack()
# stack.push("строка 1")
# stack.push("строка 2")
# stack.push("строка 3")
# print(stack.count())
# print(stack.pop())
# print(stack.pop())
# print(stack.count())
