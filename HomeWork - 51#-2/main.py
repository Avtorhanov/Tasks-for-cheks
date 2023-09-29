from flask import Flask, render_template, request

import sqlite3

app = Flask(__name__)

DATABASE_NAME = 'app_data.db'

def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS grades
                 (subject TEXT PRIMARY KEY, grade INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS lessons_data
                 (subject TEXT PRIMARY KEY, topic TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS homework_data
                 (subject TEXT PRIMARY KEY, assignment TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Notes
                     (subject TEXT PRIMARY KEY, assignment TEXT)''')

    conn.commit()
    conn.close()

init_db()

menu = [
    {'name': 'Главная', 'url': '/'},
    {'name': 'Написать Учителю', 'url': '/teach'},
    {'name': 'Мои оценки', 'url': '/rating'},
    {'name': 'Классные занятия', 'url': '/lessons'},
    {'name': 'Домашняя работа', 'url': '/homework'},
    {'name': 'Заметки', 'url': '/notes'},
]

@app.route('/note/<subject>')
def note_details(subject):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT assignment FROM Notes WHERE subject = ?", (subject,))
    assignment = c.fetchone()
    conn.close()

    if assignment:
        return f"<h1>{subject}</h1><p>{assignment[0]}</p>"
    else:
        return "Заметка не найдена."


@app.route('/index')
@app.route('/')
def index():
    # Получим данные о заметках
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM Notes")
    notes = dict(c.fetchall())
    conn.close()

    return render_template('index.html', title='Главная', notes=notes)


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

        conn = sqlite3.connect(DATABASE_NAME)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO grades (subject, grade) VALUES (?, ?)", (subject, grade))
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM grades")
    grades = dict(c.fetchall())
    conn.close()

    return render_template('rating.html', title='Мои оценки', menu=menu, grades=grades)


@app.route('/lessons', methods=['GET', 'POST'])
def lessons():
    if request.method == 'POST':
        subject = request.form['subject']
        topic = request.form['topic']

        conn = sqlite3.connect(DATABASE_NAME)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO lessons_data (subject, topic) VALUES (?, ?)", (subject, topic))
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM lessons_data")
    lessons_data = dict(c.fetchall())
    conn.close()

    return render_template('lessons.html', title='Классные занятия', menu=menu, lessons_data=lessons_data)


@app.route('/homework', methods=['GET', 'POST'])
def homework():
    if request.method == 'POST':
        subject = request.form['subject']
        assignment = request.form['assignment']

        conn = sqlite3.connect(DATABASE_NAME)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO homework_data (subject, assignment) VALUES (?, ?)", (subject, assignment))
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM homework_data")
    homework_data = dict(c.fetchall())
    conn.close()

    return render_template('homework.html', title='Домашняя работа', menu=menu, homework_data=homework_data)

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        subject = request.form['subject']
        assignment = request.form['assignment']

        conn = sqlite3.connect(DATABASE_NAME)
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO Notes (subject, assignment) VALUES (?, ?)", (subject, assignment))
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM Notes")
    notes = dict(c.fetchall())
    conn.close()

    return render_template('notes.html', title='Мои заметки', menu=menu, notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
