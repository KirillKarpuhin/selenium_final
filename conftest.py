import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    # Добавляем параметр для выбора браузера
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    
    # Добавляем параметр для выбора языка
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, fr, ru, etc.")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра browser_name
    browser_name = request.config.getoption("browser_name")
    
    # Получаем значение параметра language
    user_language = request.config.getoption("language")
    
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        
        # Настройки для Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        
        # Настройки для Firefox
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()

# 2 фикстуры: для запуска опреденного браузера и для выбора языка
# запуск происходит pytest --language=es --browser_name=chrome -s -v test_items.py