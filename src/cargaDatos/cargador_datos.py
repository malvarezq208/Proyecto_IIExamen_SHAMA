

import pandas as pd
import os
import csv

#Definicion clase cargador_datos CSV de la carpeta data-raw
class cargador_datos:

    #Definicion del construcutor
    def __init__(self, ruta_archivo):
        self.__ruta_archivo = ruta_archivo #Variable que guarda la ruta del archivo
        self.__encabezado = None #Variable que me
        self.__separador = None #Variable que determina el tipo de separador del CSV
        self.__columnas_validas = None
        self.__decimal = None #Variable que determina el decimal del csv
        self.__df = None #Varible que guarda el archivo CSV en un dataframe

    @property
    def ruta_archivo(self):
        return self.__ruta_archivo
    @property
    def encabezado(self):
        return self.__encabezado
    @property
    def separador(self):
        return self.__separador
    @property
    def columnas_validas(self):
        return self.__columnas_validas
    @property
    def decimal(self):
        return self.__decimal
    @property
    def df(self):
        return self.__df

    @ruta_archivo.setter
    def ruta_archivo(self,ruta_archivo):
        self.__ruta_archivo=ruta_archivo

    @encabezado.setter
    def encabezado(self,encabezado):
        self.__encabezado=encabezado

    @separador.setter
    def separador(self,separador):
        self.__separador=separador

    @columnas_validas.setter
    def columnas_validas(self,columnas_validas):
        self.__columnas_validas=columnas_validas

    @decimal.setter
    def decimal(self,decimal):
        self.__decimal=decimal

    @df.setter
    def df(self,df):
        self.__df=df



    #Metodo deteccion_archivo
    #Dicho metodo nos ayuda a conocer el tipo de separador y decimal para realizar la carga de archivo
    def deteccion_archivo(self):
    #With Permite cerrar el archivo cuando se termine de usar
    #f.readline() lee la primera linea del archivo y la guarda en un CSV

        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Construir la ruta completa al CSV

        self.__ruta_archivo = os.path.join(base_dir, "..", "..", self.__ruta_archivo)
        self.__ruta_archivo = os.path.normpath(self.__ruta_archivo)  # Normaliza la ruta

        with open(self.__ruta_archivo, 'r', encoding='utf-8') as f:
            primera_linea = f.readline()

        # Detectar separador
        #csv.Sniffer() analiza automaticamente el formato de un archivo CSV en este caso usamos delimiter
        self.__separador = csv.Sniffer().sniff(primera_linea).delimiter

        # Detectar decimal (Verificacion de la primera linea )
        # Si hay comas y no hay puntos entonces se asume que la coma es el separador decimal
        self.__decimal = ',' if ',' in primera_linea and '.' not in primera_linea else '.'
        return print(self.__df)

        #Metodo leer_archivo
        #Dicho metodo carga el metodo deteccion_archivo y lo proceso para crear el dt
    def leer_archivo(self):
        self.deteccion_archivo()  # Asegura que los parámetros estén definidos

        # Leer el encabezado para contar columnas válidas
        #strip()= Elimina espacios en blanco al principio y final de la cadena de texto
        #split()= Divide una cadena de texto en partes
        with open(self.__ruta_archivo) as f:
            encabezado = f.readline().strip().split(self.separador)
            self.__columnas_validas = [col for col in encabezado if col]  # Eliminar vacíos

            # Leer el archivo con los parámetros detectados tomados del metodo deteccion_archivo()
            self.__df = pd.read_csv(
                self.__ruta_archivo,
                sep=self.__separador,
                decimal=self.__decimal,
                usecols=self.__columnas_validas, #Especifica la columnas que se desean cargar
                skiprows=1, #omite la primera fila del archivo csv
                names=self.__columnas_validas #Asigna nombres a las columnas
            )

            print("Su archivo fue cargado correctamente. \n")
            print(f"El archivo cargador fue cargado de la siguiente ruta {self.ruta_archivo}\n A continuacion le muestro el dataset \n")
            print(self.__df)
            print("---------------------------------------------------------------------------------------------------\n")

        return



