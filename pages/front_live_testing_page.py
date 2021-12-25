from .base_page import BasePage
from ..settings import main_settings
from .locators import FrontLiveTestingLocators
import time
import datetime
from selenium.webdriver.common.by import By


class FrontLiveTestingPage(BasePage):

    def click_to_tab_live_testing(self):
        self.browser.find_element(*FrontLiveTestingLocators.LIVE_TESTING_TAB).click()

    def set_test_url(self):
        self.browser.find_element(*FrontLiveTestingLocators.FIELD_INPUT_TEST_URL).click()
        self.browser.find_element(*FrontLiveTestingLocators.FIELD_INPUT_TEST_URL).send_keys(main_settings.LIVE_TEST_URL)

    def create_vnc_sessions(self, platform):
        if platform == "Linux":
            configs = main_settings.CONFIGS_ON_LINUX
            vnc_os_tab = FrontLiveTestingLocators.VNC_LINUX_TAB
        elif platform == "Windows":
            configs = main_settings.CONFIGS_ON_WINDOWS
            vnc_os_tab = FrontLiveTestingLocators.VNC_WIN_TAB
        else:
            configs = ""
            vnc_os_tab = ""
            print(f"The Platform {platform} is not exist!")
        report_message = []
        i = 0
        for browser_name, browser_version in configs:
            i += 1
            self.browser.find_element(*vnc_os_tab).click()
            self.browser.find_element(*FrontLiveTestingLocators.CLICK_BROWSER_TAB).click()
            self.browser.find_element_by_xpath(f'//*[contains(text(), "{browser_name}")]').click()
            self.browser.find_element(*FrontLiveTestingLocators.CLICK_BROWSER_VERSION_TAB).click()
            self.browser.find_element_by_xpath(f'//*[contains(text(), "{browser_version}")]').click()
            self.browser.find_element(*FrontLiveTestingLocators.BUTTON_RUN_LIVE_TEST).click()
            self.waiting_for_element_hide_over_time(By.XPATH, FrontLiveTestingLocators.PRELOADER_WAIT_VNC, main_settings.TIMEOUT_CREATE_VNC)
            if self.is_element_present(By.XPATH, FrontLiveTestingLocators.TIMER_IN_VNC):
                time.sleep(main_settings.TIMEOUT_VNC_SESSION)
                tmp_success = (f"{i}. {browser_name} {browser_version} - Ok\n")
                print(tmp_success)
                report_message += [tmp_success]
                self.browser.find_element(*FrontLiveTestingLocators.CLOSE_VNC_SESSION).click()
            elif self.is_element_present(*FrontLiveTestingLocators.CLOSE_ERROR_POPUP):
                tmp_error = (f"{i}. {browser_name} {browser_version} - Error\n")
                print(tmp_error)
                report_message += [tmp_error]
                self.browser.find_element(*FrontLiveTestingLocators.CLOSE_ERROR_POPUP).click()
            else:
                tmp_hung = (f"{i}. {browser_name} {browser_version} - Hung..\n")
                print(tmp_hung)
                report_message += [tmp_hung]
                if self.is_element_present(*FrontLiveTestingLocators.CANCEL_START_VNC_SESSION):
                    self.browser.find_element(*FrontLiveTestingLocators.CANCEL_START_VNC_SESSION).click()  # Если прелоадер беЗконечен, то попадаем в исходную позицию, выбор таб с ОС
                elif self.is_element_present(By.XPATH, FrontLiveTestingLocators.TIMER_IN_VNC):
                    self.browser.find_element(*FrontLiveTestingLocators.CLOSE_VNC_SESSION).click()
                elif self.is_element_present(*FrontLiveTestingLocators.CLOSE_ERROR_POPUP):
                    self.browser.find_element(*FrontLiveTestingLocators.CLOSE_ERROR_POPUP).click()
        report = "".join(report_message)
        now = datetime.datetime.now()
        date_time = (now.strftime("%Y-%m-%d  %H:%M:%S"))
        log_report = (f"Live testing on {platform}\nReport from:  {date_time}\n\n{report}")
        return log_report










