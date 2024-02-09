from pylenium.driver import Pylenium
import fw


class HerokuApp:

    def __init__(self, py: Pylenium):
        self.py = py

    def navigate_to_heroku(self):
        """
        Navigates to the HerokuApp page
        """
        self.py.visit("https://the-internet.herokuapp.com/")
        self.py.should().have_title("The Internet")

        return self

    def select_example(self, example: str):
        """
        Clicks on the add/remove elements link on the herokuapp page
        """

        self.py.get('a[href=' + f'"{example}"').click()
        self.py.url().endswith("{example}")
        return self

    def click_example_button(self, example: str):
        """
        Clicks on the buttons/boxes while on the specified example page
        """

        self.py.get(f'button[onclick="{example}"]').click()
        return self

    def store_example_button(self, example: str):
        """
        finds a button and store it to a variable for later use
        """

        buttons = self.py.find(f'button[onclick="{example}"]')
        buttonslength = buttons.length()
        return buttonslength

    def verify_dynamic_content(self):
        """
        verify dynamic content on the herokuapp page is populating
        """

        self.py.url().endswith("/dynamic_content")
        dynamic_content = len(self.py.get('.example #content').children()[0].children()[1].text())
        return dynamic_content

    def click_dropdown(self, example: str, number: int):
        """
        clicks the dropdown bar for the dropdown heorkuapp page and then selects one of the options in the dropdown list
        """

        self.py.get(f'select[id="{example}"]').click()
        self.py.get(f'option[value="{number}"]').click()
        self.py.get(f'option[value="{number}"][selected="selected"]').should().be_visible()

