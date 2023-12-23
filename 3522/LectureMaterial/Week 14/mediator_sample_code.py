from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def notify(self, sender, **kwargs):
        pass


class Button:
    def __init__(self, light_color, mediator: Mediator):
        self.light_color = light_color
        self.mediator = mediator

    def on_press(self):
        #red button: self.light_color = "Red"
        self.mediator.notify(self, light_color=self.light_color)


class TrafficLight:
    """
    Traffic class responds
    """
    def __init__(self, mediator):
        self.text = "Traffic Light"
        self.mediator = mediator

    def display(self, light_color):
        print(f"{self.text}: {light_color}")
        self.mediator.notify(self, light_color=light_color)

class Car:
    """
    Car class responds to traffic light colors
    """
    def __init__(self):
        self.text = "Car is"

    def action(self, light_color):
        if light_color == "Red":
            print(f"{self.text}: {'Stopping'}")
        elif light_color == "Yellow":
            print(f"{self.text}: {'doing nothing'}")
        elif light_color == "Green":
            print(f"{self.text}: {'Going'}")


class ConcreteMediator(Mediator):
    def __init__(self):
        self.traffic_light = TrafficLight(self)
        self.red_button = Button("Red", self)
        self.yellow_button = Button("Yellow", self)
        self.green_button = Button("Green", self)
        self.car = Car()
        self.exit_screen = False

    def execute(self):
        while not self.exit_screen:
            print("\nWhat do you want to do?")
            print("1.Press Red Light")
            print("2.Press Yellow Light")
            print("3.Press Green Light")
            print("4.Exit program")

            choice = int(input())
            if choice == 1:
                self.red_button.on_press()
            elif choice == 2:
                self.yellow_button.on_press()
            elif choice == 3:
                self.green_button.on_press()
            else:
                self.exit_screen = True

    def notify(self, sender, **kwargs):
        if sender == self.red_button or \
            sender == self.yellow_button or \
                sender == self.green_button:
            self.traffic_light.display(**kwargs) #traffic light responds to button presses
        elif sender == self.traffic_light:
            self.car.action(**kwargs) #car responds to traffic light

def main():
    concrete_mediator = ConcreteMediator()
    concrete_mediator.execute()


if __name__ == '__main__':
    main()
