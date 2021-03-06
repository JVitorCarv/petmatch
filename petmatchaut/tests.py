from threading import Thread
from time import sleep
from django.test import LiveServerTestCase
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestHome(LiveServerTestCase):
    def test(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get('http://127.0.0.1:8000/')

        assert "PetMatch" in driver.title

        Thread(sleep(3))

class TestSignup(LiveServerTestCase):
    def testSignup(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        options.add_argument('headless')
        driver.get('http://127.0.0.1:8000/accounts/signup/')

        email = driver.find_element_by_id('id_email')
        username = driver.find_element_by_id('id_username')
        first_name = driver.find_element_by_id('id_first_name')
        last_name = driver.find_element_by_id('id_last_name')
        password = driver.find_element_by_id('id_password1')
        password_confirm = driver.find_element_by_id('id_password2')
        
        #populate the form with data
        email.send_keys('selenium.test@gmail.com')
        username.send_keys('Selen')
        first_name.send_keys('Sele')
        last_name.send_keys('Nium')
        password.send_keys('momentanio')
        password_confirm.send_keys('momentanio')

        driver.find_element_by_class_name("btn-success").click()
        Thread(sleep(5))
        
        driver.close()
        
        
        

'''   
class TestLogin(LiveServerTestCase):
    def testLogin(self):
        login = webdriver.Chrome()
        login.get('http://127.0.0.1:8000/accounts/login/')

        email = login.find_element_by_id('id_login')
        password = login.find_element_by_id('id_password')

        email.send_keys('selenium@gmail.com')
        password.send_keys('momentanio')
        Thread(sleep(3))

        submit login.find_elements_by_xpath("//button[contains(@class,'btn btn-sucess')]")


class testAddPet(LiveServerTestCase):
    def testAddPet(self):
        login = webdriver.Chrome()
        login.get('http://127.0.0.1:8000/accounts/login/')

        email = login.find_element_by_id('id_login')
        password = login.find_element_by_id('id_password')

        email.send_keys('selenium@gmail.com')
        password.send_keys('momentanio')
        Thread(sleep(3))
        
        login.find_elements_by_xpath("//button[contains(@class,'btn btn-sucess')]")

        pet_name = login.find_element_by_id('id_pet_name')
        pet_race = login.find_element_by_id('id_race')
        pet_age = login.find_element_by_id('id_pet_age')
        pet_image = login.find_element_by_id('id_pet_image')

        pet_name.send_keys('Pet')
        pet_race.send_keys('Race')
        pet_age.send_keys('5')
        pet_image.send_keys(os.getcwd()+"media/cao.png")
        Thread(sleep(3))

        login.find_elements_by_xpath("//button[contains(@class,'btn btn-sucess')]")
'''