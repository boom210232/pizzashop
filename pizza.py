from enum import Enum


class PizzaSize(Enum):
    small = {'base_price': 120, 'topping': 20}
    medium = {'base_price': 200, 'topping': 25}
    large = {'base_price': 300, 'topping': 30}
    jumbo = {'base_price': 450, 'topping': 45}

    @property
    def price(self):
        return self.value['base_price']

    @property
    def topping_price(self):
        return self.value['topping']


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size: PizzaSize):
        if not isinstance(size, PizzaSize):
            raise TypeError("size must me PizzaSize")
        self.size = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        # Explanatory or inline are optional. (I choose in inline.)
        return self.size.price + self.size.topping_price * len(self.toppings)

    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self):
        # return a printable description of the pizza such as
        # "small pizza with mushroom" or "small plain pizza"
        description = self.size.name
        if self.toppings:
            description += " pizza with " + ", ".join(self.toppings)
        else:
            description += " plain cheese pizza"
        return description
