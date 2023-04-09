import os
from flask_cors import CORS
from flask import Flask, jsonify
from src.service.Api_Via_cep import Buscar_Cep
from src.entities.Automacao_Maps import DriverMaps
from src.entities.Consulta_Cpf import DriverConsultaCPF
from src.entities.MidiasNegativas import DriverMidiasNegativas
from src.entities.PortalTransparencia import DriverPortalTransparencia
from src.app import * 

app = Flask(__name__)
arvore = os.getcwd()
CORS (app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return " Em funcionamento"

@app.route("/buscarcep/<string:cep>/<int:numeroR>", methods=['GET','POST','OPTIONS'])
def test_cep(cep, numeroR):
    pdf = Buscar_Cep(cep)
    pdf.Run()
    obj = DriverMaps(pdf.logradouro,numeroR,pdf.bairro)
    obj.Run()
    path = jsonify({'caminho':f'{arvore}\\src\\asset\\ImagemFrontal.png'})
    return path

@app.route("/buscartransparencia/<string:cpf>", methods=['GET'])
def test_transparencia(cpf):
    obj = DriverPortalTransparencia(cpf)
    obj.Run()
    path = jsonify({'caminho':f'{arvore}\\src\\asset\\PortalTransparencia.png'})
    print(path)
    return path

@app.route("/buscarnome/<string:nome>/<string:cpf>", methods=['GET'])
def test_google(nome):
    obj = DriverMidiasNegativas(nome)
    obj.Run()
    path = jsonify({'caminho':f'{arvore}\\src\\asset\\PortalTransparencia.png'})
    print(path)
    return path

@app.route("/buscarcpf/<string:cpf>", methods=['GET','POST'])
def test_cpf(cpf):
    path = f'{arvore}\\src\\asset\\ConsultaCPF.png'
    obj = DriverConsultaCPF(cpf)
    obj.Run()
    path = jsonify({'caminho':f'{arvore}\\src\\asset\\ConsultaCPF.png'})
    print(path)
    return path


# @app.route("/buscarcliente/<string:cpf>")
# def consulta_cpf(cpf):
#     arvore = os.getcwd()
#     i = []
#     path = f'{arvore}/src/asset/{cpf}'

#     if os.path.isdir(path):
#         dir = os.listdir(path)
#         for file in dir:
#             path1 = f'{arvore}/src/asset/{cpf}/{file}'
#             i.append(path1)
    
#     else:
#         return "Cliente não cadastrado"

#     return i
