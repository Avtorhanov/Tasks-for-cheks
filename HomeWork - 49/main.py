from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'Написать Учителю', 'url': '/teach'},
    {'name': 'Мои оценки', 'url': '/rating'},
    {'name': 'Классные занятия', 'url': '/lessons'},
    {'name': 'Домашняя работа', 'url': '/homework'},
]

# Пример данных для оценок
grades = {
    'Математика': 5,
    'Физика': 4,
    'Информатика': 5,
}

lessons_data = {
    'Информатика': 'Flask and Jinja2'
}

homework_data = {
    'Первое занятие': 'Приступить к занятию'
}

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/teach', methods=['GET', 'POST'])
def teach():
    if request.method == 'POST':
        return render_template('index.html', title='Главная', menu=menu)

    return render_template('teach.html', title='Опишите ваш вопрос')


@app.route('/rating', methods=['GET', 'POST'])
def rating():
    if request.method == 'POST':

        subject = request.form['subject']
        grade = int(request.form['grade'])
        grades[subject] = grade

    return render_template('rating.html', title='Мои оценки', menu=menu, grades=grades)


@app.route('/lessons', methods=['GET', 'POST'])
def lessons():
    if request.method == 'POST':

        subject = request.form['subject']
        topic = request.form['topic']
        lessons_data[subject] = topic

    return render_template('lessons.html', title='Классные занятия', menu=menu, lessons_data=lessons_data)


@app.route('/homework', methods=['GET', 'POST'])
def homework():
    if request.method == 'POST':
        subject = request.form['subject']
        assignment = request.form['assignment']

        homework_data[subject] = assignment

    return render_template('homework.html', title='Домашняя работа', menu=menu, homework_data=homework_data)

if __name__ == '__main__':
    app.run(debug=True)
