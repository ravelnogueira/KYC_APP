from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

class Driver_PortalTransparencia:
    def __init__(self,cpf):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1600x900")
        self.nav = webdriver.Chrome(service=self.service,options=self.options)
        self.cpf = cpf
        self.link = f'https://portaldatransparencia.gov.br/busca?termo={self.cpf}'

    def Run(self):
        self.nav.get(self.link)
        sleep(7)
        self.nav.save_screenshot('src/asset/PortalTransparencia.png')


        