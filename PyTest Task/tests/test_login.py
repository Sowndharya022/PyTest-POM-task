# tests/test_login.py
import pytest


from pages.login_page import LoginPage
from selenium.common.exceptions import TimeoutException


@pytest.mark.usefixtures("setup")
class TestLoginFunctionality:

    def test_search_functionality(self):
        login_page = LoginPage(self.driver)

        try:
            # Navigate to the IMDB search page
            self.driver.get("https://www.imdb.com/search/name/")

            # Interact with the page elements
            login_page.scroll_into_view(login_page.NAME_INPUT)
            login_page.expand_all()
            login_page.input_name("Sowndharya M")
            login_page.see_results()

            print("Test executed successfully.")

        except TimeoutException:
            print("A timeout occurred during the test execution.")
