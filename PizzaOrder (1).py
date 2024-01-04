import random

# SC1
class Pizza:
    # SC3
    def __init__(self, menu_code, pizza_name, inventory_count, price):
        self.menu_code = menu_code
        self.pizza_name = pizza_name
        self.inventory_count = inventory_count
        self.price = price

    # SC4
    def toString(self):
        return f"Menu Code: {self.menu_code}, Pizza Name: {self.pizza_name}, Inventory Count: {self.inventory_count}, Price: {self.price}"

    # SC12 (modified)
    def __str__(self):
        return self.toString()

# SC
def get_integer_input(prompt, error_message, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                raise ValueError(f"Error: Please enter a number between {min_value} and {max_value}.")
        except ValueError as e:
            print(error_message)
            print(e)

# SC11
def create_pizza():
    menu_code = input("Please enter a three-letter/number menu code: ")
    # SC9
    pizza_name = input("Please enter the pizza name: ")
    # SC10 # SC7
    inventory_count = get_integer_input("Please enter the total inventory count: ",
                                        "Error: Inventory count cannot be negative.", 0, float('inf'))
    # SC2 # SC5
    price = round(random.uniform(10, 20), 2)
    return Pizza(menu_code, pizza_name, inventory_count, price)

# SC11
def main():
    try:
        create_pizza_count = get_integer_input("How many simulated frozen pizza items do you want to create? (1-10): ",
                                               "Error: You must enter a number between 1 and 10.", 1, 10)
        print("You entered:", create_pizza_count)
    except ValueError as e:
        print(e)
        exit()

    pizzas_list = []
    for i in range(1, create_pizza_count + 1):
        print(f"\nPizza number {i}:")
        pizza = create_pizza()
        pizzas_list.append(pizza)

    # SC12
    print("\nListed below is your current pizza inventory:")
    for pizza in pizzas_list:
        print(pizza)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
