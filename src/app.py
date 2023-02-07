from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import base64 

engine = create_engine('postgresql://postgres:96485140@localhost:5432/postgres')
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session = Session()

class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer,nullable=False, autoincrement=True )
    nome = Column(String, nullable = False)
    cpf = Column(String, nullable=False,primary_key=True)
    consulta_cpf = Column(String, nullable=True)
    jusbrasil = Column(String, nullable=True)
    consulta_armas = Column(String, nullable=True)
    consulta_guns = Column(String, nullable=True)
    consulta_cvmr = Column(String, nullable=True)
    consulta_envolvimento = Column(String, nullable=True)
    consulta_fraud = Column(String, nullable=True)
    consulta_fraude = Column(String, nullable=True)
    consulta_involvement = Column(String, nullable=True)
    consulta_lavagem = Column(String, nullable=True)
    consulta_lawsuit = Column(String, nullable=True)
    consulta_moneylaudering = Column(String, nullable=True)
    consulta_processos = Column(String, nullable=True)
    consulta_regulation = Column(String, nullable=True)
    maps_frontal = Column(String, nullable=True)
    maps_planta = Column(String, nullable=True)

    def __repr__(self):
        return f'Custumer [{self.id}, {self.nome}, {self.documento}, {self.consulta_cpf}, {self.jusbrasil}] \n'

# Insert
def Insert_Path(id,nome,cpf,jusbrasil):
    data_insert = Customers(id=id,nome=nome,cpf=cpf,jusbrasil=jusbrasil)
    Session.add(data_insert)
    Session.commit()

# GET ALL
def Get_Path():
    Dict = {}
    data = Session.query(Customers).all()
    for i in data:
        Dict[i.cpf] = {"id":i.id,
            "nome": i.nome,
            "cpf": i.cpf,
            "Jusbrasil": i.jusbrasil,
            "consulta_armas": i.consulta_armas,
            "consulta_guns":i.consulta_guns,
            "consulta_cvm":i.consulta_cvmr,
            "consulta_involvement":i.consulta_involvement,
            "consulta_envolvimento":i.consulta_envolvimento,
            "consulta_fraud":i.consulta_fraud,
            "consulta_fraude":i.consulta_fraude,
            "consulta_lavagem":i.consulta_lavagem,
            "consulta_money_laudering":i.consulta_moneylaudering,
            "consulta_lawsuit":i.consulta_lawsuit,
            "consulta_processos":i.consulta_processos,
            "consulta_regulation":i.consulta_regulation,
            "maps_frontal" : i.maps_frontal,
            "maps_planta" : i.maps_planta
            }
    
    return Dict

# GET BY CPF
def Get_Path_imagens(cpf):
    Dict = {}

    data = Session.query(Customers).filter(Customers.cpf == cpf)
    for i in data:
        Dict = {"id":i.id,
            "nome": i.nome,
            "cpf": i.cpf,
            "Jusbrasil": i.jusbrasil,
            "consulta_armas": i.consulta_armas,
            "consulta_guns":i.consulta_guns,
            "consulta_cvm":i.consulta_cvmr,
            "consulta_involvement":i.consulta_involvement,
            "consulta_envolvimento":i.consulta_envolvimento,
            "consulta_fraud":i.consulta_fraud,
            "consulta_fraude":i.consulta_fraude,
            "consulta_lavagem":i.consulta_lavagem,
            "consulta_money_laudering":i.consulta_moneylaudering,
            "consulta_lawsuit":i.consulta_lawsuit,
            "consulta_processos":i.consulta_processos,
            "consulta_regulation":i.consulta_regulation,
            "maps_frontal" : i.maps_frontal,
            "maps_planta" : i.maps_planta
            }

    return Dict

# UPDATE
def Update_Imagem(cpf,campo,valor):
    Session.query(Customers).filter(Customers.cpf == cpf).update({campo:valor})
    Session.commit()

# DELETE
def Delete_imagem(cpf):
    Session.query(Customers).filter(Customers.cpf == cpf).delete()
    Session.commit()





# TESTES:

# with open("src/asset/15103414716/PortalTransparencia.png", "wb") as fh:
#     fh.write(base64.encodebytes(s))
#     Insert_Path(1, "RAVEL", "15103414716",fh)

# Insert_Path(1, "RAVEL", "15103414716")
# Update_Imagem("15103414716", "jusbrasil", "EU ESTOU FUNCIONANDO")

# Get_Path_imagens("15103414716")
    
# Get_Path()

# Delete_imagem("15103414716")
# Get_Path()