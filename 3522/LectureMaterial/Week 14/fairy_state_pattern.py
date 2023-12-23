"""
State Pattern in game with fairies that can change between elemental states
"""

import abc
import enum

# enums to easily represent each element
class Element(enum.Enum):
    FIRE = 1
    WATER = 2
    WIND = 3
    NONE = 4

class Fairy:

    static_id = 1
    """
    Fairy is the context. This will be the container that changes its states
    """
    def __init__(self, state):
        self.id = Fairy.static_id
        Fairy.static_id += 1
        self.health = 100
        self.attack_power = 10
        self.state = None
        self.change_state(state)

    def change_state(self, state):
        """
        Changes the fairy's state and make the state reference back to this fairy
        """
        self.state = state
        self.state.fairy = self
        print(f"Fairy({self.id}) changed to {state.element.name} element")

    def attack(self, enemy_fairy):
        """
        Attack function relies on the state to perform the actual attack logic
        """
        self.state.attack(enemy_fairy)

    def take_damage(self, damage):
        self.health -= damage

    def print_health(self):
        print(f"Fairy({self.id})'s health: {self.health}")

    def get_element(self):
        return self.state.element

    def __str__(self):
        return f"{self.get_element().name} Fairy({self.id})"

class State(abc.ABC):
    """
    The abstract state class that contains references back to the context
    and methods to set the context
    """

    def __init__(self):
        self.fairy = None
        self.element = Element.NONE

    def set_fairy(self, fairy):
        self.fairy = fairy

    @abc.abstractmethod
    def strong_against(self, enemy_fairy):
        """
        Checks if this enemy's element is a specific weaker type
        """
        pass

    @abc.abstractmethod
    def attack(self, enemy_fairy):
        damage = self.fairy.attack_power
        double_string = ""

        if self.strong_against(enemy_fairy):
            damage *= 2
            double_string = " CRITICAL"

        print(f"{self.fairy} attacks {enemy_fairy}"
              f" for{double_string} damage: {damage}!")
        enemy_fairy.take_damage(damage)


class FireState(State):
    """
    The concrete state. Each state sets its unique values and provides
    the attack function that fairy will eventually call to perform the attack logic
    """
    def __init__(self):
        super()
        self.element = Element.FIRE

    def strong_against(self, enemy_fairy):
        return enemy_fairy.get_element() == Element.WIND

    def attack(self, enemy_fairy):
        super().attack(enemy_fairy)

        if self.strong_against(enemy_fairy):
            enemy_fairy.change_state(FireState())  # enemy fairy changes state when receiving critical damage


class WaterState(State):
    """
    The concrete state. Each state sets its unique values and provides
    the attack function that fairy will eventually call to perform the attack logic
    """
    def __init__(self):
        super()
        self.element = Element.WATER

    def strong_against(self, enemy_fairy):
        return enemy_fairy.get_element() == Element.FIRE

    def attack(self, enemy_fairy):
        super().attack(enemy_fairy)

        if self.strong_against(enemy_fairy):
            enemy_fairy.change_state(WaterState())  # enemy fairy changes state when receiving critical damage

class WindState(State):
    """
    The concrete state. Each state sets its unique values and provides
    the attack function that fairy will eventually call to perform the attack logic
    """
    def __init__(self):
        super()
        self.element = Element.WIND

    def strong_against(self, enemy_fairy):
        return enemy_fairy.get_element() == Element.WATER

    def attack(self, enemy_fairy):
        super().attack(enemy_fairy)

        if self.strong_against(enemy_fairy):
            enemy_fairy.change_state(WindState())  # enemy fairy changes state when receiving critical damage


def main():
    print("---INITIALIZING TWO FAIRIES AND THEIR STATES---")
    # create the first fairy and its states
    fire_state = FireState()
    water_state = WaterState()
    wind_state = WindState()
    fairy = Fairy(fire_state) #sets the initial state of the fairy to fire

    # create the second fairy and its states
    fire_state_2 = FireState()
    water_state_2 = WaterState()
    wind_state_2 = WindState()
    fairy2 = Fairy(wind_state_2) #sets the initial state of the fairy to wind
    fairy.print_health()
    fairy2.print_health()

    print("\n---FAIRIES BEGIN ATTACKING---")
    # fire fairy attacks wind fairy. Fire does double damage to wind
    # Wind fairy will change to Fire type within the state
    fairy.attack(fairy2)
    fairy.print_health()
    fairy2.print_health()

    print("\n---FAIRIES CHANGE STATES AND ATTACKING---")
    #fire fairy now changes to a wind fairy
    fairy.change_state(wind_state)

    # water fairy attacks wind fairy. water does normal damage to wind
    fairy.attack(fairy2)
    fairy.print_health()
    fairy2.print_health()


if __name__ == '__main__':
    main()