import sys
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='hellsing02',
    database='banco'
    )


def insert(cpf, nome, senha):
    try:
        meucursor = mydb.cursor()
        query = 'INSERT INTO clientes VALUES (%s, %s, 0, %s, 0)'
        values = (cpf, nome, int(senha))
        meucursor.execute(query, values)
        mydb.commit()
    except mysql.connector.errors.IntegrityError:
        print ("Valores duplicados!")
        return False22

def criar():
    nome_cliente = input("Digite seu Nome: ")
    cpf_cliente = input("Digite seu CPF: ")
    senha_cliente = int(input("Digite sua senha: "))
    if insert(cpf_cliente,nome_cliente,senha_cliente) == False:
        print("")
    else:
        try:
            insert(cpf_cliente,nome_cliente,senha_cliente)
            print("Cliente adicionado com sucesso!")
        except:
            print("Erro! Tente novamente com os dados corretos.")

def select(cpf_cliente_cadastrado):
    meucursor = mydb.cursor()
    value = str(cpf_cliente_cadastrado)
    query = "SELECT * FROM clientes WHERE cpf = "
    meucursor.execute(query+value)
    result = meucursor.fetchall()
    return result

def autenticacao():
    cpf = str(input('Digite seu CPF: '))
    senha = int(input('Digite sua Senha: '))
    resultados = select(cpf)
    if resultados[0][3] == senha:
        return resultados, True
    else:
        return resultados, False

def depositar():
    valores = autenticacao()
    if valores[1]:
        novovalor = input('Digite o valor a ser colocado: ')
        cursor = mydb.cursor()
        query = "UPDATE clientes SET saldo = {0} WHERE cpf = '{1}'".format(novovalor,valores[0][0][0])
        cursor.execute(query)
        mydb.commit()
        print("Valor adicionado com sucesso!")
    else:
        return False

def saldo():
    values = autenticacao()
    if values[1]:
        cursor = mydb.cursor()
        query = "SELECT saldo FROM clientes WHERE cpf = "
        cursor.execute(query+values[0][0][0])
        result = cursor.fetchone()
        valor = result[0]
        print("Seu Saldo é R$%.2f" %valor)
    else:
        return False

def sacar():
    values = autenticacao()
    if values [1]:
        cursor = mydb.cursor()
        query = "SELECT saldo FROM clientes WHERE cpf = "
        cursor.execute(query+values[0][0][0])
        result = cursor.fetchone()
        valor = result[0]
        saque = float(input('Qual valor a ser sacado?'))
        transf = valor-saque
        if transf > 0:
            cursor = mydb.cursor()
            query = "UPDATE clientes SET saldo = {0} WHERE cpf = '{1}'".format(transf,values[0][0][0])
            cursor.execute(query)
            mydb.commit()
            print("Saque efetuado!")
        else:
            print("Sem saldo!")
    else:
        return False

    

criar()
depositar()
sacar()
saldo()