import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en")


@pytest.fixture(scope="function")
def browser(request):
    languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en "
    language = request.config.getoption("language")
    if (language + " ") in languages:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1280, 1280)

    else:
        print("\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en".format(language))
        pytest.fail("Wrong Language")
        # assert 0
    yield browser
    print("\nquit browser..")
    browser.quit()