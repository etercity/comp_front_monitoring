from .base_page import BasePage
from .locators import FrontScreenshotsLocators
from datetime import datetime


class FrontScreenshotPage(BasePage):

    def set_test_url(self, test_url): self.browser.find_element(*FrontScreenshotsLocators.TEST_URL_FIELD).send_keys(test_url)

    def click_test_url(self): self.browser.find_element(*FrontScreenshotsLocators.TEST_URL_FIELD).click()

    def select_width_1024(self): self.browser.find_element(*FrontScreenshotsLocators.WIDTH_1024).click()

    def select_custom_width(self, custom_width): self.browser.find_element_by_xpath(f"//label[text()='{custom_width} px']").click()

    def select_all_configs(self): self.browser.find_element(*FrontScreenshotsLocators.OS_BROWSER_NAME_TAB).click()

    def select_some_configs(self): self.browser.find_element(*FrontScreenshotsLocators.for_test_tmp2).click()

    def select_custom_os(self, custom_os): self.browser.find_element_by_xpath(f"//div[text()='{custom_os}']").click()

    def select_custom_browser(self, custom_browser): self.browser.find_element_by_xpath(f"//td[text()='{custom_browser}']").click()

    def press_btn_create_screenshots(self): self.browser.find_element(*FrontScreenshotsLocators.CREATE_SCREENSHOTS_BTN).click()

    def click_on_login_profile(self): self.browser.find_element(*FrontScreenshotsLocators.LOGIN_PROFILE_BUTTON).click()

    def add_new_login_profile(self): self.browser.find_element(*FrontScreenshotsLocators.ADD_NEW_LOGIN_PROFILE_BUTTON).click()

    def input_url_by_the_login_form(self, test_url_by_the_login_form): self.browser.find_element(*FrontScreenshotsLocators.INPUT_URL_BY_LOGIN_FORM).send_keys(test_url_by_the_login_form)

    def press_button_next_in_login_profile(self): self.browser.find_element(*FrontScreenshotsLocators.BUTTON_NEXT_IN_LOGIN_PROFILE_POPUP).click()

    def click_on_user_name_selector(self): self.browser.find_element(*FrontScreenshotsLocators.USER_NAME_SELECTOR_IN_LOGIN_PROFILE_POPUP).click()

    def select_user_name_selector(self): self.browser.find_element(*FrontScreenshotsLocators.SELECT_USERNAME_SELECTOR).click() #Если поменялся локатор тестируемого сайта, и вместо икспас надо др., то меняем значение option-3 на option-0 - option-4

    def input_user_name_selector_value(self, user_name_selector_value): self.browser.find_element(*FrontScreenshotsLocators.INPUT_USER_NAME).send_keys(user_name_selector_value)

    def click_on_password_selector(self): self.browser.find_element(*FrontScreenshotsLocators.PASSWORD_SELECTOR_IN_LOGIN_PROFILE_POPUP).click()

    def select_password_selector(self): self.browser.find_element(*FrontScreenshotsLocators.SELECT_PASSWORD_SELECTOR).click() #Если поменялся локатор тестируемого сайта, и вместо икспас надо др., то меняем значение option-3 на option-0 - option-4

    def input_password_selector_value(self, password_selector_value): self.browser.find_element(*FrontScreenshotsLocators.INPUT_PASSWORD).send_keys(password_selector_value)

    def click_on_login_button_selector(self): self.browser.find_element(*FrontScreenshotsLocators.LOGINBUTTON_SELECTOR_IN_LOGIN_PROFILE_POPUP).click()

    def select_login_button_selector(self): self.browser.find_element(*FrontScreenshotsLocators.SELECT_LOGIN_BUTTON_SELECTOR).click() #Если поменялся локатор тестируемого сайта, и вместо икспас надо др., то меняем значение option-3 на option-0 - option-4

    def input_login_button_selector_value(self, login_button_selector_value): self.browser.find_element(*FrontScreenshotsLocators.INPUT_LOGIN_BUTTON).send_keys(login_button_selector_value)

    def input_username_creds(self, username_creds): self.browser.find_element(*FrontScreenshotsLocators.INPUT_USERNAME_CREDS).send_keys(username_creds)

    def input_password_creds(self, password_creds): self.browser.find_element(*FrontScreenshotsLocators.INPUT_PASSWORD_CREDS).send_keys(password_creds)

    def input_login_profile_name(self, login_profile_name): self.browser.find_element(*FrontScreenshotsLocators.INPUT_LOGIN_PROFILE_NAME).send_keys(login_profile_name)

    def press_button_save_in_login_profile(self): self.browser.find_element(*FrontScreenshotsLocators.BUTTON_SAVE_IN_LOGIN_PROFILE).click()

    def delete_test_login_profile(self, login_profile_name): self.browser.find_element_by_xpath(f"//li[text()='{login_profile_name}']/button[@title='Delete']").click()

    def confirm_delete_test_login_profile(self): self.browser.find_element(*FrontScreenshotsLocators.CONFIRM_DELETE_LOGIN_PROFILE).click()

    def click_on_ba(self): self.browser.find_element(*FrontScreenshotsLocators.BASIC_AUTHENTICATION_BUTTON).click()

    def input_user_ba(self, user_name_ba): self.browser.find_element(*FrontScreenshotsLocators.INPUT_USER_BA).send_keys(user_name_ba)

    def input_password_ba(self, user_password_ba): self.browser.find_element(*FrontScreenshotsLocators.INPUT_PASSWORD_BA).send_keys(user_password_ba)

    def press_button_save_ba(self): self.browser.find_element(*FrontScreenshotsLocators.BUTTON_SAVE_IN_BA).click()

    def make_log_report_created_screenshots(self, header_report_to_telegram):
        now = datetime.now()
        date_time = (now.strftime("%Y-%m-%d  %H:%M:%S"))
        report_from = (f"Report from:  {date_time}\n")
        errors = []
        i = 0
        for item in self.browser.find_elements(*FrontScreenshotsLocators.SCREENSHOT_ERROR):
            # print(item.get_attribute("innerHTML"))  # распечатка html
            i += 1
            div_class_attr = item.find_element(*FrontScreenshotsLocators.DIV_CLASS_ATTR).get_attribute("title")
            text_config = (div_class_attr.rsplit(', ', 1)[0])  # обрезаем разрешение
            errors += [f"{i}. {text_config}\n"]
        if errors: str_errors = "".join(errors)
        else: str_errors = 0
        hungs = []
        i = 0
        for item in self.browser.find_elements(*FrontScreenshotsLocators.SCREENSHOT_HUNG):
            i += 1
            div_class_attr = item.find_element(*FrontScreenshotsLocators.DIV_CLASS_ATTR).get_attribute("title")
            text_config = (div_class_attr.rsplit(', ', 1)[0])
            hungs += [f"{i}. {text_config}\n"]
        if hungs: str_hungs = "".join(hungs)
        else: str_hungs = 0
        log_report = (
            f"{header_report_to_telegram}\n{report_from}\nScreenshot(s) not created:\n{str_errors}\nHanging screenshot(s):\n{str_hungs}")
        return log_report

















