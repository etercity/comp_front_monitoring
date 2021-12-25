from ..settings import main_settings
from ..pages.signup_login_logout_page import SignupLoginLogoutPage
import time


class TestFrontLoginLogout():

    def setup(self):
        self.link_to_promo = (f"{main_settings.URL_PROMO}")
        self.link_to_front = (f"{main_settings.URL_FRONT}")

    def test_login_to_front_from_promo(self, browser, request):
        page = SignupLoginLogoutPage(browser, self.link_to_promo)
        page.open()
        page.login_to_front_from_promo(request, browser)

    def test_logout_from_front_to_auth0_form(self, browser):
        page = SignupLoginLogoutPage(browser, self.link_to_front)
        page.click_on_header_button_authenticated()
        time.sleep(3)
        page.click_on_logout_from_front()
        page.should_be_unauthorized()






