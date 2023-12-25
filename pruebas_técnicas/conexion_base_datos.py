""" Realiza una conexion desde python a una base de datos de mysql 
#Host: mysql-5707.dinaserver.com
#Port: 3306
#User:mouredev_read
#Password: moredev_pass
#Database: moure_test"""
#!  Cunado realices la conexión, lanza la siguiente consulta e imprime el resultado: - SELECT * FROM `challengues`
#! Podemas usar las librerias que queramos.

"""Para establecer una conexión con una base de datos MySQL utilizando mysql.connector.connect(), necesitas proporcionar los siguientes argumentos:

user: El nombre de usuario para autenticarse en la base de datos.
password: La contraseña para autenticarse en la base de datos.
host: El nombre del host donde se encuentra la base de datos. Puede ser un nombre de dominio o una dirección IP.
database: El nombre de la base de datos a la que te quieres conectar.
Aquí te dejo un ejemplo de cómo puedes modificar tu código para establecer una conexión con la base de datos:"""
# Importamos el módulo mysql.connector para poder conectarnos a MySQL
import mysql.connector

# Creamos un diccionario con las credenciales y la información de la base de datos
config = {
    "host": "mysql-5707.dinaserver.com",  # El nombre del host donde se encuentra la base de datos
    "port": "3306",  # El puerto en el que el servidor MySQL está escuchando
    "database": "moure_test",  # El nombre de la base de datos a la que queremos conectarnos
    "user": "mouredev_read",  # El nombre de usuario para autenticarse en la base de datos
    "password": "mouredev_pass"  # La contraseña para autenticarse en la base de datos
}

# Establecemos una conexión con la base de datos utilizando las credenciales y la información del diccionario config
connection = mysql.connector.connect(**config)

# Creamos un objeto cursor, que nos permitirá ejecutar comandos SQL
cursor = connection.cursor()

# Definimos la consulta SQL que queremos ejecutar
query = "SELECT * FROM challenges"

# Ejecutamos la consulta SQL
cursor.execute(query)

# Obtenemos todos los registros devueltos por la consulta
result = cursor.fetchall()

# Iteramos sobre cada fila del resultado e imprimimos la fila
for row in result:
    print(row)

# Cerramos el cursor y la conexión a la base de datos
cursor.close()
connection.close()