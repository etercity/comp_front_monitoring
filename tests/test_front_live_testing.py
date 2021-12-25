from ..settings import main_settings
from ..pages.signup_login_logout_page import SignupLoginLogoutPage
from ..pages.front_live_testing_page import FrontLiveTestingPage
from ..telegram import telebot
import pytest


class TestFrontLiveTesting():

    def setup(self):
        self.link_to_promo = (f"{main_settings.URL_PROMO}")
        self.link_to_front = (f"{main_settings.URL_FRONT}")
        self.test_url = main_settings.LIVE_TEST_URL
        self.timeout = main_settings.TIMEOUT_CREATE_VNC
        self.configs_on_linux = main_settings.CONFIGS_ON_LINUX
        self.configs_on_windows = main_settings.CONFIGS_ON_WINDOWS

    @pytest.mark.monitoring
    def test_live_testing_on_linux(self, browser, request):
        page = SignupLoginLogoutPage(browser, self.link_to_promo)
        page.open()
        page.login_to_front_from_promo(request, browser)
        page = FrontLiveTestingPage(browser, self.link_to_front)
        page.open()
        page.click_to_tab_live_testing()
        page.set_test_url()
        if request.config.getoption("vnc_os") == "Linux": report_txt = page.create_vnc_sessions(main_settings.OS_LINUX)
        elif request.config.getoption("vnc_os") == "Windows": report_txt = page.create_vnc_sessions(main_settings.OS_WIN)
        else:
            report_txt = page.create_vnc_sessions(main_settings.OS_LINUX)
            if request.config.getoption("telechat") and request.config.getoption("teletoken"):
                telebot.Telebot(request.config.getoption("telechat"), request.config.getoption("teletoken")).sendMessage(report_txt)
            else: print(report_txt)
            report_txt = page.create_vnc_sessions(main_settings.OS_WIN)
        if request.config.getoption("telechat") and request.config.getoption("teletoken"):
            telebot.Telebot(request.config.getoption("telechat"), request.config.getoption("teletoken")).sendMessage(report_txt)
        else: print(report_txt)





