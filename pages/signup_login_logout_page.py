from .base_page import BasePage
from .locators import SignupLoginLogoutLocators
from .locators import BasePageLocators
from ..settings import main_settings


class SignupLoginLogoutPage(BasePage):

    def login_to_front_from_promo(self, request, browser):
        self.email = request.config.getoption("login")
        self.password = request.config.getoption("password")
        self.go_to_front_from_promo()
        self.explicit_wait_login_form(browser)
        self.login_exist_user_to_front()
        self.explicit_wait_whatsnewdemoreminder_popup(browser)
        self.close_whatsnewdemoreminder_popup()
        self.should_be_authorized_user_to_front()

    def click_on_header_button_authenticated(self):
        self.browser.find_element(*SignupLoginLogoutLocators.HEADER_BUTTON_AUTHENTICATED).click()

    def click_on_logout_from_front(self):
        self.browser.find_element(*SignupLoginLogoutLocators.HEADER_BUTTON_LOGOUT).click()

    def should_be_unauthorized(self):
        assert self.is_element_present(*SignupLoginLogoutLocators.EMAIL_FIELD), "Login Form Auth0 is presented" \
                                                  "Login Form Auth0 is NOT presented"

    def go_to_front_from_promo(self):
        self.browser.find_element(*SignupLoginLogoutLocators.LOGIN_BUTTON_FROM_PROMO).click()

    def login_exist_user_to_front(self):
        """ Логин существующего юзера """
        self.browser.find_element(*SignupLoginLogoutLocators.EMAIL_FIELD).send_keys(self.email)
        if self.password:
            self.browser.find_element(*SignupLoginLogoutLocators.PASS_FIELD).send_keys(self.password)
        self.browser.find_element(*SignupLoginLogoutLocators.LOGIN_BUTTON).click()
        if self.browser.find_elements(*SignupLoginLogoutLocators.LOGIN_PASSWORD_INVALID):
            print(f"\nLogin/Password is Invalid")
        if self.browser.find_elements(*SignupLoginLogoutLocators.LOGIN_PASSWORD_INCORRECT):
            print(f"\nLogin/Password is Incorrect")

    def explicit_wait_login_form(self, browser, explicit_wait_sec=main_settings.EXPLICIT_WAIT):
        locator = SignupLoginLogoutLocators.LOGIN_BUTTON
        self.explicit_wait(browser, explicit_wait_sec, locator)

    def explicit_wait_whatsnewdemoreminder_popup(self, browser, explicit_wait_sec=main_settings.EXPLICIT_WAIT):
        locator = SignupLoginLogoutLocators.POPUP_CLOSE
        self.explicit_wait(browser, explicit_wait_sec, locator)

    def close_whatsnewdemoreminder_popup(self):
        self.browser.find_element(*SignupLoginLogoutLocators.POPUP_CLOSE).click()

    def should_be_authorized_user_to_front(self):
        locator = BasePageLocators.USER_EMAIL_IN_HEADER
        self.should_be_authorized_user(locator)
