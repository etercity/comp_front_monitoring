from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_EMAIL_IN_HEADER = (By.CSS_SELECTOR, ".header__authenticated-btn .header__authenticated-btn-label")


class SignupLoginLogoutLocators():
    LOGIN_BUTTON_FROM_PROMO = (By.XPATH, "//li[@class='li-row']/a[@class='btn btn-back-app btn-login']")
    EMAIL_FIELD = (By.NAME, "email")
    PASS_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "submit")
    POPUP_CLOSE = (By.TAG_NAME, "button[title='Close']")
    LOGIN_PASSWORD_INVALID = (By.XPATH, "//div[@class='auth0-lock-error-invalid-hint']")
    LOGIN_PASSWORD_INCORRECT = (By.XPATH, "//div[@class='auth0-global-message auth0-global-message-error']")
    HEADER_BUTTON_AUTHENTICATED = (By.XPATH, "//div[@class ='header__authenticated']")
    HEADER_BUTTON_LOGOUT = (By.XPATH, "//a[text()='Log out']")


class FrontScreenshotsLocators():
    TEST_URL_FIELD = (By.NAME, "url")
    WIDTH_1024 = (By.XPATH, "//label[@class='resolution'][3]")
    OS_BROWSER_NAME_TAB = (By.XPATH, '//td[contains(text(), "OS/Browser")]')
    for_test_tmp2 = (By.XPATH, "//tr[@class='configurations__table-row'][3]/td[1]") #Для дебага выбираем не все конфиги
    CREATE_SCREENSHOTS_BTN = (By.CSS_SELECTOR, "button.btn.blue-btn.configurations__btn-button")
    SCREENSHOT_ERROR = (By.XPATH, '//*[@class="thumbnail__error"]/parent::div')  # '//*[@class="thumbnail__error"]/preceding-sibling::div' - возьмет предыдущий элемент:
    SCREENSHOT_HUNG = (By.XPATH, '//*[@class="thumbnail__loading"]/parent::div')
    DIV_CLASS_ATTR = (By.CLASS_NAME, "thumbnail__overlay")

    LOGIN_PROFILE_BUTTON = (By.XPATH, "//div[text()='Login Profile']")
    ADD_NEW_LOGIN_PROFILE_BUTTON = (By.XPATH, "//button[@class='configs-authentication__login-profile-form-btn blue-btn']")
    INPUT_URL_BY_LOGIN_FORM = (By.XPATH, "//form[@class='login-profile-creator-popup__tabpanel-form']/input[@class='login-profile-creator-popup__tabpanel-form-field-url']")
    BUTTON_NEXT_IN_LOGIN_PROFILE_POPUP = (By.XPATH, "//div[@class='login-profile-creator-popup__tabpanel' and not (contains(@style,'display: none'))]//button[@class='btn light-blue-btn login-profile-creator-popup__tabpanel-form-buttons-btn']")
    USER_NAME_SELECTOR_IN_LOGIN_PROFILE_POPUP = (By.XPATH, "//div[@class='login-profile-creator-popup__tabpanel-form-fieldswrapper'][1]/div[@class='login-profile-creator-popup__tabpanel-form-fieldwrapper'][1]")
    SELECT_USERNAME_SELECTOR = (By.XPATH, "//div[@id='react-select-2-option-3']")
    INPUT_USER_NAME = (By.XPATH, "//input[@name='usernameValue']")
    PASSWORD_SELECTOR_IN_LOGIN_PROFILE_POPUP = (By.XPATH, "//div[@class='login-profile-creator-popup__tabpanel-form-fieldswrapper'][2]/div[@class='login-profile-creator-popup__tabpanel-form-fieldwrapper'][1]")
    SELECT_PASSWORD_SELECTOR = (By.XPATH, "//div[@id='react-select-3-option-3']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='passwordValue']")
    LOGINBUTTON_SELECTOR_IN_LOGIN_PROFILE_POPUP = (By.XPATH, "//div[@class='login-profile-creator-popup__tabpanel-form-fieldswrapper'][3]/div[@class='login-profile-creator-popup__tabpanel-form-fieldwrapper'][1]")
    SELECT_LOGIN_BUTTON_SELECTOR = (By.XPATH, "//div[@id = 'react-select-4-option-4']")
    INPUT_LOGIN_BUTTON = (By.XPATH, "//input[@name='submitValue']")
    INPUT_USERNAME_CREDS = (By.XPATH, "//input[@name='login']")
    INPUT_PASSWORD_CREDS = (By.XPATH, "//input[@name='password']")
    INPUT_LOGIN_PROFILE_NAME = (By.XPATH, "//input[@name='title']")
    BUTTON_SAVE_IN_LOGIN_PROFILE = (By.XPATH, "//button[@class='btn blue-btn login-profile-creator-popup__tabpanel-form-buttons-btnsave']")
    CONFIRM_DELETE_LOGIN_PROFILE = (By.XPATH, "//button[text()='YES']")
    BASIC_AUTHENTICATION_BUTTON = (By.XPATH, "//div[@class='configs-authentication__basic-authentication-button']")
    INPUT_USER_BA = (By.XPATH, "//input[@placeholder='Username']")
    INPUT_PASSWORD_BA = (By.XPATH, "//input[@placeholder='Password']")
    BUTTON_SAVE_IN_BA = (By.XPATH, "//button[text()='Save']")

    SMARTSCROLL_SWITCH = (By.XPATH, "//div[@class='configs-authentication__smartscroll-checker-switch']")


class FrontLiveTestingLocators():
    LIVE_TESTING_TAB = (By.XPATH, "//div[@class = 'header__pageSelector']/a[2]")
    FIELD_INPUT_TEST_URL = (By.XPATH, "//input[@class = 'realTimeTestingPage__input']")
    VNC_WIN_TAB = (By.XPATH, '//button[@class="realTimeTestingPage__button"]/span[@class="realTimeTestingPage__button-background windows"]')
    VNC_LINUX_TAB = (By.XPATH, '//button[@class="realTimeTestingPage__button"]/span[@class="realTimeTestingPage__button-background linux"]')
    CLICK_BROWSER_TAB = (By.XPATH, '//div[@class="realTimeTestingPage__popup-selects"]/div[1]/div[1]')
    CLICK_BROWSER_VERSION_TAB = (By.XPATH, '//div[@class="realTimeTestingPage__popup-selects"]/div[2]/div[1]')
    BUTTON_RUN_LIVE_TEST = (By.XPATH, '//button[@class="realTimeTestingPage__popup-run-btn orange-gradient-btn one-border-active"]')
    PRELOADER_WAIT_VNC = ("//div[@class='realTimeTestingPreloader__loader']")
    TIMER_IN_VNC = ("//div[@class='realTimeTesting__header-timer']")
    CLOSE_VNC_SESSION = (By.XPATH, "//button[@class='realTimeTesting__header-close-btn square-btn']")
    CLOSE_ERROR_POPUP = (By.XPATH, "//button[@class='realTimeTestingPopup__btn blue-btn']")
    CANCEL_START_VNC_SESSION = (By.XPATH, "//button[@class='realTimeTestingPreloader__btn white-blue-btn']")


