# conftest.py
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
    driver.get("https://www.imdb.com/search/name/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
