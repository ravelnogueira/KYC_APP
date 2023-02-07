import os
from flask_cors import CORS
from flask import Flask, jsonify
from src.service.Api_Via_cep import Buscar_Cep
from src.entities.Automacao_Maps import Driver_Maps
from src.entities.Consulta_Cpf import Driver_ConsultaCPF
from src.entities.MidiasNegativas import Driver_MidiasNegativas
from src.entities.PortalTransparencia import Driver_PortalTransparencia
from src.app import * 

app = Flask(__name__)
arvore = os.getcwd()
CORS (app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return " Em funcionamento"

@app.route("/buscarcep/<string:cep>/<int:numeroR>", methods=['GET','POST','OPTIONS'])
def Test_Cep(cep, numeroR):
    pdf = Buscar_Cep(cep)
    pdf.Run()
    obj = Driver_Maps(pdf.logradouro,numeroR,pdf.bairro)
    obj.Run()
    path = jsonify({'caminho':f'{arvore}\\src\\asset\\ImagemFrontal.png'})
    return path

@app.route("/buscartransparencia/<string:cpf>", methods=['GET'])
def Test_Transparencia(cpf):
    obj = Driver_PortalTransparencia(cpf)
    obj.Run()
    path = jsonify({'caminho':f'{arvore}\\src\\asset\\PortalTransparencia.png'})
    print(path)
    return path

@app.route("/buscarnome/<string:nome>/<string:cpf>", methods=['GET'])
def Test_Google(nome):
    obj = Driver_MidiasNegativas(nome)
    obj.Run()
    path = jsonify({'caminho':f'{arvore}\\src\\asset\\PortalTransparencia.png'})
    print(path)
    return path

@app.route("/buscarcpf/<string:cpf>", methods=['GET','POST'])
def Test_CPF(cpf):
    path = f'{arvore}\\src\\asset\\ConsultaCPF.png'
    obj = Driver_ConsultaCPF(cpf)
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
