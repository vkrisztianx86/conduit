import csv
import time
import allure
import configuration as config
from field_identification import Field_Identification
from field_identification import test_comment


# Ez a main class, ebben vannak definiálva a különböző tesztesetek végrehajtásához a függvények. A
# "Test_Main_conduit" osztály GitHub-ra pusholásával kezdődik a folyamat, a
# Conduit weboldal automatizált tesztelése. A docker elindul, feltelepülnek a kód futtatásához szükséges programok, majd
# minden egyes teszteset különálló egységként elkezd lefutni sorban, ezután megkezdődik a kiértékelés, és ennek a
# végén a folyamat leáll.
# ------------------------------------------------------------------------------------------------------------------
class Test_Main_Conduit:

    # ChromeDriver indítása, weboldal megnyitása
    # ------------------------------------------------------------------------------------------------------------------
    def setup_method(self):
        self.conduit = Field_Identification(browser=config.get_preconfigured_chrome_driver())
        self.conduit.open()

    # Chromedriver bezárása
    # ------------------------------------------------------------------------------------------------------------------
    def teardown_method(self):
        self.conduit.close()

    @allure.id('TC1')
    @allure.title('Sütik elfogadása')
    def test_accept_cookie(self):
        cookie_bar_content = self.conduit.cookie_bar_content()
        cookie_Btn = self.conduit.cookie_Btn()
        container_before_accepting_cookie = self.conduit.container().text
        time.sleep(2)
        assert cookie_bar_content.is_displayed()
        cookie_Btn.click()
        time.sleep(3)
        container_after_accepting_cookie = self.conduit.container().text
        assert container_before_accepting_cookie != container_after_accepting_cookie

    @allure.id('TC2')
    @allure.title('Regisztráció - üres mezőkkel')
    def test_signup_with_empty_fields(self):
        self.conduit.sign_up_Btn().click()
        time.sleep(2)
        current_URL = self.conduit.current_URL()
        assert current_URL == 'http://localhost:1667/#/register'
        self.conduit.sign_up_Btn_green().click()
        time.sleep(1)
        reg_failed = self.conduit.reg_failed()
        assert reg_failed.is_displayed()
        reg_failed.click()

    @allure.id('TC3')
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

    @allure.id('TC4')
    @allure.title('Bejelentkezés - sikeresen')
    def test_signin_succesfully(self):
        self.conduit.sign_in()
        time.sleep(2)
        profile_name = self.conduit.profile_name()[2]
        assert profile_name.is_displayed()

    @allure.id('TC5')
    @allure.title('Kijelentkezés')
    def test_logout_succesfully_or_unsuccesfully(self):
        self.conduit.sign_in()
        time.sleep(2)
        logout_Btn = self.conduit.logout_Btn()
        assert logout_Btn.is_displayed()
        logout_Btn.click()
        time.sleep(3)
        signin = self.conduit.sign_in_Btn()
        assert signin.is_displayed()

    @allure.id('TC6')
    @allure.title('Új adatbevitel - kommentként')
    def test_type_in_new_data_as_comment(self):
        self.conduit.sign_in()
        data2 = test_comment
        time.sleep(2)
        article = self.conduit.article()
        article[-1].click()
        time.sleep(2)
        self.conduit.comment_input().click()
        time.sleep(2)
        self.conduit.comment_input().clear()
        time.sleep(1)
        self.conduit.comment_input().send_keys(data2)
        time.sleep(2)
        self.conduit.post_comment().click()
        time.sleep(2)
        card_text = self.conduit.card_text()[-1]
        time.sleep(1)
        assert card_text.text == data2

    @allure.id('TC7')
    @allure.title('Új adatbevitel - karakterbevitel nélkül')
    def test_type_in_without_data(self):
        self.conduit.sign_in()
        time.sleep(2)
        article = self.conduit.article()
        article[-1].click()
        time.sleep(1)
        comment_input = self.conduit.comment_input()
        self.conduit.post_comment().click()
        time.sleep(2)
        assert len(comment_input.text) == 0

    @allure.id('TC8')
    @allure.title('Több oldalas lista bejárása')
    def test_iterating_thru_pages(self):
        self.conduit.sign_in()
        time.sleep(2)
        pages = self.conduit.pages()
        counter = 1
        for page in pages:
            page.click()
            time.sleep(1)
            print(page.text, end=';')
            counter += 1
            if counter == len(pages):
                assert counter == len(pages)

    @allure.id('TC9')
    @allure.title('Meglévő adat módosítása')
    def test_data_modification(self):
        self.conduit.sign_in()
        self.conduit.settings_Btn().click()
        time.sleep(1)
        current_username = self.conduit.username_input().get_attribute('value')
        current_username_mod = current_username[0:-1]
        self.conduit.username_input().clear()
        self.conduit.username_input().send_keys(current_username_mod + 'mod')
        current_username_mod = current_username_mod + 'mod'
        self.conduit.update_Btn().click()
        time.sleep(2)
        assert self.conduit.update_successful_modal().is_displayed()
        time.sleep(2)
        self.conduit.update_successful_modal_ok_Btn().click()
        time.sleep(2)
        current_username = self.conduit.username_input().get_attribute('value')
        assert current_username_mod == current_username

    @allure.id('TC10')
    @allure.title('Meglévő adat törlése')
    def test_delete_data(self):
        self.conduit.sign_in()
        data1 = test_comment
        article = self.conduit.article()
        article[0].click()
        time.sleep(2)
        self.conduit.comment_input().click()
        time.sleep(2)
        self.conduit.comment_input().clear()
        self.conduit.comment_input().send_keys(data1)
        time.sleep(2)
        self.conduit.post_comment().click()
        time.sleep(2)
        card_text = self.conduit.card_text()[0]
        assert card_text.text == data1
        self.conduit.delete().click()
        time.sleep(1)
        card_text = self.conduit.card_text()[0]
        assert card_text.text != data1

    @allure.id('TC11')
    @allure.title('Adatok lementése felületről')
    def test_read_from_conduit(self):
        self.conduit.sign_in()
        time.sleep(2)
        article = self.conduit.article()
        article[-1].click()
        time.sleep(2)
        data = self.conduit.text_to_read().text
        time.sleep(1)
        with open('Data.txt', 'w', encoding='UTF-8') as file_to_write:
            file_to_write.write(str(data))
        time.sleep(2)
        with open('Data.txt', 'r', encoding='UTF-8') as file_to_read:
            content = file_to_read.read()
            print(content)
            assert data == content

    @allure.id('TC12')
    @allure.title('Adatok listázása')
    def test_listing_data_from_conduit(self):
        self.conduit.sign_in()
        time.sleep(2)
        article = self.conduit.article()
        article[-1].click()
        time.sleep(2)
        data = self.conduit.text_to_read().text
        time.sleep(1)
        with open('Data.txt', 'w', encoding='UTF-8') as file_to_write:
            file_to_write.write(str(data))
        time.sleep(2)
        with open('Data.txt', 'r', encoding='UTF-8') as file_to_read:
            content = file_to_read.read()
            print(content)
            content1 = content.split()
            print(content1[1::3])
            assert content == data

    @allure.id('TC13')
    @allure.title('Regisztráció - sikeresen + sorozatos adatbevitel listából')
    def test_signup_succesfully_and_data_input_iteration(self):
        self.conduit.sign_up_Btn().click()
        time.sleep(1)
        current_URL = self.conduit.current_URL()
        assert current_URL == 'http://localhost:1667/#/register'
        time.sleep(1)
        with open('Vizsgaremek_POM/Datax.csv', 'r') as reg_inputs:
            reg_reader = csv.reader(reg_inputs, delimiter=',')
            next(reg_reader)
            for inputs in reg_reader:
                self.conduit.username_input_signup().send_keys(inputs[1])
                self.conduit.email_input_signup().send_keys(inputs[2])
                self.conduit.password_input_signup().send_keys(inputs[3])
                self.conduit.sign_up_Btn_green().click()
                time.sleep(3)
                reg_modal = self.conduit.registration_successful_modal()
                assert reg_modal.is_displayed()
                self.conduit.registration_successful_modal().click()
                time.sleep(2)
                self.conduit.home_Btn().click()
                time.sleep(2)
                self.conduit.logout_Btn().click()
                time.sleep(2)
                self.conduit.sign_up_Btn().click()
