from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

class DriverMaps:
    def __init__(self,rua,numero,bairro):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1920x1080")
        self.nav = webdriver.Chrome(service=self.service,options=self.options)
        self.street = rua
        self.number = numero
        self.district = bairro
        self.CompleteAdress =  f'{self.street} {self.number} {self.district}'

    def run(self):
        self.Go_Maps()

    def go_maps(self):

        self.nav.get('https://www.google.com/maps')
        self.nav.find_element('xpath','//*[@id="searchboxinput"]').send_keys(self.CompleteAdress)
        self.nav.find_element('xpath','//*[@id="searchbox-searchbutton"]').click()
        sleep(4)
        self.nav.find_element('xpath','//*[@id="QA0Szd"]/div/div/div[2]/button').click()
        sleep(2)

        sleep(1.5)
        self.nav.find_element('xpath','//*[@id="QA0Szd"]/div/div/div[2]/button').click()
        self.nav.find_element('xpath','//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/button/img').click()
        sleep(2) 
        self.nav.find_element('xpath','//*[@id="QA0Szd"]/div/div/div[2]/button').click()
        sleep(2)
        self.nav.save_screenshot(f'src/asset/ImagemFrontal.png')



