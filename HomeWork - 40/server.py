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
# def run_server():
#     host = '127.0.0.1'
#     port = 12345
#
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     server_socket.bind((host, port))
#
#     server_socket.listen(1)
#     print('Сервер запущен и ожидает подключения...')
#     while True:
#
#         client_socket, addr = server_socket.accept()
#         print('Подключение установлено:', addr)
#
#         handle_connection(client_socket)
# def handle_connection(client_socket):
#     while True:
#
#         data = client_socket.recv(1024)
#         if not data:
#             break
#
#         message = data.decode()
#         print('Получено сообщение от клиента:', message)
#
#         response = 'Сообщение получено: ' + message
#         client_socket.send(response.encode())
#
#     client_socket.close()
# if __name__ == '__main__':
#     run_server()


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

# from flask import Flask, request, jsonify
# import json
# from threading import Lock
#
# app = Flask(__name__)
# lock = Lock()
#
# def load_weather_data():
#     with open('weather_data.json', 'r') as file:
#         data = json.load(file)
#     return data
#
# @app.route('/weather', methods=['GET'])
# def get_weather():
#     country = request.args.get('country')
#     city = request.args.get('city')
#
#
#     weather_data = get_weather_data_from_source(country, city)
#
#     return jsonify(weather_data)
#
# def get_weather_data_from_source(country, city):
#
#     with lock:
#         weather_data = load_weather_data()
#         if country in weather_data and city in weather_data[country]:
#             return weather_data[country][city]
#
#
#     return {}
#
# if __name__ == '__main__':
#     app.run()
