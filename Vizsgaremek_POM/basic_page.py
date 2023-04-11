from datetime import datetime


# Osztály definiálása, amiben egy tetszőleges weboldal alapfunkciói vannak függvényekbe
# szervezve. Ez a Test_Main_Conduit osztály ősosztálya.
# ------------------------------------------------------------------------------------------------------------------

class Basic_Page:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        self.browser.close()

    def refresh(self):
        self.browser.refresh()
