from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..settings import main_settings


class BasePage():
    """Класс базовой страницы"""
    def __init__(self, browser, url):
        """Конструктор вызывающий браузер"""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(main_settings.IMPLICITLY_WAIT)

    def open(self):
        """ Открывает страницу в браузере """
        self.browser.get(self.url)

    def click_element(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True

    def get_text(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            return None

    def is_element_present(self, how, what):
        """ """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_appears_after_while(self, how, what, timeout):
        """ Ожидает, что в течении 10 секунд данный элемент будет расположен и виден. Если в течении 10 секунд не найден,
        кинет ошибку Timeout. Возвращает элемент как только найден, но не позднее 10 секунд."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """ Проверяет, что элемент не появился в течение timeout """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def waiting_for_element_hide_over_time(self, how, what, timeout):
        """Функция ожидания скрытия элемента на странице в течении времени Time"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self, locator):
        """ Проверяет, что пользователь залогинен """
        assert self.is_element_present(*locator), "User email is not presented" \
                                                                                " probably unauthorised user"

    def explicit_wait(self, browser, explicit_wait_sec, locator):
        """говорим Selenium проверять в течение N секунд, пока элемент не станет кликабельным"""
        WebDriverWait(browser, explicit_wait_sec).until(
            EC.element_to_be_clickable(locator)
        )

    def make_screenshot(self, screenshot_filename):
        """Set window size..."""
        total_width = self.browser.execute_script("return document.body.offsetWidth")
        total_height = self.browser.execute_script("return document.body.scrollHeight")
        """Scrolling..."""
        self.browser.set_window_size(total_width, total_height + 83)
        """Make screenshot and save it"""
        # self.browser.save_screenshot(f"{main_settings.SCREENSHOT_NAME}")
        self.browser.find_element_by_tag_name('body').screenshot(f"{screenshot_filename}")




