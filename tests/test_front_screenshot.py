from ..pages.signup_login_logout_page import SignupLoginLogoutPage
from ..pages.front_screenshot_page import FrontScreenshotPage
from ..settings import main_settings
from ..telegram import telebot
import pytest
import time


class TestFrontScreenshots():

    def setup(self):
        self.link_to_promo = (f"{main_settings.URL_PROMO}")
        self.link_to_front = (f"{main_settings.URL_FRONT}")
        self.test_url = main_settings.SCREENSHOT_TEST_URL
        self.timeout = main_settings.TIMEOUT_CREATE_SCREENSHOTS
        self.screenshot_filename = main_settings.SCREENSHOT_NAME
        self.header_report_to_telegram = "Screenshots web testing"

    @pytest.mark.monitoring
    def test_make_screenshots(self, browser, request):
        page = SignupLoginLogoutPage(browser, self.link_to_promo)
        page.open()
        page.login_to_front_from_promo(request, browser)
        page = FrontScreenshotPage(browser, self.link_to_front)
        page.set_test_url(self.test_url)
        page.select_custom_width(request.config.getoption("width"))
        if request.config.getoption("os"): page.select_custom_os(request.config.getoption("os"))
        elif request.config.getoption("browser"): page.select_custom_browser(request.config.getoption("browser"))
        else: page.select_all_configs()
        page.press_btn_create_screenshots()
        time.sleep(self.timeout)
        page.make_screenshot(self.screenshot_filename)
        report_txt = page.make_log_report_created_screenshots(self.header_report_to_telegram)
        if request.config.getoption("telechat") and request.config.getoption("teletoken"):
            telebot.Telebot(request.config.getoption("telechat"), request.config.getoption("teletoken")).send_report_to_telegram(self.screenshot_filename, report_txt)
            print(report_txt)
        else: print(report_txt)
















