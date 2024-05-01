from databaseConnector import databaseConnector
from lectorAPA import inicializar
import csv

from datetime import date
today = date.today()

def main():
    debug = True
    guardar = False
    recursivo = True
 
    
    data = []
    contenido_por_fuente = []

    contenido_por_fuente = inicializar( recursivo )

    if debug:
        for fuente in contenido_por_fuente: 
            if len(fuente) < 400:
                print("=====================")
                print(fuente[:400])
                print("=====================")
                
        # Generar archivo CSV en la misma carpeta que el script
        nombre_archivo = 'datos_db.csv'
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv, delimiter=';')  # Usar punto y coma como delimitador
            escritor_csv.writerow(['Contenido', 'Fecha'])
            for fuente in contenido_por_fuente: 
                data.append([fuente[:400].encode('utf-8'), today])  # Codificar la cadena fuente como bytes UTF-8
                escritor_csv.writerow([fuente.encode('utf-8')])  # Codificar la cadena como bytes UTF-8 antes de escribir en el CSV

        print(f'Se ha generado el archivo CSV "{nombre_archivo}" en la misma carpeta que el script.')

    if guardar:
        print("Guardar en base de datos")
        for fuente in contenido_por_fuente: 
            data.append( ( fuente[:400], today) )

        database = databaseConnector("localhost")
        database.conectar()
        database.insertRow(data)        


if __name__ == "__main__":
    main()
