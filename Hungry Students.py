class Topping:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"{self.name} - ${self.cost:.2f}"


class Item:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def get_price(self):
        return self.base_price + sum(t.cost for t in self.toppings)

    def get_type(self):
        return "Generic Item"

    def get_receipt_line(self):
        lines = [f"{self.name} ({self.get_type()}) - ${self.get_price():.2f}"]
        for topping in self.toppings:
            lines.append(f"  + {topping}")
        return "\n".join(lines)


class Food(Item):
    def get_type(self):
        return "Food"


class Drink(Item):
    def get_type(self):
        return "Drink"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total(self):
        return sum(item.get_price() for item in self.items)

    def generate_receipt(self):
        receipt = ["=== Cinos Receipt ==="]
        for item in self.items:
            receipt.append(item.get_receipt_line())
        receipt.append("----------------------")
        receipt.append(f"Total: ${self.get_total():.2f}")
        return "\n".join(receipt)


# Topping cost lookup
TOPPING_PRICES = {
    "cherry": 0.00,
    "whipped cream": 0.00,
    "caramel sauce": 0.50,
    "chocolate sauce": 0.50,
    "nacho cheese": 0.30,
    "chili": 0.60,
    "bacon bits": 0.30,
    "ketchup": 0.00,
    "mustard": 0.00,
}

def create_topping(name):
    name = name.lower()
    if name in TOPPING_PRICES:
        return Topping(name, TOPPING_PRICES[name])
    else:
        raise ValueError(f"Unknown topping: {name}")


# Example usage
if __name__ == "__main__":
    order = Order()

    hotdog = Food("Hotdog", 2.30)
    hotdog.add_topping(create_topping("ketchup"))
    hotdog.add_topping(create_topping("mustard"))

    fries = Food("French Fries", 1.50)
    fries.add_topping(create_topping("nacho cheese"))
    fries.add_topping(create_topping("chili"))

    milkshake = Drink("Milkshake", 3.00)
    milkshake.add_topping(create_topping("whipped cream"))
    milkshake.add_topping(create_topping("cherry"))

    order.add_item(hotdog)
    order.add_item(fries)
    order.add_item(milkshake)

    print(order.generate_receipt())
