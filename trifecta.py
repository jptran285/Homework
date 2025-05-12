class IceStorm:
    FLAVOR_PRICES = {
        "Mint Chocolate Chip": 4.00,
        "Chocolate": 3.00,
        "Vanilla Bean": 3.00,
        "Banana": 3.50,
        "Butter Pecan": 3.50,
        "S'more": 4.00
    }

    TOPPING_PRICES = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Storios": 1.00,
        "Dig Dogs": 1.00,
        "T&T's": 1.00,
        "Cookie Dough": 1.00,
        "Pecans": 0.50
    }

    def __init__(self, base="Ice Cream", size="Regular"):
        self.base = base
        self.size = size
        self.flavors = []
        self.toppings = []

    def add_flavor(self, flavor):
        if flavor in self.FLAVOR_PRICES:
            self.flavors.append(flavor)

    def get_flavors(self):
        return self.flavors

    def get_num_flavors(self):
        return len(self.flavors)

    def add_topping(self, topping):
        if topping in self.TOPPING_PRICES:
            self.toppings.append(topping)

    def get_toppings(self):
        return self.toppings

    def get_base(self):
        return self.base

    def get_size(self):
        return self.size

    def get_total(self):
        total = sum(self.FLAVOR_PRICES[f] for f in self.flavors)
        total += sum(self.TOPPING_PRICES[t] for t in self.toppings)
        return total

    def __str__(self):
        result = f"{self.size} {self.base} Ice Storm\n"
        result += f"Flavors: {', '.join(self.flavors)}\n"
        if self.toppings:
            result += f"Toppings: {', '.join(self.toppings)}\n"
        result += f"Total: ${self.get_total():.2f}"
        return result


# Example usage
if __name__ == "__main__":
    ice_storm = IceStorm()
    ice_storm.add_flavor("Chocolate")
    ice_storm.add_flavor("Banana")
    ice_storm.add_topping("Chocolate Sauce")
    ice_storm.add_topping("Storios")
    print(ice_storm)
