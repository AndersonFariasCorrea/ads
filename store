import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="store",
  password="mypassword!",
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

    print(mycursor.rowcount, "record inserted.")

def queryProducts():
    mycursor.execute("SELECT * FROM products")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
userChoise = ''
while userChoise != "s":
    userChoise = input("Informe a acao a ser performada.\n(i Inserir produto)\n(C Consultar produtos)\n(s Sair):\t")
    if userChoise == 'i':
        insertProduct()
    elif userChoise == 'p':
        queryProducts()
