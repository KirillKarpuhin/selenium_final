from selenium.common.exceptions import NoSuchElementException 

# базовая страница, от которой наследуются остальные классы и опишем вспомогательные методы для работы с драйвером.
class BasePage():
     # добавляем конструктор — метод, который вызывается, когда создаем объект. Он объявляется ключевым словом __init__
         # (параметры: экземпляр драйвера и url адрес). Внутри конструктора сохраняем эти данные как аттрибуты класса

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # добавим метод open. Он должен открывать нужную страницу в браузере, используя метод get(). open() может обращаться
    # к атрибутам класса: self.browser и self.url

    def open(self):
        self.browser.get(self.url)

    # Напишем вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать нам True или False    
    def __init__(self, browser, url, timeout=10): # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) 
     
    #  реализуем метод is_element_present, в котором будем перехватывать исключение.
    #  В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор). 
    #  Чтобы перехватывать исключение, нужна конструкция try/except: 
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException): # если не найдет кнопку, например, логина, то вернет сообщение об ошибке из main_page
            return False
        return True
    
    # Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 
    #from selenium.common.exceptions import имя_исключения