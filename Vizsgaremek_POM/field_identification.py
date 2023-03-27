from basic_page import Basic_Page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

test_data = {
    "username": "Krisztianx86",
    "email": "vkrisztianx86@gmail.com",
    "password": "passworD12"
}
test_data2 = {
    "username": "Tester1",
    "email": "Tester1@yhoo.hu",
    "password": "passworD12"
}

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
        return self.browser.find_element(By.XPATH, '//i[@class="ion-android-exit"]')

    def article(self):
        return self.browser.find_elements(By.CLASS_NAME, 'article-preview')

    def comment_input(self):
        return WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//textarea[@placeholder="Write a comment..."]')))

    def post_comment(self):
        return self.browser.find_element(By.XPATH, '//button[@class="btn btn-sm btn-primary"]')

    def card_text(self):
        return self.browser.find_elements(By.XPATH, '//p[@class="card-text"]')[-1]

    def delete(self):
        return WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//i[@class="ion-trash-a"]')))

    def cookie_Btn(self):
        return self.browser.find_element(By.XPATH, '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')

    def cookie_bar_content(self):
        return self.browser.find_element(By.CSS_SELECTOR, '.cookie__bar__content')

    def current_URL(self):
        return self.browser.current_url

