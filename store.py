import mysql.connector
import re

pattern = r'^[01]$'

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="store",
  password="yourDatabasePassword",
  database="store"
)

mycursor = mydb.cursor()

def insertProduct():
    nome_prod = input("nome do produto:\t")
    quant_prod = input("quantidade do produto:\t")
    unit_value = input("valor unitario do produto:\tR$ ")
    situation_prod = input("situacao do produto\n1 ativo ou 0 desativado:\t")

    sql = "INSERT INTO products (nome_prod, quant_prod, unit_value, situation_prod) VALUES (%s, %s, %s, %s);"
    val = (str(nome_prod), int(quant_prod), float(unit_value), int(situation_prod))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "produto inserido.")

def queryProducts():
    mycursor.execute("SELECT * FROM products")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def productSituationUpdate():
    cod_prod = input("Codigo do produto:\t")

    if re.match(pattern, cod_prod):

        sql = "SELECT * FROM products WHERE cod_prod = %s"
        adr = (cod_prod, )

        mycursor.execute(sql, adr)

        myresult = mycursor.fetchall()
        x = ''
        for x in myresult:
            x = x

        situation_prod = input("situacao do produto:\t")
        mycursor = mydb.cursor()
        sql = "UPDATE products SET situation_prod = %s WHERE cod_prod = %s"
        val = (situation_prod, cod_prod)

        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "produto(s) afetado(s)")
    else:
        input('Entrada Invalida!')

userChoise = ''
while userChoise != "s":
    userChoise = input("Informe a acao a ser performada.\n(i Inserir produto)\n(a Atualizar produto)\n(c Consultar produtos)\n(s Sair):\t")
    if userChoise == 'i':
        insertProduct()
    elif userChoise == 'a':
        productSituationUpdate()
    elif userChoise == 'p':
        queryProducts()
