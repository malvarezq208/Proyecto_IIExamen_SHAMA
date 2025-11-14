# Importamos las librerías necesarias.
import pandas as pd
import numpy as np

class ProcesadorEDA: # Creamos la clase ProcesadorEDA la cual nos ayudara a realizar un analisis EDA.
    def __init__(self, DF_PremierLeague = pd.DataFrame()): # Realizamos el constructor.
        self.__DF_PremierLeague = DF_PremierLeague # Aqui tenemos nustro atributo privado que almacena el DataFrame.
        self.__num_filas = DF_PremierLeague.shape[0] # Aqui tenemos nuestros atributos privados que almacenan el numero de filas y columnas.
        self.__num_columnas = DF_PremierLeague.shape[1]

# Creamos los propertys (getters) para acceder a los atributos privados.
    @property
    def DF_PremierLeague(self):
        return self.__DF_PremierLeague
    @property
    def num_filas(self):
        return self.__num_filas
    @property
    def num_columnas(self):
        return self.__num_columnas
    
# Creamos los setters para que podamos modificar los atributos privados si es necesario.
    @DF_PremierLeague.setter
    def DF_PremierLeague(self, DF_PremierLeague):
        self.__DF_PremierLeague = DF_PremierLeague
    @num_filas.setter
    def num_filas(self, num_filas):
        self.__num_filas = num_filas    
    @num_columnas.setter
    def num_columnas(self, num_columnas):
        self.__num_columnas = num_columnas

# Iniciamos con la agregacion de metodos que necesitaremos para el analisis EDA.
    
# 1. Metodo en el cual obtendremos informacion general del Dataset que se nos a proporcionado.
    def informacion_premier_league(self):
        print("Informacion General de la Premier League:\n")
        print("Head")
        print (self.__DF_PremierLeague.head(), "\n")
        print("Informacion")
        print (self.__DF_PremierLeague.info(), "\n")
        print("Estadisticas")
        print (self.__DF_PremierLeague.describe())



