from basic_page import Basic_Page
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Tesztadatok dictionary-ba szervezése
# ------------------------------------------------------------------------------------------------------------------

test_data2 = {
    "counter": "12",
    "username": "Tester11",
    "email": "Tester1@yahoo.hu",
    "password": "passworD12",
    "test_comment": "Bandita"
}

# Regisztrációs adatok összeállítása dictionary-ból és változókba mentése
# ------------------------------------------------------------------------------------------------------------------
username = test_data2["username"] + test_data2["counter"]
email = test_data2["email"] + test_data2["counter"]
password = test_data2["password"]
test_comment = test_data2["test_comment"]

test_list = [username, email, password]


# Osztály létrehozása, ami a Basic Page gyerekosztálya, benne a különböző,
# conduit oldali bevitelimező, gomb, és szövegmező-beazonosítások vannak függvényekbe szervezve, ezek
# meghívásakor a visszatérítési érték az aktuális mező lesz.
# ------------------------------------------------------------------------------------------------------------------
class Field_Identification(Basic_Page):

    def __init__(self, browser):
        super().__init__(browser, url='http://localhost:1667/#/')

    def sign_in_Btn(self):
        return self.browser.find_elements(By.XPATH, '//a[@class="nav-link"]')[0]

    def sign_up_Btn(self):
        return self.browser.find_elements(By.XPATH, '//a[@class="nav-link"]')[1]

    def home_Btn(self):
        return self.browser.find_element(By.XPATH, '//a[@class="nav-link router-link-exact-active active"]')

    def sign_up_Btn_green(self):
        return self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')

    def reg_failed(self):
        return self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')

    def username_input_signup(self):
        return self.browser.find_element(By.XPATH, '//input[@placeholder="Username"]')

    def email_input_signup(self):
        return self.browser.find_element(By.XPATH, '//input[@placeholder="Email"]')

    def password_input_signup(self):
        return self.browser.find_element(By.XPATH, '//input[@placeholder="Password"]')

    def registration_successful_modal(self):
        return WebDriverWait(self.browser, 6).until(
            EC.presence_of_element_located((By.XPATH, '//button[@class="swal-button swal-button--confirm"]')))

    def logout_Btn(self):
        return self.browser.find_element(By.XPATH, '//a[@active-class="active"]')

    def logout_Btn_1(self):
        return self.browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[5]/a/i')

    def logout_Btn2(self):
        return self.browser.find_element(By.XPATH, '/html/body/div[1]/nav/div/ul/li[3]/a')

    def article(self):
        return self.browser.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a/h1')

    def comment_input(self):
        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))

    def post_comment(self):
        return self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')

    def card_text(self):
        return self.browser.find_elements(By.XPATH, '//p[@class="card-text"]')

    def delete(self):
        return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//i[@class="ion-trash-a"]')))

    def cookie_Btn(self):
        return self.browser.find_element(By.XPATH,
                                         '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')

    def cookie_bar_content(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.cookie__bar__content')

    def current_URL(self):
        return self.browser.current_url

    def sign_up_inputs(self):
        return self.browser.find_elements(By.XPATH, '//input[@class="form-control form-control-lg"]')

    def profile_name(self):
        return self.browser.find_elements(By.XPATH, '//a[@class="nav-link"]')

    def pages(self):
        return self.browser.find_elements(By.CSS_SELECTOR, '.page-link')

    def new_article(self):
        return self.browser.find_element(By.XPATH, '//i[@class="ion-compose"]')

    def text_input(self):
        return self.browser.find_elements(By.XPATH, '//input[@type="text"]')

    def publish_article_Btn(self):
        return self.browser.find_element(By.XPATH, '//button[@type="submit"]')

    def texta_area(self):
        return self.browser.find_element(By.XPATH, '//textarea[@rows="8"]')

    def edit_article(self):
        return self.browser.find_element(By.XPATH, '//i[@class="ion-edit"]')

    def input_text(self):
        return self.browser.find_element(By.XPATH, '//div[@class="col-xs-12"]/div/p')

    def annyoying_panel(self):
        return self.browser.find_element(By.XPATH, '//i[@class="ion-plus-round"]')

    def conduit_logo(self):
        return self.browser.find_element(By.XPATH, '//a[@class="navbar-brand router-link-active"]')

    def settings_Btn(self):
        return self.browser.find_element(By.XPATH, '//*[@id="app"]/nav/div/ul/li[3]/a')

    def username_input(self):
        return self.browser.find_element(By.XPATH, '//input[@placeholder="Your username"]')

    def update_Btn(self):
        return self.browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary pull-xs-right"]')

    def update_successful_modal(self):
        return self.browser.find_element(By.XPATH, '//div[@class="swal-title"]')

    def update_successful_modal_ok_Btn(self):
        return self.browser.find_element(By.XPATH, '//button[@class="swal-button swal-button--confirm"]')

    def text_to_read(self):
        return self.browser.find_element(By.XPATH, '//div[@class="col-xs-12"]/div/p')

    def container(self):
        return self.browser.find_element(By.XPATH, '//*[@id="app"]/footer/div')

    # A sign-in függvény nem egy adott weboldal-elem beazonosítását végzi el, hanem egy komplett
    # bejelentkezési folyamatot, amit több alkalommal hívok meg a "Test_Main_Conduit" osztályban.
    # ------------------------------------------------------------------------------------------------------------------

    def sign_in(self):
        self.sign_in_Btn().click()
        time.sleep(2)
        self.email_input_signup().send_keys(test_list[1])
        self.password_input_signup().send_keys(test_list[2])
        time.sleep(2)
        self.sign_up_Btn_green().click()
        time.sleep(2)
