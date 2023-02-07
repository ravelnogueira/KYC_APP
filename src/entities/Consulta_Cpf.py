from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

class Driver_ConsultaCPF:
    def __init__(self,cpf):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1600x900")
        self.nav = webdriver.Chrome(service=self.service,options=self.options)
        self.cpf = cpf
        self.link = f'https://www.situacao-cadastral.com'

    def Run(self):
        self.cpf = self.validate(self.cpf)
        arvore = os.getcwd()

        if self.cpf == False:
            return ("CPF Invalido")

        self.nav.get(self.link)
        self.nav.maximize_window()
        self.nav.find_element('xpath','//*[@id="doc"]').send_keys(self.cpf)
        self.nav.find_element('xpath','//*[@id="consultar"]').click()
        sleep(2)
        self.nav.save_screenshot(f'src/asset/ConsultaCPF.png')

    def validate(self, cpf: str) -> bool:
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return cpf



