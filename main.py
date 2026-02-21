from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By

# Dane testowe
DATA_EMAIL = "jncv kjxcv@spam.la"
#stworzenie instancji klasy Chrome
# to otworzy przegladarke

driver = Chrome()

driver.get("https://automationpractice.techwithjatin.com/")


# maksymalizacja okna
driver.maximize_window()

#znajdz element Sign in
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
#kliknij w odnaleziony element
sign_in_a.click()

#wipsz email
driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)

print(type(sign_in_a))
sleep(5)
driver.quit()
