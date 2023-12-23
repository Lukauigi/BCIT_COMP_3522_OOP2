import time
from enum import Enum

class ScreenEnum(Enum):
    MAIN_MENU = "Main Menu screen"
    GAMEPLAY = "Gameplay screen"

class Screen:
    """
    An expensive object that is computationally intensive.
    """

    def __init__(self, name):
        """
        Creating this object takes a while.
        """
        print(f"Loading {name}. This is a time consuming process")
        time.sleep(2)
        print("Wait for it...")
        time.sleep(1)
        print(f"{name} has been loaded")

class Game:

    def __init__(self):
        """
        The game has access to a screen. In Lazy Inititalization we don't
        initialize it outright.
        """
        print("Game initializing")

        #No initialization performed on screens yet. Set them to None for now
        self._main_menu_screen = None
        self._gameplay_screen = None

    def start(self):
        """
        When the screen is accessed we check to see if it is initialized.
        If it isn't initialized then we initialize it.
        This is lazy intialization. We have delayed the initialization
        of an expensive object until we needed it.
        """
        if not self._main_menu_screen:
            self._main_menu_screen = Screen(ScreenEnum.MAIN_MENU.value) #initialize main menu screen for the first time
        print("Execute start logic")

    def start_gameplay(self):
        """
        When the screen is accessed we check to see if it is initialized.
        If it isn't initialized then we initialize it.
        This is lazy intialization. We have delayed the initialization
        of an expensive object until we needed it.
        """
        if not self._gameplay_screen:
            self._gameplay_screen = Screen(ScreenEnum.GAMEPLAY.value) #initialize gameplay screen for the first time
        print("Execute gameplay logic")


def main():
    game = Game() #creates an instance of Game, BUT inside the game SCREENs are NOT initialized
    game.start() #initializes main menu screen

    #if we never access gameplay, we never have to make memory for the gameplay screen
    choice = int(input("***\n-Press 1 to start gameplay\n-Press 2 to exit game\n***"))

    if choice == 1:
        game.start_gameplay() #screen is initialized here when we access start gameplay for the first time

    print("***\nThanks for playing! Game exiting\n***")

if __name__ == '__main__':
    main()