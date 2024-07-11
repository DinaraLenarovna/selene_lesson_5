import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    # browser.config.timeout = 2.0
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')  # вместо этой строки можно добавить другие опции
    browser.config.driver_options = driver_options

    yield

    browser.quit()


