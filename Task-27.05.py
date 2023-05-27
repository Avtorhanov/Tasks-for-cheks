# # Задание
# # Создайте приложение для эмуляции работы пиццерии.
# # Приложение должно иметь следующую функциональность:
# # 1. Пользователь может выбрать из пяти стандартных
# # рецептов пиццы или создать свой рецепт.
# # 2. Пользователь может выбирать добавлять ли топпин-
# # ги (сладкий лук, халапеньо, чили, соленный огурец,
# # оливки, прошутто и т.д.).
# # 3. Информацию о заказанной пицце нужно отображать
# # на экран и сохранять в файл.
# # 4. Расчет может производиться, как наличными, так и
# # картой.
# # 5. Необходимо иметь возможность просмотреть коли-
# # чество проданных пицц, выручку, прибыль.
# # 6. Классы приложения должны быть построены с уче-
# # том принципов SOLID и паттернов проектирования
#
from abc import ABC, abstractmethod
import pickle


class Pizza(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Margherita(Pizza):
    def get_name(self):
        return "Margherita"

    def get_price(self):
        return 10.0


class Pepperoni(Pizza):
    def get_name(self):
        return "Pepperoni"

    def get_price(self):
        return 12.0


class Hawaiian(Pizza):
    def get_name(self):
        return "Hawaiian"

    def get_price(self):
        return 11.0


class CustomPizza(Pizza):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price


class Topping(ABC):
    @abstractmethod
    def get_name(self):
        pass


class Onion(Topping):
    def get_name(self):
        return "Onion"


class Jalapeno(Topping):
    def get_name(self):
        return "Jalapeno"


class Chili(Topping):
    def get_name(self):
        return "Chili"


class Cucumber(Topping):
    def get_name(self):
        return "Cucumber"


class Olive(Topping):
    def get_name(self):
        return "Olive"


class Prosciutto(Topping):
    def get_name(self):
        return "Prosciutto"


class Order:
    def __init__(self):
        self.pizzas = []
        self.toppings = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def add_topping(self, topping):
        self.toppings.append(topping)


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):
    def pay(self, amount):
        return f"Payment successful. Change: {amount}"


class CardPayment(Payment):
    def pay(self, amount):
        return "Payment successful"


class Statistics:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_total_pizzas_sold(self):
        return sum(len(order.pizzas) for order in self.orders)

    def get_total_revenue(self):
        return sum(sum(pizza.get_price() for pizza in order.pizzas) for order in self.orders)

    def get_total_profit(self, costs):
        return self.get_total_revenue() - costs * self.get_total_pizzas_sold()


def save_orders(orders):
    with open('orders.pkl', 'wb') as file:
        pickle.dump(orders, file)


def load_orders():
    try:
        with open('orders.pkl', 'rb') as file:
            orders = pickle.load(file)
            return orders
    except FileNotFoundError:
        return []


def display_statistics(statistics):
    print("---- Statistics ----")
    print("Total pizzas sold:", statistics.get_total_pizzas_sold())
    print("Total revenue:", statistics.get_total_revenue())
    print("Total profit:", statistics.get_total_profit(10))


def main():
    menu = [
        Margherita(),
        Pepperoni(),
        Hawaiian()
    ]

    orders = load_orders()
    statistics = Statistics()

    payment_methods = {
        "cash": CashPayment(),
        "card": CardPayment()
    }

    while True:
        print("---- Pizza Emulator App ----")
        print("1. Display menu")
        print("2. Create an order")
        print("3. View statistics")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("---- Menu ----")
            for i, pizza in enumerate(menu, start=1):
                print(f"{i}. {pizza.get_name()} - ${pizza.get_price()}")
            print()

        elif choice == "2":
            order = Order()
            print("---- Create an Order ----")
            while True:
                print("---- Menu ----")
                for i, pizza in enumerate(menu, start=1):
                    print(f"{i}. {pizza.get_name()} - ${pizza.get_price()}")
                print("0. Finish order")
                pizza_choice = input("Enter pizza number (0 to finish order): ")

                if pizza_choice == "0":
                    break

                try:
                    pizza_index = int(pizza_choice) - 1
                    pizza = menu[pizza_index]
                    order.add_pizza(pizza)
                except (ValueError, IndexError):
                    print("Invalid input. Please try again.")

            while True:
                print("---- Toppings ----")
                print("1. Onion")
                print("2. Jalapeno")
                print("3. Chili")
                print("4. Cucumber")
                print("5. Olive")
                print("6. Prosciutto")
                print("0. Finish adding toppings")
                topping_choice = input("Enter topping number (0 to finish): ")

                if topping_choice == "0":
                    break

                try:
                    topping_index = int(topping_choice)
                    if 1 <= topping_index <= 6:
                        topping = [
                            Onion(),
                            Jalapeno(),
                            Chili(),
                            Cucumber(),
                            Olive(),
                            Prosciutto()
                        ][topping_index - 1]
                        order.add_topping(topping)
                    else:
                        print("Invalid input. Please try again.")
                except ValueError:
                    print("Invalid input. Please try again.")

            payment_method = input("Enter payment method (cash or card): ")
            payment = payment_methods.get(payment_method.lower())
            if payment:
                amount = sum(pizza.get_price() for pizza in order.pizzas)
                payment_result = payment.pay(amount)
                print(payment_result)
                orders.append(order)
                statistics.add_order(order)
                save_orders(orders)
                print("Order placed successfully.")
            else:
                print("Invalid payment method. Please try again.")

            print()

        elif choice == "3":
            display_statistics(statistics)
            print()

        elif choice == "4":
            break

        else:
            print("Invalid input. Please try again.")
            print()


if __name__ == "__main__":
    main()
