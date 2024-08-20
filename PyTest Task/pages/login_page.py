# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    NAME_INPUT = (By.XPATH, "//*[@id='nameTextAccordion']//input")

    EXPAND_ALL = (By.XPATH,
                  '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button')

    NAME_SEARCHBAR = (By.XPATH, '//input[@data-testid="test-nametext"]')
    SEE_RESULTS_BUTTON = (By.XPATH, '/*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button')

    def input_name(self, name):
        self.enter_text(self.NAME_SEARCHBAR, name)

    def expand_all(self):
        self.click_element(self.EXPAND_ALL)

    def see_results(self):
        self.click_element(self.SEE_RESULTS_BUTTON)



