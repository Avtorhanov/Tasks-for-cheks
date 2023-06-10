# Создание системы управления задачами
#
# 1) Создайте класс TaskManager с атрибутами для
# хранения задач и информации о пользователях.
#
# 2) Реализуйте методы в классе TaskManager, чтобы добавлять
# задачи, назначать задачи пользователям, помечать задачи как
# выполненные и отображать сведения о задачах.
#
# 3) Создайте класс User с атрибутами для информации о пользователе,
# такой как имя, адрес электронной почты и роль
# (например, администратор или обычный пользователь).
#
# 4) Реализуйте методы в классе User для создания учетных записей пользователей,
# обновления информации о пользователях и просмотра назначенных задач.
#
# 5) Примените соответствующие методы инкапсуляции для защиты
# конфиденциальной пользовательской информации и гарантируйте, что операции,
# связанные с задачами, могут выполняться только авторизованными пользователями.
#
# 6) Используйте наследование для создания специализированных
# пользовательских ролей с различными разрешениями и возможностями
# (например, администраторы могут назначать задачи,
# обычные пользователи могут только просматривать задачи).
#
# 7) Внедрите проверку данных, чтобы гарантировать, что назначения задач
# и пользовательские операции выполняются с допустимыми входными данными и ограничениями

class Task:
    def __init__(self, task_id, title, description):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.is_completed = False


class User:
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.users = []

    def add_task(self, task_id, title, description):
        task = Task(task_id, title, description)
        self.tasks.append(task)

    def assign_task(self, task_id, username):
        task = self.find_task_by_id(task_id)
        user = self.find_user_by_username(username)
        if task and user:

            print(f"Task '{task.title}' assigned to user '{user.username}'")
        else:
            print("Task or user not found")

    def mark_task_completed(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            task.is_completed = True
            print(f"Task '{task.title}' marked as completed")
        else:
            print("Task not found")

    def display_task_info(self, task_id):
        task = self.find_task_by_id(task_id)
        if task:
            print("Task Information:")
            print(f"ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Status: {'Completed' if task.is_completed else 'Pending'}")
        else:
            print("Task not found")

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


task_manager = TaskManager()

task_manager.add_task(1, "Task 1", "Do something")
task_manager.add_task(2, "Task 2", "Do something else")

user1 = User("John", "john@example.com", "admin")
user2 = User("Jane", "jane@example.com", "user")
task_manager.users.extend([user1, user2])

task_manager.assign_task(1, "John")

task_manager.mark_task_completed(1)

task_manager.display_task_info(1)
