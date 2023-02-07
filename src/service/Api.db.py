# # ROTAS DO CRUD
# @app.route("/")
# def hello():
#     return "Rotas: 1- /buscarcep (Buscar cep) \n 2- /buscartransparencia (Consulta Portal da Transparencia) \n 3- /buscarnome (Consulta Midias negativas e JusBrasil) \n 4- /gerapdf (Gera Pdf) 5- /buscarcpf (Consulta Situação Cadastral)"

# @app.route("/path", methods=['GET'])
# def test_db():
#     return Get_Path()

# @app.route("/path/<string:cpf>", methods=['GET'])
# def test_db12(cpf):
#     return Get_Path_imagens(cpf)

# @app.route("/insert/<string:id>/<string:cpf>/<string:name>", methods=['GET','POST'])
# def test_db_1(id, name, cpf):
#     Insert_Path(id, name, cpf)
#     return "sucess"

# @app.route("/update/<string:cpf>/<string:campo>/<string:valor>", methods=['GET','POST'])
# def Test_db(cpf,campo,valor):
#     Update_Imagem(cpf,campo,valor)
#     return "sucess"

# @app.route("/delete/<string:cpf>", methods=['GET','POST'])
# def test_delete(cpf):
#     Delete_imagem(cpf)
#     return "sucess"    