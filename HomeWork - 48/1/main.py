from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(''))

users = [
    {'name': 'John Doe', 'email': 'john.doe@gmail.com'},
    {'name': 'Alice Smith', 'email': 'alice.smith@hotmail.com'},
    {'name': 'Bob Johnson', 'email': 'bob.johnson@gmail.com'},
    {'name': 'Sam Tarver', 'email': 'bob.tarver@gmail.com'},
]

tm = env.get_template('user_list.html')
msg = tm.render(users=users)

# 1. С записью в файл
with open('user_list_output.html', 'w')as file:
    file.write(msg)

# 2. С выводом в run
# tm = env.get_template('user_list.html')
# msg = tm.render(users=users)
# print(msg)