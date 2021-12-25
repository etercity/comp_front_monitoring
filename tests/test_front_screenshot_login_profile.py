from ..settings import main_settings
from ..pages.signup_login_logout_page import SignupLoginLogoutPage
from ..pages.front_screenshot_page import FrontScreenshotPage
from ..telegram import telebot
import time


class TestFrontScreenshotLoginProfile():

    def setup(self):
        self.link_to_promo = (f"{main_settings.URL_PROMO}")
        self.link_to_front = (f"{main_settings.URL_FRONT}")
        self.timeout = main_settings.TIMEOUT_CREATE_SCREENSHOTS
        self.explicit_wait_for_save_test_login_profile = main_settings.EXPLICIT_WAIT_FOR_SAVE_TEST_LOGIN_PROFILE
        self.screenshot_filename = main_settings.SCREENSHOT_LOGIN_PROFILE_NAME
        self.test_url = main_settings.SCREENSHOT_LOGIN_PROFILE_TEST_URL
        self.test_url_by_the_login_form = main_settings.SCREENSHOT_LOGIN_PROFILE_FORM_URL
        self.user_name_selector_value = main_settings.LOC_ELEMENT_USERNAME_FIELD
        self.password_selector_value = main_settings.LOC_ELEMENT_PASSWORD_FIELD
        self.login_button_selector_value = main_settings.LOC_ELEMENT_LOGIN_BUTTON
        self.username_creds = main_settings.LOGIN_TO_LOGIN_PROFILE_TEST_URL
        self.password_creds = main_settings.PASSWORD_TO_LOGIN_PROFILE_TEST_URL
        self.login_profile_name = main_settings.LOGIN_PROFILE_NAME
        self.header_report_to_telegram = "Screenshots with Login Profile"

    def test_make_screenshots_login_profile(self, browser, request):
        page = SignupLoginLogoutPage(browser, self.link_to_promo)
        page.open()
        page.login_to_front_from_promo(request, browser)
        page = FrontScreenshotPage(browser, self.link_to_front)
        page.set_test_url(self.test_url)
        page.click_on_login_profile()
        page.add_new_login_profile()
        page.input_url_by_the_login_form(self.test_url_by_the_login_form)
        page.press_button_next_in_login_profile()
        page.click_on_user_name_selector()
        page.select_user_name_selector()
        page.input_user_name_selector_value(self.user_name_selector_value)
        page.click_on_password_selector()
        page.select_password_selector()
        page.input_password_selector_value(self.password_selector_value)
        page.click_on_login_button_selector()
        page.select_login_button_selector()
        page.input_login_button_selector_value(self.login_button_selector_value)
        page.press_button_next_in_login_profile()
        page.input_username_creds(self.username_creds)
        page.input_password_creds(self.password_creds)
        page.press_button_next_in_login_profile()
        page.input_login_profile_name(self.login_profile_name)
        page.press_button_save_in_login_profile()
        time.sleep(self.explicit_wait_for_save_test_login_profile)
        if request.config.getoption("os"): page.select_custom_os(request.config.getoption("os"))
        elif request.config.getoption("browser"): page.select_custom_browser(request.config.getoption("browser"))
        else: page.select_all_configs()
        page.select_custom_width(request.config.getoption("width"))
        page.press_btn_create_screenshots()
        time.sleep(self.timeout)
        page.make_screenshot(self.screenshot_filename)
        report_txt = page.make_log_report_created_screenshots(self.header_report_to_telegram)
        page.click_test_url()
        page.click_on_login_profile()
        page.delete_test_login_profile(self.login_profile_name)
        page.confirm_delete_test_login_profile()
        if request.config.getoption("telechat") and request.config.getoption("teletoken"):
            telebot.Telebot(request.config.getoption("telechat"), request.config.getoption("teletoken")).send_report_to_telegram(self.screenshot_filename, report_txt)
            print(report_txt)
        else: print(report_txt)

