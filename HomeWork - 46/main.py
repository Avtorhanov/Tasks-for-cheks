import sqlite3
from faker import Faker
import random
import datetime

fake = Faker('ru_RU')

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Создаем таблицу "Users" с фейковыми данными
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        age INTEGER CHECK (age >= 18),
        registration_date DATE DEFAULT (DATE('now'))
    )
""")

# Создаем таблицу "Posts" с фейковыми данными
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Posts (
        post_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT NOT NULL,
        content TEXT,
        post_date DATE DEFAULT (DATE('now')),
        FOREIGN KEY (user_id) REFERENCES Users (user_id)
    )
""")

for _ in range(10):
    username = fake.user_name()
    email = fake.email()
    age = random.randint(18, 65)
    cursor.execute("""
        INSERT INTO Users (username, email, age) VALUES (?, ?, ?)
    """, (username, email, age))

for _ in range(20):
    user_id = random.randint(1, 10)
    title = fake.sentence()
    content = fake.text()
    post_date = fake.date_between(start_date='-1y', end_date='today')
    cursor.execute("""
        INSERT INTO Posts (user_id, title, content, post_date) VALUES (?, ?, ?, ?)
    """, (user_id, title, content, post_date))

conn.commit()
conn.close()
