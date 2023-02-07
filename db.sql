use postgres;

CREATE TABLE Customers(
    id INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(15) NOT NULL,
    Consulta_CPF BYTEA,
    JusBrasil BYTEA,
    Consulta_Armas BYTEA,
    Consulta_Guns BYTEA,
    Consulta_CVMR BYTEA,
    Consulta_Envolvimento BYTEA,
    Consulta_Fraud BYTEA,
    Consulta_Fraude BYTEA,
    Consulta_Involvement BYTEA,
    Consulta_Lavagem BYTEA,
    Consulta_Lawsuit BYTEA,
    Consulta_MoneyLaudering BYTEA,
    Consulta_Processos BYTEA,
    Consulta_Regulation BYTEA,
    Maps_Frontal BYTEA,
    Maps_Planta BYTEA,
        PRIMARY KEY(cpf)
)



