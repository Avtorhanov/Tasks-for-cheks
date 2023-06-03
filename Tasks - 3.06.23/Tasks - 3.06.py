
# Задача 1. Напишите функцию analysis_and_summarize_file, которая принимает имя файла в
# качестве входных данных. Файл содержит большое количество текстовых данных.
# Функция должна прочитать содержимое файла, проанализировать данные для сбора
# соответствующей информации (например, частота слов, количество строк, средняя длина слова)
# и создать сводный отчет в новом файле.

def analysis_and_summarize_file(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = content.split('\n')
    word_count = {}
    total_words = 0
    total_word_length = 0

    for line in lines:
        words = line.split()
        total_words += len(words)
        total_word_length += sum(len(word) for word in words)

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1


    report_filename = "output.txt"

    with open(report_filename, 'w') as report_file:
        report_file.write("Отчет по файлу: " + filename + "\n")
        report_file.write("\n")

        report_file.write("Количество строк: " + str(len(lines)) + "\n")
        report_file.write("\n")

        report_file.write("Частота слов:\n")
        for word, count in word_count.items():
            report_file.write(word + ": " + str(count) + "\n")
        report_file.write("\n")

        if total_words > 0:
            average_word_length = total_word_length / total_words
            report_file.write("Средняя длина слова: " + str(average_word_length) + "\n")
        else:
            report_file.write("Средняя длина слова: Не удалось вычислить (файл пустой)\n")

    print("Сводный отчет успешно создан в файле", report_filename)

filename = "story.txt"

analysis_and_summarize_file(filename)


# Задача 2. Напишите две функции: encrypt_file и decrypt_file. Функция encrypt_file должна
# принимать имя файла и ключ в качестве входных данных, считывать содержимое файла,
# шифровать содержимое с помощью пользовательского алгоритма шифрования и записывать
# зашифрованные данные в новый файл. Функция decrypt_file должна принимать имя файла
# и тот же ключ в качестве входных данных, читать зашифрованное содержимое файла,
# расшифровывать содержимое с использованием обратного алгоритма и записывать
# расшифрованные данные в новый файл. Создайте декоратор с именем encryption_logging,
# который регистрирует сведения об операциях шифрования и дешифрования,
# такие как имя файла, ключ и отметка времени.

from datetime import datetime

def encryption_logging(func):
    def wrapper(filename, key):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Шифрование/дешифрование файла '{filename}' с ключом '{key}' начато в {timestamp}")
        result = func(filename, key)
        print(f"Шифрование/дешифрование файла '{filename}' с ключом '{key}' завершено в {timestamp}")

        return result

    return wrapper

def my_encrypt_function(content, key):
    encrypted_content = content + key
    return encrypted_content

def decrypt_algorithm(encrypted_content, key):
    decrypted_content = encrypted_content.replace(key, "")
    return decrypted_content

@encryption_logging
def encrypt_file(filename, key):
    with open(filename, 'r') as file:
        content = file.read()

    encrypted_content = my_encrypt_function(content, key)

    encrypted_filename = "encrypted_" + filename

    with open(encrypted_filename, 'w') as encrypted_file:
        encrypted_file.write(encrypted_content)

    print("Файл успешно зашифрован и сохранен как", encrypted_filename)

@encryption_logging
def decrypt_file(filename, key):
    with open(filename, 'r') as encrypted_file:
        encrypted_content = encrypted_file.read()

    decrypted_content = decrypt_algorithm(encrypted_content, key)

    decrypted_filename = "decrypted_" + filename

    with open(decrypted_filename, 'w') as decrypted_file:
        decrypted_file.write(decrypted_content)

    print("Файл успешно расшифрован и сохранен как", decrypted_filename)

encrypt_file("file.txt", "my_key")
decrypt_file("encrypted_file.txt", "my_key")


# Задача 3. Напишите функцию с именем analysis_file_sizes, которая принимает путь к каталогу
# в качестве входных данных. Функция должна рекурсивно обходить каталог и его подкаталоги и
# вычислять общий размер всех файлов, содержащихся в них. Результат должен быть возвращен в
# удобочитаемом формате, например, в килобайтах (КБ), мегабайтах (МБ) или гигабайтах (ГБ).
# Реализуйте эту функциональность с помощью модуля os в Python.

import os

def analysis_file_sizes(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size

    total_size = convert_size(total_size)

    return total_size

def convert_size(size):

    power = 2**10

    n = 0
    power_labels = {0: '', 1: 'КБ', 2: 'МБ', 3: 'ГБ'}

    while size > power:
        size /= power
        n += 1

    formatted_size = "{:.2f}".format(size)
    formatted_size = formatted_size.rstrip('0').rstrip('.')

    return f"{formatted_size} {power_labels[n]}"



directory = '/path/to/directory'
total_size = analysis_file_sizes(directory)
print(f"Общий размер файлов в каталоге '{directory}': {total_size}")
