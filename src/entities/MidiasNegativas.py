from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

class DriverMidiasNegativas:
    def __init__(self,nome, cpf):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1600x900")
        self.nav = webdriver.Chrome(service=self.service,options=self.options)
        self.nome = nome
        self.cpf = cpf
        self.link = f'https://www.google.com'


    def run(self):
        self.ConsultaPalavras()
        self.ConsultarJus()

    def consulta_palavras(self):
        self.nav.get(self.link)
        self.nome = self.nome.replace("+"," ")

        arvore = os.getcwd()
        xpath_initial = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        xpath_second = '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input'

        self.nav.find_element('xpath',xpath_initial).send_keys(f'"{self.nome} fraude"')
        self.nav.find_element('xpath',xpath_initial).submit()
        
        if os.path.isdir(f'{arvore}/src/asset/{self.cpf}'):
            self.nav.save_screenshot(f'src/asset/{self.cpf}/ConsultaKeyWordsfraude.png')

        else:
            os.makedirs(f'{arvore}/src/asset/{self.cpf}')
            self.nav.save_screenshot(f'src/asset/{self.cpf}/ConsultaKeyWordsfraude.png')

        lista = ["fraud", "processos","lawsuit",
        "envolvimento","involvement", "lavagem", "Money laundering",
        "cvm","regulation", "armas","guns"]

        for i in lista:
            self.nav.find_element('xpath',xpath_second).clear()        
            self.nav.find_element('xpath',xpath_second).send_keys(f'"{self.nome} {i}"')
            self.nav.find_element('xpath',xpath_second).submit()
            sleep(3)
            self.nav.save_screenshot(f'src/asset/{self.cpf}/ConsultaKeyWords{i}.png')


    def consultar_jus(self):
        self.nav.get(self.link)
        self.nome = self.nome.replace("+"," ")
        self.nav.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(f'site:jusbrasil.com.br "{ self.nome}"')
        self.nav.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').submit()
        sleep(5)
        self.nav.save_screenshot(f'src/asset/{self.cpf}/ConsultaJusBrasil.png')
        self.nav.close()


