from ..settings import main_settings
from ..pages.signup_login_logout_page import SignupLoginLogoutPage
from ..pages.front_screenshot_page import FrontScreenshotPage
from ..telegram import telebot
import time


class TestFrontScreenshotBa():

    def setup(self):
        self.link_to_promo = (f"{main_settings.URL_PROMO}")
        self.link_to_front = (f"{main_settings.URL_FRONT}")
        self.screenshot_filename = main_settings.SCREENSHOT_BAA
        self.timeout = main_settings.TIMEOUT_CREATE_SCREENSHOTS
        self.header_report_to_telegram = "Screenshots with Basic Authentication"

    def test_make_screenshots_baa(self, browser, request):

        if request.config.getoption("test_url_baa") and request.config.getoption("login_baa") and request.config.getoption("password_baa"):
            page = SignupLoginLogoutPage(browser, self.link_to_promo)
            page.open()
            page.login_to_front_from_promo(request, browser)
            page = FrontScreenshotPage(browser, self.link_to_front)
            page.set_test_url(request.config.getoption("test_url_baa"))
            page.select_custom_width(request.config.getoption("width"))
            if request.config.getoption("os"): page.select_custom_os(request.config.getoption("os"))
            elif request.config.getoption("browser"): page.select_custom_browser(request.config.getoption("browser"))
            else: page.select_all_configs()
            page.click_on_ba()
            page.input_user_ba(request.config.getoption("login_baa"))
            page.input_password_ba(request.config.getoption("password_baa"))
            page.press_button_save_ba()
            page.press_btn_create_screenshots()
            time.sleep(self.timeout)
            page.make_screenshot(self.screenshot_filename)
            report_txt = page.make_log_report_created_screenshots(self.header_report_to_telegram)
            if request.config.getoption("telechat") and request.config.getoption("teletoken"):
                telebot.Telebot(request.config.getoption("telechat"), request.config.getoption("teletoken")).send_report_to_telegram(self.screenshot_filename, report_txt)
                print(report_txt)
            else: print(report_txt)
        else:
            print("One or more request parameter not set..")
            pass








