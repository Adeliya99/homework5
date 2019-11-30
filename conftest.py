import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or en")


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def language(request, browser):
    language_name = request.config.getoption("language")
    link = None
    if language_name == "es":
        print("\nstart test in es..")
        link = "http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/"
        browser.get(link)
    elif language_name == "fr":
        print("\nstart test in fr..")
        link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
    else:
        raise pytest.UsageError("--language_name should be es or fr")
