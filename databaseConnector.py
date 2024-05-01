from mysql.connector import Error
import mysql.connector

class databaseConnector:

    # connection = ""
    
    def __init__(self,hostname):
        self.connection = ""
        self.hostname = hostname

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host= self.hostname,
                port=3306,
                user='root',
                password='*Q1w2e3r4',
                db='fuentes'
            )
            if self.connection.is_connected():
                print("Database connected successfully")
                
        except Error as ex:
            print("Error during connection: {}".format(ex))

    def disconnectDB(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection closed.")

    def insertRow(self,data):
        cursor  = self.connection.cursor()

        cursor.executemany("""INSERT INTO fuente (contenido, fecha) VALUES (%s,%s)""", data)
        self.connection.commit()

