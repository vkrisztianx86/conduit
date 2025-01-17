"""
A modul célja, hogy ne kelljen minden egyes példánál ismételni a megfelelő Chrome driver létrehozását.
Importálás után elég a get_preconfigured_chrome_driver() függvényt meghívni.
"""
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# A ChromeWebdriver indításához szükséges függvény, amely a Test_Main_Conduit osztályban
# van meghívva, a setup_method-on belül.
# ------------------------------------------------------------------------------------------------------------------

def get_preconfigured_chrome_driver() -> webdriver.Chrome:
    s = Service(executable_path=ChromeDriverManager().install())
    o = Options()
    o.add_experimental_option('detach', True)
    o.add_argument('--headless')
    o.add_argument('--no-sandbox')
    o.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(service=s, options=o)
