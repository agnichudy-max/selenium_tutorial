from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import unittest
from datatools import TestData
from datatools import Gender

class RegisterNewUserTest(unittest.TestCase):
    def setUp(self):
        # warunki wstepne
        # 1. Otwarta strona glowna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.techwithjatin.com/")
        # 2. Uzytkownik niezalogowany (opcjonalnie) mozna sprawdzic

    def test_no_name_in_registration_form(self):
     # KROKI
    # 1- kliknij 'sign in'
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
        # Czekam (usune po napisaniu tekstu)
        sleep(2)
    # 2- Wpisz email
        self.driver.find_element(By.ID, "email_create").send_keys(TestData.EMAIL)
    # 3- Kliknij create account
        self.driver.find_element(By.ID, "SubmitCreate").click()
        self.driver.implicitly_wait(5)
    # 4- Kliknij swoja plec
        if TestData.GENDER == Gender.FEMALE:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender2"]').click()
        else:
            self.driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()



