import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opts_chrome = Options()
from selenium.webdriver.firefox.options import Options
opts_ff = Options()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
    parser.addoption('--browser_mode', action='store', default=None,
                     help="The default is GUI, but you can set --browser_mode='headless'")
    parser.addoption('--login', action='store', default=None,
                     help="Input login mail to front: example@mail.com")
    parser.addoption('--password', action='store', default=None,
                     help="Input password")
    parser.addoption('--telechat', action='store', default=None,
                     help="Input telechat_id")
    parser.addoption('--teletoken', action='store', default=None,
                     help="Input teletoken")
    parser.addoption('--width', action='store', default=1024,
                     help="Input width: 500, 768, 1024 (default), or 1920")
    parser.addoption('--os', action='store', default=None,
                     help="Input os: Windows 10, Windows 7, macOS, Dark mode, or Linux")
    parser.addoption('--browser', action='store', default=None,
                     help="Input browser: Chrome, Firefox, IE, Safari, or Opera")
    parser.addoption('--vnc_os', action='store', default=None,
                     help="Input vnc_os: Linux or Windows")
    parser.addoption('--test_url_baa', action='store', default=None,
                     help="Input test_url_baa")
    parser.addoption('--login_baa', action='store', default=None,
                     help="Input login_baa")
    parser.addoption('--password_baa', action='store', default=None,
                     help="Input password_baa")


@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    browser_mode = request.config.getoption("browser_mode")
    login = request.config.getoption("login")
    password = request.config.getoption("password")
    if not login:
        raise pytest.UsageError("--login should be set")
    elif not password:
        raise pytest.UsageError("--password should be set")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = opts_chrome
        chrome_options.add_argument('--start-maximized')
        if browser_mode == "headless":
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            print(f"\nbrowser_mode: {browser_mode}")
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        ff_options = opts_ff
        ff_options.add_argument('--start-maximized')
        if browser_mode == "headless":
            ff_options.add_argument('--headless')
            print(f"\nbrowser_mode: {browser_mode}")
        ff_options.set_preference("intl.accept_languages", browser_language)
        browser = webdriver.Firefox(options=ff_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

