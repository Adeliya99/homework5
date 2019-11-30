import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_guest_should_see_add_button(language, browser):
    button = browser.find_element_by_css_selector("[class = 'btn btn-lg btn-primary btn-add-to-basket']")
    assert button.is_displayed(), "Button is not exist!"