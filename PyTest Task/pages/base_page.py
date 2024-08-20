# pages/base_page.py

# Using Page Object Model (POM), Explicit Wait, Expected Conditions, Pytest kindly do the following task as mentioned below :-
# 1) Go to https://www.imdb.com/search/name/
# 2) Fill the data given in the Input Boxes, Select Boxes and Drop Down menu on the webpage and do a search
# 3) Do not use the sleep() method for the task.


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def scroll_into_view(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)