from enum import Enum

class BaseEnum(Enum):
    """
    The different base options for a Pizza
    """
    REGULAR = 0,
    WHOLEWHEAT = 1,
    CAULIFLOWER = 2


class ToppingEnum(Enum):
    """
    The different topping options for a Pizza
    """
    RED_ONION = 0,
    PEPPERS = 1,
    SPINACH = 2,
    MUSHROOM = 3,
    PEPPERONI = 4,
    CHICKEN = 5,
    BACON = 6,
    BEYOND_MEAT = 7,
    PINEAPPLE = 8


class CheeseEnum(Enum):
    """
    The different Cheese options for a Pizza
    """
    PARMESAN = 0,
    MOZZARELLA = 1,
    VEGAN_CHEESE = 2


class SauceEnum(Enum):
    """
    The different sauce options for a Pizza.
    """
    TOMATO = 0,
    ALFREDO = 1,
    BBQ = 2

class Pizza():
    """
    As a contrived example let's look at a Pizza. as a complex object
    the pizza can have multiple toppins, cheeses, a base and even be
    "half and half" , that is have 2 pizza's in one or even be folded
    into a calzone.
    """

    def __init__(self, base, is_halfnhalf, sauce_1, sauce_2,
                 toppings_1, toppings_2, cheese_1, cheese_2,
                 is_calzone) -> None:
        self.base = None
        self.sauce_1 = None
        self.sauce_2 = None
        self.toppings_1 = []
        self.toppings_2 = []
        self.cheeses_1 = []
        self.cheeses_2 = []
        self.is_halfnhalf = is_halfnhalf
        self.is_calzone = None

p = Pizza(BaseEnum.WHOLEWHEAT, SauceEnum.TOMATO, SauceEnum.BBQ,
          ToppingEnum.PEPPERONI, ToppingEnum.SPINACH, CheeseEnum.MOZZARELLA, CheeseEnum.PARMESAN,
          False)