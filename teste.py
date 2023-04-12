import mysql.connector
import re

pattern = r'^[01]$'
x = ''

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="store",
  password="yourDatabasePassword",
  database="store"
)

mycursor = mydb.cursor()

def productSituationUpdate():
    cod_prod = input("Codigo do produto:\t")

    if re.match(pattern, cod_prod):

        sql = "SELECT * FROM products WHERE cod_prod = %s"
        adr = (cod_prod, )

        mycursor.execute(sql, adr)

        myresult = mycursor.fetchall()
        
        for x in myresult:
            x = x
        else:
            input('Entrada Invalida!')

productSituationUpdate()
print(x)