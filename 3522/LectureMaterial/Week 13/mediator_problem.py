import abc
from abc import ABC, abstractmethod

# Various UI components
class TextLabel:
    def __init__(self, text):
        self.text = text

    def display_text(self, text):
        self.text = text
        print(self.text)

class InputField(abc.ABC):
    def __init__(self):
        self.text = None

    @abc.abstractmethod
    def enter_data(self, credentials):
        pass

class UserIDInputField(InputField):

    def __init__(self, text_lbl: TextLabel):
        self.status_text = text_lbl
        self.text = None

    def enter_data(self, credentials):
        self.status_text.display_text("Enter user id:")
        self.text = input()

class UserPasswordInputField(InputField):

    def __init__(self, text_lbl: TextLabel):
        self.status_text = text_lbl
        self.text = None

    def enter_data(self, credentials):
        self.status_text.display_text("Enter user password:")
        self.text = input()

class Screen:
    def back(self):
        print("Going back from screen")

class LogInScreen(Screen):
    def log_in(self):
        print("Entered log in screen")

# More UI components that are TIGHTLY coupled with other UI components
class LogInButton:

    def __init__(self, login_screen: Screen, username_inputfield: UserIDInputField, pwd_inputfield: UserPasswordInputField):
        self.login_screen = login_screen
        self.username_inputfield = username_inputfield
        self.pwd_inputfield = pwd_inputfield
        self._login_text = TextLabel("Log in")

    def on_click(self, credentials: dict) -> bool:
        if credentials[self.username_inputfield.text] == self.pwd_inputfield.text:
            self.login_screen.log_in() #this button can ONLY be used with a login_screen
            return True
        return False


class ExitButton:

    def __init__(self, screen: Screen):
        self.screen = screen

    def on_click(self, credentials: dict):
        self.screen.back() #this button is tied to only interacting with the screen back function


def main():
    #create login screens
    login_screen = LogInScreen()

    #create buttons and labels used in buttons
    text_label = TextLabel("User id")
    username_input_field = UserIDInputField(text_label)
    text_label = TextLabel("User password")
    password_input_field = UserPasswordInputField(text_label)

    #hook up log in button to communicate with login screen, and input fields
    login_button = LogInButton(login_screen, username_input_field, password_input_field)

    #setup valid username and passwords
    credentials_db = {}
    credentials_db["aaa"] = "111"
    credentials_db["zorak_the_destroyer"] = "i_am_l33t"

    #allow user to attempt to log in
    username_input_field.enter_data(credentials_db)
    password_input_field.enter_data(credentials_db)

    try:
        #simulate user pressing log in button after entering username and password
        login_button.on_click(credentials_db)
    except Exception:
        print("Login failed")
    else:
        print("You logged in!!")




if __name__ == '__main__':
    main()

