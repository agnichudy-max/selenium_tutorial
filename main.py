from selenium.webdriver import Chrome
from time import sleep


#stworzenie instancji klasy Chrome
# to otworzy przegladarke

driver = Chrome()

driver.get("https://www.google.com/")

# maksymalizacja okna
driver.maximize_window()

sleep(5)
driver.quit()
