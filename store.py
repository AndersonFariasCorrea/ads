# pip install mysql-connector-python
# biblioteca de conexao com o banco mysql
import mysql.connector

# meu arquivo com os dados de conexao
import db

# biblioteca regax para tratamento de entradas e formatacoes
import re

# padrao 1 ou 0 para productSituationUpdate(), situacao de um produto
pattern = r'^[01]$'

try:
    # cria a conexao com o banco de dados
    mydb = mysql.connector.connect(
        host=db.DB_HOST,
        user=db.DB_USER,
        password=db.DB_PASS,
        database=db.DB_NAME
    )

    mycursor = mydb.cursor()

    # declaracao da funcao para insercao de produtos no banco
    def insertProduct():
        # variaveis de entrada do usuario, é recomendado adicionar esterelizacao nas entradas dos usuarios
        nome_prod = input("nome do produto:\t")
        quant_prod = input("quantidade do produto:\t")
        unit_value = input("valor unitario do produto:\tR$ ")
        situation_prod = input("situacao do produto\n1 ativo ou 0 desativado:\t")

        # query sql para insercao no banco
        sql = "INSERT INTO products (nome_prod, quant_prod, unit_value, situation_prod) VALUES (%s, %s, %s, %s);"
        val = (str(nome_prod), int(quant_prod), float(unit_value), int(situation_prod))
        # execucao da query
        mycursor.execute(sql, val)

        mydb.commit()

        # returno sobre o insert
        print(mycursor.rowcount, "produto inserido.\n")

    # declaracao da funcao de consulta aos dados no banco
    def queryProducts():

        #query select todos os dados da table products
        mycursor.execute("SELECT * FROM products")

        # faz o fetch dos dados para uma array
        myresult = mycursor.fetchall()

        # verifica se a array retornada não está vazia
        if len(myresult) != 0:
            
            # headers da table retornada
            print("codigo, nome, quant, val_BRL, situacao")
            # saida dos valores em tela
            for x in myresult:
                if x != '':
                    print(x)
        
        # caso a array estaja vazio, tamanho de array == 0
        else:
            print("Nao ha produto(s) cadastrado(s)!\n")

    # declaracao da funcao atualizar situacao de um produto
    def productSituationUpdate():
        mycursor = mydb.cursor()

        # usuario deve informar o codigo do produto
        cod_prod = input("Codigo do produto:\t")

        # query seleciona produto com o codigo informado para verificar sua existencia
        sql = "SELECT * FROM products WHERE cod_prod = %s"
        adr = (cod_prod, )

        # execucao da query
        mycursor.execute(sql, adr)

        # faz o fetch dos dados para uma array
        myresult = mycursor.fetchall()

        # declaracao de x vazio
        if len(myresult) > 0:
            # se o produto existe, usuario informa qual quer que seja a situacao do produto
            situation_prod = input("Nova situacao do produto:\t")

            # valida a entrada do usuario, sendo 1 ou 0
            if re.match(pattern, situation_prod):

                # query para atualizacao do produto com codigo e situacao passados pelo usuario
                sql = "UPDATE products SET situation_prod = %s WHERE cod_prod = %s"
                val = (situation_prod, cod_prod)

                # execucao da query
                mycursor.execute(sql, val)

                mydb.commit()

                # retorno positivo da insercao
                print(mycursor.rowcount, "produto(s) afetado(s)\n")
            else:
                # o usuario nao informou uma situacao invalida para o produto (nao foi 1 e nem 0)
                input('Situação Invalida!\n')
        else:
            # caso nao seja localizado produto com o codigo informado
            print("Nao ha produto com o codigo informado!\n")


    # declaracao vazia de variavel que inicializa a escolha do usuario
    userChoise = None

    # loop para a acao que o usuario deseja performar
    while userChoise != "s":

        # usuario informa qual acao deseja realizar
        userChoise = input("Informe a acao a ser performada.\n(i) Inserir produto\n(a) Atualizar produto\n(c) Consultar produtos\n(s) Sair:\t")

        # usuario deseja inserir um novo produto
        if userChoise == 'i':
            insertProduct()

        # usuario deseja atualizar um produto
        elif userChoise == 'a':
            productSituationUpdate()

        # usuario deseja consultar produtos cadastrados
        elif userChoise == 'c':
            queryProducts()

except mysql.connector.Error as error:
    print("Erro ao conectar ao MySQL:", error)

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
# <!--Andyです-->