# Задание 1
# Реализуйте клиент — серверное приложение, позво-
# ляющее обмениваться сообщениями в формате один к
# одному. Для начала общения необходимо установить
# соединение. После соединение используется текстовый
# формат. В беседе участвуют только два человека. После
# завершения беседы сервер переходит к ожиданию нового
# участника разговора.

# import socket
#
# def run_client():
#     host = '127.0.0.1'
#     port = 12345
#
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     client_socket.connect((host, port))
#     print('Подключено к серверу')
#
#     while True:
#
#         message = input('Введите сообщение: ')
#
#         client_socket.send(message.encode())
#
#         response = client_socket.recv(1024)
#
#         print('Получен ответ от сервера:', response.decode())
#
#     client_socket.close()
#
# if __name__ == '__main__':
#     run_client()


# Задание 2
# Реализуйте погодное клиент-серверное приложение.
# Клиент обращается к серверу с указанием: страны и горо-
# да. Сервер, получив запрос, возвращает погоду на неделю
# для данной местности. Используйте для реализации при-
# ложения механизмы многопоточности. Данные о погоде
# должны быть предопределенными и взяты из файла.
#
# Задание 3
# Измените задание номер 2. Добавьте получение про-
# гноза погоды из внешнего источника.
# Для этоговоспользуйтесь сайтом https://openweathermap.
# org. Для начала нужно зарегистрироваться на сайте по
# ссылке https://home.openweathermap.org/users/sign_up
# и получить ключ для дальнейшей работы. На странице
# https://openweathermap.org/current есть подробная доку-
# ментация как работать с API. Теперь после запроса от
# клиента необходимо получать данные о погоде с этого
# источника. Полученный результат возвращать клиенту.

# import requests
#
# def run_client():
#     base_url = 'http://127.0.0.1:5000/weather'
#
#     while True:
#         country = input('Введите название страны: ')
#         city = input('Введите название города: ')
#
#         params = {'country': country, 'city': city}
#
#         response = requests.get(base_url, params=params)
#
#         if response.status_code == 200:
#
#             weather_data = response.json()
#
#             if weather_data:
#
#                 print('Прогноз погоды для', city + ',', country + ':')
#                 for day, forecast in weather_data.items():
#                     print(day, '-', forecast)
#             else:
#                 print('Данные о погоде не найдены.')
#         else:
#             print('Ошибка при выполнении запроса.')
#
# if __name__ == '__main__':
#     run_client()
