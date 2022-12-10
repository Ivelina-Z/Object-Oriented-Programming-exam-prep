from food_order_app.project.client import Client


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if self.__find_client_by_phone_number(client_phone_number):
            raise Exception('The client has already been registered!')
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f'Client {client_phone_number} registered successfully.'

    def add_meals_to_menu(self, *meals):
        accepted_meals = ['Starter', 'MainDish', 'Dessert']
        [self.menu.append(meal) for meal in meals if meal.__class__.__name__ in accepted_meals]

    def show_menu(self):
        if self.__check_if_menu_ready():
            return '\n'.join([dish.details() for dish in self.menu])
        raise Exception('The menu is not ready!')

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if not self.__check_if_menu_ready():
            raise Exception('The menu is not ready!')

        client = self.__find_client_by_phone_number(client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            meal = self.__find_meal_by_name(meal_name)
            if not meal:
                self.__clear_cart(client)
                raise Exception(f'{meal_name} is not on the menu!')

            if meal.quantity < meal_quantity:
                self.__clear_cart(client)
                raise Exception(f'Not enough quantity of {meal.__class__.__name__}: {meal_name}!')

            client.shopping_cart.append(meal)
            meal.quantity -= meal_quantity
            meal.ordered += meal_quantity
            client.bill += meal.price * meal_quantity
        return f'Client {client.phone_number} successfully ordered {", ".join([meal.name for meal in client.shopping_cart])} for {client.bill:.2f}lv.'

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        self.__clear_cart(client)
        return f'Client {client.phone_number} successfully canceled his order.'

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        paid_money = client.bill
        self.__clear_cart(client)
        receipt_id = self.__get_receipt_id()
        return f'Receipt #{receipt_id} with total amount of {paid_money:.2f} was successfully paid for {client_phone_number}.'

    def __find_client_by_phone_number(self, phone_number):
        client = next(filter(lambda c: c.phone_number == phone_number, self.clients_list), None)
        return client

    def __find_meal_by_name(self, meal_name):
        meal = next(filter(lambda m: m.name == meal_name, self.menu), None)
        return meal

    def __check_if_menu_ready(self):
        if len(self.menu) >= 5:
            return True

    @staticmethod
    def __get_receipt_id():
        FoodOrdersApp.receipt_id += 1
        return FoodOrdersApp.receipt_id

    @staticmethod
    def __clear_cart(client, finish_order=False):
        if not client.shopping_cart:
            raise Exception('There are no ordered meals!')
        if not finish_order:
            for meal in client.shopping_cart:
                meal.quantity += meal.ordered
                meal.ordered = 0
        client.shopping_cart.clear()
        client.bill = 0.0

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'
