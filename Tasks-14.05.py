# Задание 1
# Создайте реализацию паттерна Command.
# Протестируйте работу созданного класса

from abc import ABC, abstractmethod

# class for creating commands
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

# Concrete implementation of the command
class Door_opening(Command):
    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.opening()
        print('Дверь открыта')

class Closing_door(Command):
    def __init__(self, door):
        self.door = door

    def execute(self):
        self.door.closing()
        print('Дверь закрыта')

# Door control
class Door_control:
    def __init__(self):
        self.is_open = False

    def opening(self):
        self.is_open = True

    def closing(self):
        self.is_open = False

# Call object
class Access:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print("Command not found.")

# Instantiate the door control object and commands
By_access = Door_control()
By_access_open_command = Door_opening(By_access)
By_access_closing_command = Closing_door(By_access)

# Register the commands with the Access object
access = Access()
access.register("Сезам откройся", By_access_open_command)
access.register("Сезам закройся", By_access_closing_command)
#
# Execute the commands
access.execute("Сезам откройся")
# access.execute("Сезам закройся")

# Задание 2
# Есть класс, предоставляющий доступ к набору чисел.
# Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле
# меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и
# выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому
# набору необходимо вносить запись в лог-файл. При
# реализации используйте паттерн Proxy (для логгирования)
# и другие необходимые паттерны

from datetime import datetime
from abc import ABC, abstractmethod

class DataSource(ABC):

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def update_data(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read_data(self):
        with open(self.filename, 'r') as f:
            self.data = [int(line.strip()) for line in f]

        return self.data

    def update_data(self):
        with open(self.filename, 'w') as f:
            self.data = [i + 1 for i in self.data]
            f.write('\n'.join(str(i) for i in self.data))

class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def sum(self):
        return sum(self.data_source.read_data())

    def max(self):
        data = self.data_source.read_data()
        return max(data) if data else 'Список пуст'

    def min(self):
        data = self.data_source.read_data()
        return min(data) if data else 'Список пуст'

    def average(self):
        data = self.data_source.read_data()
        return sum(data) / len(data) if data else 'Список пуст'

class DataProxy(DataSource):
    def __init__(self, data_source):
        self.data_source = data_source
        self.read_logged = False

    def update_data(self):
        self.data_source.update_data()
        self.log('Updated')

    def log(self, action):
        with open('log.txt', 'a') as f:
            f.write(f'{action}\n')

    def log(self, action, data=None):
        message = f'{action} - {datetime.now():%H:%M:%S %Y-%m-%d}'
        if data:
            message += f': {data}'
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

    def read_data(self):
        if not self.read_logged:
            self.log('Updated')
            self.read_logged = True
        data = self.data_source.read_data()
        return data

class DataCacheDecorator(DataProcessor):
    def __init__(self, data_source, cache_size=100):
        super().__init__(DataProxy(data_source))
        self.cache_size = cache_size
        self.cache = {}

    def sum(self):
        if 'sum' not in self.cache:
            self.cache['sum'] = super().sum()
        return self.cache['sum']


data_source = FileDataSource('data.txt')
data_processor = DataCacheDecorator(data_source, cache_size=100)

print('Summ - ', data_processor.sum(),
     '\nMax - ', data_processor.max(),
     '\nMin - ', data_processor.min(),
     '\nAver - ', data_processor.average())


# Задание 3
# Создайте приложение для работы в библиотеке. Оно
# должно оперировать следующими сущностями: Книга,
# Библиотекарь, Читатель. Приложение должно позволять
# вводить, удалять, изменять, сохранять в файл, загружать из
# файла, логгировать действия, искать информацию (результаты
# поиска выводятся на экран или файл) о сущностях.
# При реализации используйте максимально возможное
# количество паттернов проектирования.
# -----------------------------------
