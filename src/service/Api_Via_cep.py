import requests

class Buscar_Cep:
    def __init__(self, cep):
        self.cep = cep
        self.url = 'https://viacep.com.br/ws/{cep}/json/'
        self.logradouro = ''
        self.bairro = ''

    def Run(self):
        self.cep = self.Validate(self.cep)
        response = requests.get(self.url.format(cep=self.cep))
        
        if response.status_code == 404: 
            response = requests.get(self.url.format(cep=self.cep))

        response1 = response.json()
        self.bairro = response1["bairro"]
        self.logradouro = response1['logradouro']
        return response.json()

    def Validate(self, field):
        self.cep = "".join(field.replace("-"," ").split())
        if self.cep.isdigit() and len(self.cep) == 8:
           return self.cep
        raise Exception('CEP "{field}" Format Invalid'.format(field=field))


