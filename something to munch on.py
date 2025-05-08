import unittest


class MenuItem:
    TOPPING_PRICES = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Nacho Cheese": 0.30,
        "Chili": 0.60,
        "Bacon Bits": 0.30,
        "Ketchup": 0.00,
        "Mustard": 0.00
    }

    def __init__(self, name, base_price, item_type):
        self.name = name
        self.base_price = base_price
        self.item_type = item_type
        self.toppings = []

    def add_topping(self, topping):
        if topping in self.TOPPING_PRICES:
            self.toppings.append(topping)

    def get_price(self):
        return self.base_price + sum(
            self.TOPPING_PRICES.get(t, 0.0) for t in self.toppings
        )

    def get_toppings(self):
        return self.toppings

    def get_topping_count(self):
        return len(self.toppings)

    def get_type(self):
        return self.item_type


class Food(MenuItem):
    FOOD_PRICES = {
        "Hotdog": 2.30,
        "Corndog": 2.00,
        "Ice Cream": 3.00,
        "Onion Rings": 1.75,
        "French Fries": 1.50,
        "Tater Tots": 1.70,
        "Nacho Chips": 1.90
    }

    def __init__(self, name):
        base_price = self.FOOD_PRICES.get(name, 0.0)
        super().__init__(name, base_price, "Food")


class Drink(MenuItem):
    def __init__(self, name, base_price):
        super().__init__(name, base_price, "Drink")


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        return sum(item.get_price() for item in self.items)

    def generate_receipt(self):
        lines = ["Receipt:"]
        for item in self.items:
            line = f"{item.get_type()} ({item.name}) - ${item.get_price():.2f}"
            if item.get_toppings():
                line += f" | Toppings: {', '.join(item.get_toppings())}"
            lines.append(line)
        lines.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    order = Order()

    drink = Drink("Cola", 1.75)
    drink.add_topping("Cherry")
    drink.add_topping("Whipped Cream")
    order.add_item(drink)

    food = Food("French Fries")
    food.add_topping("Nacho Cheese")
    food.add_topping("Chili")
    order.add_item(food)

    print(order.generate_receipt())


# Unit Test
class TestCinosOrderSystem(unittest.TestCase):
    def test_total_price(self):
        order = Order()
        d = Drink("Root Beer", 1.50)
        d.add_topping("Caramel Sauce")
        f = Food("Tater Tots")
        f.add_topping("Chili")
        order.add_item(d)
        order.add_item(f)
        expected = 1.50 + 0.50 + 1.70 + 0.60
        self.assertAlmostEqual(order.get_total(), expected)

    def test_receipt_contains_items(self):
        order = Order()
        d = Drink("Lemonade", 1.25)
        d.add_topping("Whipped Cream")
        f = Food("Hotdog")
        order.add_item(d)
        order.add_item(f)
        receipt = order.generate_receipt()
        self.assertIn("Lemonade", receipt)
        self.assertIn("Hotdog", receipt)
        self.assertIn("Total: $", receipt)


# Run tests if file is executed directly
if __name__ == "__main__":
    unittest.main(exit=False)
