import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configuration as config
from field_identification import Field_Identification
from field_identification import test_list


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
        try:
            cookie_Btn.click()
        except BaseException as E:
            print(f'Cookie window is not showing up, error is {E}')
        print('TC1,TC2 lefutott')

    @allure.id('TC3')
    @allure.title('Regisztráció - üres mezőkkel')
    def test_signup_with_empty_fields(self):
        self.conduit.sign_up_Btn().click()
        time.sleep(1)
        current_URL = self.conduit.current_URL()
        assert current_URL == 'http://localhost:1667/#/register'
        self.conduit.sign_up_Btn_green().click()
        time.sleep(1)
        reg_failed = self.conduit.reg_failed()
        assert reg_failed.is_displayed()
        reg_failed.click()
        print('TC3 lefutott')

    @allure.id('TC4, TC5')
    @allure.title('Regisztráció - sikeresen + sorozatos adatbevitel listából')
    def test_signup_succesfully_and_data_input_iteration(self):
        self.conduit.sign_up_Btn().click()
        time.sleep(1)
        current_URL = self.conduit.current_URL()
        assert current_URL == 'http://localhost:1667/#/register'
        time.sleep(1)
        signup_inputs = self.conduit.sign_up_inputs()
        counter = 0
        for input in signup_inputs:
            input.send_keys(test_list[counter])
            counter += 1
        self.conduit.sign_up_Btn_green().click()
        time.sleep(1)
        reg_modal = self.conduit.registration_successful_modal()
        assert reg_modal.is_displayed()
        self.conduit.registration_successful_modal().click()
        print('TC4, TC5 lefutott')

    @allure.id('TC6')
    @allure.title('Bejelentkezés - üres mezőkkel')
    def test_signin_with_empty_fields(self):
        self.conduit.sign_in_Btn().click()
        self.conduit.sign_up_Btn_green().click()
        time.sleep(1)
        login_failed = self.conduit.reg_failed()
        assert login_failed.is_displayed()
        current_URL = self.conduit.current_URL()
        assert current_URL == 'http://localhost:1667/#/login'
        login_failed.click()
        print('TC6 lefutott')

    @allure.id('TC7')
    @allure.title('Bejelentkezés - sikeresen')
    def test_signin_succesfully(self):
        # self.test_signup_succesfully()
        self.conduit.sign_in_Btn().click()
        time.sleep(1)
        self.conduit.email_input_signup().send_keys(test_list[1])
        self.conduit.password_input_signup().send_keys(test_list[2])
        self.conduit.sign_up_Btn_green().click()
        time.sleep(2)
        profile_name = self.conduit.profile_name()
        assert profile_name.text == test_list[0]
        print('TC7 lefutott')

    @allure.id('TC8, TC9')
    @allure.title('Kijelentkezés - sikeres/sikertelen')
    def test_logout_succesfully_or_unsuccesfully(self):
        self.conduit.sign_in()
        time.sleep(1)
        logout_Btn = self.conduit.logout_Btn()
        assert logout_Btn.is_displayed()
        try:
            logout_Btn.click()
        except BaseException as E:
            print(f'There is no logout button, error is {E}')
        print('TC8, TC9 lefutott')

    @allure.id('TC10')
    @allure.title('új adatbevitel - kommentként')
    def test_type_in_new_data_as_comment(self):
        self.conduit.sign_in()
        time.sleep(2)
        article = self.conduit.article()
        article[0].click()
        time.sleep(1)
        self.conduit.comment_input().click()
        time.sleep(1)
        self.conduit.comment_input().clear()
        self.conduit.comment_input().send_keys('Bandita')
        self.conduit.post_comment().click()
        card_text = self.conduit.card_text()
        assert card_text.text == 'Bandita'
        print('TC10 lefutott')

    @allure.id('TC11')
    @allure.title('új adatbevitel - karakterbevitel nélkül')
    def test_type_in_without_data(self):
        self.conduit.sign_in()
        time.sleep(2)
        article = self.conduit.article()
        article[0].click()
        time.sleep(1)
        comment_input = self.conduit.comment_input()
        self.conduit.post_comment().click()
        time.sleep(1)
        assert len(comment_input.text) == 0
        print('TC11 lefutott')

    @allure.id('TC12')
    @allure.title('több oldalas lista bejárása')
    def test_iterating_thru_pages(self):
        self.conduit.sign_in()
        time.sleep(2)
        pages = self.conduit.pages()
        for page in pages:
            page.click()
            time.sleep(2)
            print(page.text, end=';')
        print('TC12 lefutott')

    @allure.id('TC13, TC14')
    @allure.title('új adatbevitel - meglévő adat módosítás')
    def test_type_in_and_data_modification(self):
        self.conduit.data_input()
        test_data = self.conduit.input_text().text
        self.conduit.edit_article().click()
        time.sleep(2)
        self.conduit.texta_area().click()
        time.sleep(2)
        self.conduit.texta_area().send_keys('Ezisadat')
        time.sleep(3)
        adat = self.conduit.texta_area().get_attribute('value')
        assert adat == 'EzisadatEzisadat'
        time.sleep(2)
        print(('TC13, TC14 lefutott'))

    @allure.id('TC15, TC16')
    @allure.title('új adatbevitel - meglévő adat módosítás')
    def test_delete_data(self):
        self.conduit.data_input()
        self.conduit.edit_article().click()
        time.sleep(1)
        test_data = self.conduit.texta_area().text
        if test_data != '':
            self.conduit.texta_area().click()
            time.sleep(2)
            self.conduit.texta_area().clear()
            time.sleep(2)
            assert test_data == ''
            print('Yes, if')
        else:
            assert test_data == ''
            print('Yes, else')
            print('T' + test_data + 'T')
        print(('TC15, TC16 lefutott'))



