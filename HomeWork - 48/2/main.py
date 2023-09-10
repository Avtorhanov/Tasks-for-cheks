from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('.'))

products = [
    {'name': 'Product A', 'price': 55},
    {'name': 'Product B', 'price': 15},
    {'name': 'Product C', 'price': 25},
]

tm = env.get_template('product_list.html')
msg = tm.render(products=products)
print(msg)
