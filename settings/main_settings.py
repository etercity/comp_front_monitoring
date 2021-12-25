""""DOMAIN"""
URL_FRONT = 'https://front.comparium.app'
URL_PROMO = 'https://comparium.app'

"""Timings"""
IMPLICITLY_WAIT = 10 # Неявное ожидание, например для гарантированного отображения всех элементов загружаемой веб-страницы
EXPLICIT_WAIT = 15 # Явно ждем, например пока прогрузится форма логина, или появится попап при входе и т.д.
TIMEOUT_CREATE_SCREENSHOTS = 200 # Ожидаем, пока скриншоты создаются
TIMEOUT_CREATE_VNC = 182 # Ожидаем создания VNC сессии
TIMEOUT_VNC_SESSION = 24 # Время существования сессии, до закрытия

""""TELEBOT"""
COUNT_SYMBOLS = 1023

"""""Test ScreenShots"""
SCREENSHOT_NAME = '../screenshots/screen.png'
SCREENSHOT_TEST_URL = 'example.com'

""""Test LiveTesting"""
LIVE_TEST_URL = 'https://www.whatismybrowser.com/'
OS_LINUX = 'Linux'
OS_WIN = 'Windows'
CONFIGS_ON_LINUX = [['Chrome', '78.0'], ['Chrome', '79.0'], ['Chrome', '80.0'], ['Chrome', '86.0'], ['Chrome', '87.0'],
                    ['Firefox', '68.0'], ['Firefox', '74.0'], ['Firefox', '79.0'], ['Firefox', '80.0'], ['Firefox', '81.0'],
                    ['Opera', '66.0'], ['Opera', '67.0'], ['Opera', '71.0'], ['Opera', '72.0']]
CONFIGS_ON_WINDOWS = [['Chrome', '94.0'], ['Chrome', '93.0'],
                    ['Firefox', '85.0'], ['Firefox', '84.0'], ['Firefox', '83.0'],
                    ['Edge', '86.0'],
                    ['Opera', '74.0'], ['Opera', '73.0']]

"""Test ScreenShots with active Login Profile"""
EXPLICIT_WAIT_FOR_SAVE_TEST_LOGIN_PROFILE = 5
SCREENSHOT_LOGIN_PROFILE_TEST_URL = "https://casenik.com.ua/user/cabinet"
SCREENSHOT_LOGIN_PROFILE_FORM_URL = "https://casenik.com.ua/user/login"
LOC_ELEMENT_USERNAME_FIELD = "//*[@id='email']"
LOC_ELEMENT_PASSWORD_FIELD = "//*[@id='pasword']"
LOC_ELEMENT_LOGIN_BUTTON = "button-gen"
LOGIN_PROFILE_NAME = "test_login_profile"
LOGIN_TO_LOGIN_PROFILE_TEST_URL = "test@mail.com"
PASSWORD_TO_LOGIN_PROFILE_TEST_URL = "my_password"
SCREENSHOT_LOGIN_PROFILE_NAME = '../screenshots/screen_login_profile.png'

"""Test ScreenShots with Basic Access Authentication"""
SCREENSHOT_BAA = '../screenshots/screen_baa.png'

