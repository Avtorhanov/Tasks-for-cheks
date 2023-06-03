# 1. Напишите функцию analysis_and_summarize_file, которая принимает имя файла
# в качестве входных данных. Файл содержит большое количество текстовых данных.
# Функция должна прочитать содержимое файла, проанализировать данные для сбора
# соответствующей информации (например, частота слов, количество строк,
# средняя длина слова) и создать сводный отчет в новом файле.
# import re
#
#
# def analyse_file(filename, log_file):
#     file = open(filename, 'r', encoding='utf-8')
#     text = file.read()
#     string_count = text.count('\n') + 1
#     words = {}
#     avg_word_length = 0
#     words_list = re.split('[,.!?;\s]+', text)
#
#     for word in words_list:
#         avg_word_length += len(word)
#         if word in words:
#             words[word] += 1
#         else:
#             words[word] = 1
#
#     avg_word_length = avg_word_length / len(words_list)
#     word_frequency = sorted([(word, words[word] / len(words_list)) for word in words],
#                             key=lambda x: x[1], reverse=True)
#     file.close()
#     with open('log.txt', 'w', encoding='utf-8') as f:
#         f.write(f'Количество строк: {string_count}\n'
#                 f'Самые частые слова: {[word for word in word_frequency[:10]]}\n'
#                 f'Средняя длина слова: {avg_word_length}')
#
#
# print(analyse_file('file.txt', 'log.txt'))


# 2. Напишите две функции: encrypt_file и decrypt_file. Функция encrypt_file должна
# принимать имя файла и ключ в качестве входных данных, считывать содержимое файла,
# шифровать содержимое с помощью пользовательского алгоритма шифрования и записывать
# зашифрованные данные в новый файл. Функция decrypt_file должна принимать имя файла
# и тот же ключ в качестве входных данных, читать зашифрованное содержимое файла,
# расшифровывать содержимое с использованием обратного алгоритма и записывать
# расшифрованные данные в новый файл. Создайте декоратор с именем encryption_logging,
# который регистрирует сведения об операциях шифрования и дешифрования,
# такие как имя файла, ключ и отметка времени.

# import time
# import random
#
#
# def encryption_logging(func):
#     def wrapper(*args, **kwargs):
#         with open('encryption_logging.txt', 'a', encoding='utf-8') as f:
#             result = func(*args, **kwargs)
#             f.write(f'Функция {func} была вызвана на этих данных {args} в {time.ctime()}\n')
#         return result
#     return wrapper
#
#
# @encryption_logging
# def encrypt_file(file, key):
#     with open(file, 'r+') as f:
#         text = f.read()
#         shift = key % 25 + 1
#         encoded_text = ''
#         for symbol in text:
#             encoded_text += chr((ord(symbol) + shift) % 26 + 97)
#         f.seek(0)
#         f.write(encoded_text)
#
#
# @encryption_logging
# def decrypt_file(file, key):
#     with open(file, 'r+') as f:
#         encoded_text = f.read()
#         shift = key % 25 + 1
#         text = ''
#         for symbol in encoded_text:
#             text += chr((ord(symbol) - shift) % 26 + 97)
#         f.seek(0)
#         f.write(text)
#
#
# key = random.randint(1000000, 9999999)
# encrypt_file('file.txt', key)
# decrypt_file('file.txt', key)


# 3. Напишите функцию с именем analysis_file_sizes, которая принимает путь к каталогу
# в качестве входных данных. Функция должна рекурсивно обходить каталог и его подкаталоги и
# вычислять общий размер всех файлов, содержащихся в них. Результат должен быть возвращен в
# удобочитаемом формате, например, в килобайтах (КБ), мегабайтах (МБ) или гигабайтах (ГБ).
# Реализуйте эту функциональность с помощью модуля os в Python.

# import os
#
#
# def analysis_file_sizes(directory):
#     total_size = 0
#     for item in os.listdir(directory):
#         item_path = os.path.join(directory, item)
#         if os.path.isfile(item_path):
#             total_size += os.path.getsize(item_path)
#         elif os.path.isdir(item_path):
#             total_size += analysis_file_sizes(item_path)
#
#     return total_size
#
#
# print(analysis_file_sizes(r'C:\Users\kosty\Python216\37'))


