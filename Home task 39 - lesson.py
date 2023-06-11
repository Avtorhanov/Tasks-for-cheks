# 1. Создайте программу Python для интернет-магазина,
# состоящую из двух основных классов: CustomerManager и ProductInventory.
# Класс CustomerManager должен отвечать за обработку
# операций, связанных с клиентами, таких как добавление
# новых клиентов, обновление информации о клиентах и получение
# данных о клиентах. Он должен иметь такие методы,
# как add_customer(), update_customer() и get_customer().
# Класс ProductInventory должен отвечать за управление
# запасами товаров в магазине. Он должен обрабатывать
# такие операции, как добавление продуктов, обновление
# информации о продукте и получение сведений о продукте.
# Он должен иметь такие методы, как add_product(),
# update_product() и get_product().
# Разделяя управление клиентами и запасами продуктов на
# отдельные классы, вы гарантируете, что каждый класс
# несет единую ответственность, делая программу более
# модульной и простой в обслуживании.

class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def update_customer(self, customer_id, new_data):
        for customer in self.customers:
            if customer['id'] == customer_id:
                customer.update(new_data)
                break

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer['id'] == customer_id:
                return customer
        return None


class ProductInventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_product(self, product_id, new_data):
        for product in self.products:
            if product['id'] == product_id:
                product.update(new_data)
                break

    def get_product(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None


# Пример использования классов

# Создаем экземпляры классов
customer_manager = CustomerManager()
product_inventory = ProductInventory()

# Добавляем клиентов
customer1 = {'id': 1, 'name': 'Иванов', 'email': 'ivanov@example.com'}
customer_manager.add_customer(customer1)

customer2 = {'id': 2, 'name': 'Петров', 'email': 'petrov@example.com'}
customer_manager.add_customer(customer2)

# Добавляем продукты
product1 = {'id': 1, 'name': 'Телефон', 'price': 10000}
product_inventory.add_product(product1)

product2 = {'id': 2, 'name': 'Ноутбук', 'price': 50000}
product_inventory.add_product(product2)

# Обновляем информацию о клиенте
customer_manager.update_customer(1, {'email': 'newemail@example.com'})

# Обновляем информацию о продукте
product_inventory.update_product(2, {'price': 55000})

# Получаем данные о клиенте и продукте
customer_data = customer_manager.get_customer(1)
product_data = product_inventory.get_product(2)

# Выводим полученные данные
print("Данные о клиенте:")
print(customer_data)

print("Данные о продукте:")
print(product_data)

# Разработайте систему управления библиотекой Python,
# позволяющую добавлять новые типы книг без изменения
# существующей кодовой базы.
# В системе должен быть базовый класс Book, определяющий
# общие свойства и методы для всех типов книг. Подклассы,
# такие как FictionBook, NonFictionBook и ReferenceBook,
# должны наследоваться от класса Book и предоставлять
# определенные реализации для соответствующих типов.
# Чтобы добавить новый тип книги, вы должны иметь
# возможность создать новый подкласс книги и реализовать
# необходимые функции без изменения существующего кода.
# Библиотечная система должна по-прежнему иметь возможность
# беспрепятственно обрабатывать новый тип книг.
# Придерживаясь принципа открытости/закрытости, система
# управления библиотекой позволит легко расширять ее без
# необходимости изменения основной кодовой базы, повышая
# удобство сопровождения и снижая риск появления ошибок.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()}, Genre: {self.genre}"


class NonFictionBook(Book):
    def __init__(self, title, author, year, subject):
        super().__init__(title, author, year)
        self.subject = subject

    def get_info(self):
        return f"{super().get_info()}, Subject: {self.subject}"


class ReferenceBook(Book):
    def __init__(self, title, author, year, edition):
        super().__init__(title, author, year)
        self.edition = edition

    def get_info(self):
        return f"{super().get_info()}, Edition: {self.edition}"

book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
book2 = NonFictionBook("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, "Anthropology")
book3 = ReferenceBook("Python Crash Course", "Eric Matthes", 2015, "2nd")

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


class ScienceBook(Book):
    def __init__(self, title, author, year, field):
        super().__init__(title, author, year)
        self.field = field

    def get_info(self):
        return f"{super().get_info()}, Field: {self.field}"

book4 = ScienceBook("The Elegant Universe", "Brian Greene", 1999, "Physics")
print(book4.get_info())


# Создайте программу Python, определяющую иерархию классов
# для различных геометрических фигур, таких как Shape,
# Circle, Rectangle и Triangle.
# Класс Shape должен служить базовым классом, предоставляя
# общие свойства и методы для всех фигур. Каждый конкретный
# класс формы (Circle, Rectangle, Triangle) должен наследоваться
# от Shape и реализовывать свои собственные методы, такие как
# calculate_area() и calculate_perimeter().
# Программа должна позволять вам рассматривать любую фигуру как
# экземпляр класса Shape, обеспечивая соблюдение принципа подстановки
# Лисков. Это означает, что вы должны иметь возможность заменить
# любую конкретную фигуру объектом Shape в любой части программы,
# не влияя на её выполнение.
# Разрабатывая иерархию классов в соответствии с принципом замещения
# Лискова, вы создаете систему, которая является более гибкой,
# расширяемой и способной единообразно обрабатывать операции, связанные с формами.

import math


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

triangle = Triangle(3, 4, 5)
print(triangle.calculate_area())
print(triangle.calculate_perimeter())


# Разработайте программу Python для службы обмена сообщениями,
# которая включает два отдельных интерфейса: TextMessaging и MultimediaMessaging.
# Интерфейс TextMessaging должен определять методы, специфичные
# для текстовых сообщений, такие как send_text_message(),
# receive_text_message() и get_message_history().
# Интерфейс MultimediaMessaging должен включать методы, специфичные
# для мультимедийных сообщений, такие как send_multimedia_message(),
# Receive_multimedia_message() и view_media_gallery().
# Классы, представляющие различные службы обмена сообщениями, должны
# реализовывать соответствующие интерфейсы в зависимости от их возможностей.
# Например, класс, реализующий TextMessaging, может обрабатывать текстовые
# сообщения, а класс, реализующий MultimediaMessaging, может обрабатывать
# как текстовые, так и мультимедийные сообщения.
# Разделяя интерфейсы, вы гарантируете, что классам нужно будет реализовать
# только соответствующие методы, предотвращая их принуждение к предоставлению
# ненужной функциональности. Это способствует лучшей организации кода и снижает
# вероятность раздувания классов или нарушения принципа единой ответственности.

from abc import ABC, abstractmethod


class TextMessaging(ABC):
    @abstractmethod
    def send_text_message(self, message):
        pass

    @abstractmethod
    def receive_text_message(self):
        pass

    @abstractmethod
    def get_message_history(self):
        pass


class MultimediaMessaging(ABC):
    @abstractmethod
    def send_multimedia_message(self, message, media):
        pass

    @abstractmethod
    def receive_multimedia_message(self):
        pass

    @abstractmethod
    def view_media_gallery(self):
        pass


class TextMessagingService(TextMessaging):
    def send_text_message(self, message):
        print(f"Sending text message: {message}")

    def receive_text_message(self):
        print("Receiving text message")

    def get_message_history(self):
        print("Getting message history")


class MultimediaMessagingService(MultimediaMessaging):
    def send_multimedia_message(self, message, media):
        print(f"Sending multimedia message: {message} with media: {media}")

    def receive_multimedia_message(self):
        print("Receiving multimedia message")

    def view_media_gallery(self):
        print("Viewing media gallery")


text_service = TextMessagingService()
text_service.send_text_message("Hello")
text_service.receive_text_message()
text_service.get_message_history()

multimedia_service = MultimediaMessagingService()
multimedia_service.send_multimedia_message("Hello", "image.jpg")
multimedia_service.receive_multimedia_message()
multimedia_service.view_media_gallery()

# Разработайте систему ведения журнала Python, которая поддерживает
# различные типы средств ведения журнала, например ConsoleLogger,
# FileLogger и DatabaseLogger. Реализуйте принцип инверсии зависимостей,
# используя абстракции (интерфейсы) для ведения журнала.
# Определите интерфейс с именем Logger, который включает такие методы,
# как log_info(), log_warning() и log_error(). Каждый класс регистратора
# (ConsoleLogger, FileLogger, DatabaseLogger) должен реализовать этот интерфейс
# и предоставить собственную реализацию методов ведения журнала.
# Модули высокого уровня в системе должны зависеть от интерфейса регистратора,
# а не от конкретных реализаций регистратора. Это позволяет легко подключать или
# заменять различные типы регистраторов, не влияя на функциональность
# модулей высокого уровня.
# Придерживаясь принципа инверсии зависимостей, вы создаете гибкую и расширяемую
# систему ведения журналов, которая обеспечивает слабую связанность и
# модульность вашей кодовой базы.

from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_info(self, message):
        pass

    @abstractmethod
    def log_warning(self, message):
        pass

    @abstractmethod
    def log_error(self, message):
        pass


class ConsoleLogger(Logger):
    def log_info(self, message):
        print(f"[INFO] {message}")

    def log_warning(self, message):
        print(f"[WARNING] {message}")

    def log_error(self, message):
        print(f"[ERROR] {message}")


class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename

    def log_info(self, message):
        self._write_log("[INFO]", message)

    def log_warning(self, message):
        self._write_log("[WARNING]", message)

    def log_error(self, message):
        self._write_log("[ERROR]", message)

    def _write_log(self, level, message):
        with open(self.filename, "a") as file:
            file.write(f"{level} {message}\n")


class DatabaseLogger(Logger):
    def __init__(self, database):
        self.database = database

    def log_info(self, message):
        self._save_log("INFO", message)

    def log_warning(self, message):
        self._save_log("WARNING", message)

    def log_error(self, message):
        self._save_log("ERROR", message)

    def _save_log(self, level, message):
        pass

logger = ConsoleLogger()
logger.log_info("This is an information message")
logger.log_warning("This is a warning message")
logger.log_error("This is an error message")

file_logger = FileLogger("log.txt")
file_logger.log_info("This is an information message")
file_logger.log_warning("This is a warning message")
file_logger.log_error("This is an error message")

database_logger = DatabaseLogger(database)
database_logger.log_info("This is an information message")
database_logger.log_warning("This is a warning message")
database_logger.log_error("This is an error message")
