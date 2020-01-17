import sys
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='hellsing02',
    database='banco'
    )




def criar():
    nome_cliente = input("Digite seu Nome: ")
    cpf_cliente = input("Digite seu CPF: ")
    senha_cliente = int(input("Digite sua senha: "))
    def insert(cpf, nome, senha):
        meucursor = mydb.cursor()
        query = 'INSERT INTO clientes VALUES (%s, %s, 0, %s, 0)'
        values = (cpf, nome, senha)
        meucursor.execute(query, values)
        mydb.commit()
    insert(cpf_cliente,nome_cliente,senha_cliente)
    print("Cliente adicionado com sucesso!")

criar()


    