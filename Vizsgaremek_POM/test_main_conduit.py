import time

import allure
import configuration as config
from field_identification import Field_Identification


class Test_Main_Conduit:

    def setup_method(self):
        self.conduit = Field_Identification(browser=config.get_preconfigured_chrome_driver())
        self.conduit.open()

    def teardown_method(self):
        self.conduit.close()

    @allure.id('TC1, TC2')
    @allure.title('Sütik elfogadása')
    def test_accept_cookie(self):
        cookie_bar_content = self.conduit.cookie_bar_content()
        cookie_Btn = self.conduit.cookie_Btn()
        assert cookie_bar_content.is_displayed()
        if cookie_bar_content.is_displayed():
            cookie_Btn.click()
        else:
            print('Cookie window is not showing up')
        print('TC1,TC2 lefutott')

    @allure.id('TC3')
    @allure.title('Regisztráció - üres mezőkkel')
    def test_signup_with_empty_fields(self):
        signup_Btn = self.conduit.sign_up_Btn()
        signup_Btn.click()
        time.sleep(1)
        current_URL = self.conduit.current_URL()
        assert current_URL == 'http://localhost:1667/#/register'
        sign_up_Btn_green = self.conduit.sign_up_Btn_green()
        sign_up_Btn_green.click()
        time.sleep(1)
        reg_failed = self.conduit.reg_failed()
        assert reg_failed.is_displayed()
        reg_failed.click()
        print('TC3 lefutott')

    # @allure.id('TC2')
    # @allure.title('Bejelentkezés - Helytelen jelszó')
    # def test_login_bad_password(self):
    #     self.conduit.input_username().send_keys('student')
    #     self.conduit.input_password().send_keys('incorrectPassword')
    #     self.conduit.button_submit().click()
    #
    #     time.sleep(1)
    #     assert self.conduit.error_message().text == 'Your password is invalid!'
