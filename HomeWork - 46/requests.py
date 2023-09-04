import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# 1. Получить список пользователей и количество их постов
cursor.execute("""
    SELECT Users.username, COUNT(Posts.post_id) AS post_count
    FROM Users
    LEFT JOIN Posts ON Users.user_id = Posts.user_id
    GROUP BY Users.username
    ORDER BY post_count DESC
""")

results = cursor.fetchall()
print("Список пользователей и количество их постов:")
for row in results:
    print(f"Пользователь: {row[0]}, Количество постов: {row[1]}")

# 2. Найти посты, написанные пользователями старше 30 лет
cursor.execute("""
    SELECT Users.username, Posts.title
    FROM Users
    JOIN Posts ON Users.user_id = Posts.user_id
    WHERE Users.age > 30
""")

results = cursor.fetchall()
print("\nПосты, написанные пользователями старше 30 лет:")
for row in results:
    print(f"Пользователь: {row[0]}, Заголовок поста: {row[1]}")

conn.close()
