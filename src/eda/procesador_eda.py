# Importamos las librerías necesarias.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import os # Libreria para manejar rutas de archivos.

#Iniciamos la clase.

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
        print('Informacion General de la Premier League:\n')
        print('Head')
        print (self.__DF_PremierLeague.head(), '\n')
        print('Informacion')
        print (self.__DF_PremierLeague.info(), '\n')
        print('Estadisticas')
        print (self.__DF_PremierLeague.describe())

#-------------------------------------------------------------------------------------------------------------------#

# 2. Metodo con el que podremos limpiar textos ya sea el nombre de los jugadores, equipos, etc.
    def limpiar_texto(self):
        columnas_texto = self.__DF_PremierLeague.select_dtypes(include=['object', 'category']).columns # Selecciona las columnas de tipo texto.

        for columna in columnas_texto:
            self.__DF_PremierLeague[columna] = (self.__DF_PremierLeague[columna].astype(str).apply(
                lambda x: x.encode('utf-8', 'ignore').decode('utf-8', 'ignore'))
            ) # Asegura que los datos sean de tipo string.

#-------------------------------------------------------------------------------------------------------------------#

# 3. Metodo en el cual obtendremos aquellos datos nulos.
    def datos_nulos(self):
        print('Este dataset tiene nulos en las siguiente columnas: \n')
        print(self.__DF_PremierLeague.isnull().sum())

# Dentro de este segundo metodo tendremos 2 metodos que ayuden a eliminar o imputar los datos nulos.
# Eliminar los datos nulos.
    def eliminar_datos_nulos(self):
        self.__DF_PremierLeague.dropna(inplace=True)
        print('Los datos nulos han sido eliminados')

# Imputar los datos nulos (utilizar la media para los numericos y la moda para las categoricas).
    def imputar_datos_nulos(self):
        for columnas in self.__DF_PremierLeague.columns:
            if self.__DF_PremierLeague[columnas].dtype in [np.float64, np.int64]:
                self.__DF_PremierLeague[columnas].fillna(self.__DF_PremierLeague[columnas].mean(), inplace=True)
            else:
                self.__DF_PremierLeague[columnas].fillna(self.__DF_PremierLeague[columnas].mode()[0], inplace=True)
        
        print('Los datos nulos han sido imputados correctamente')

#-------------------------------------------------------------------------------------------------------------------#
# 4. Metodo en cual podremos obtener los valores duplicados.
    def datos_duplicados(self):
        print('Este dataset tiene los siguientes datos duplicados: \n') 
        print(self.__DF_PremierLeague.duplicated().sum())

# Ese metodo nos da el numero de filas duplicadas, en este nuevo metodo vamos a eliminar esos datos duplicados.
    def eliminar_datos_duplicados(self):
        self.__DF_PremierLeague.drop_duplicates(inplace=True)
        print('Los datos duplicados del dataset han sido eliminados correctamente')

#-------------------------------------------------------------------------------------------------------------------#
# 5. metodo para limpiar la edad de los juagadores ya que solo queremos el primer numero (29-343).
    def correccion_edad(self):
        self.__DF_PremierLeague['Age'] = self.__DF_PremierLeague['Age'].astype(str).str.split('-').str[0].astype(int)
        print('La columna de Age ha sido corregida correctamente')

#-------------------------------------------------------------------------------------------------------------------#
# 6. Metodo con el que vamos a corregir la columna '#' por 'Number' que es numero de la camiseta del jugador.
    def numero_camiseta(self):
        self.__DF_PremierLeague.rename(columns={'#': 'Number'}, inplace=True)
        print("La columna '#' ha sido renombrada a 'Number' correctamente")

#-------------------------------------------------------------------------------------------------------------------#
# 7. Metodo de normalizacion de categorias equipo-posicion.
    def normalizacion_categorias(self):
        self.__DF_PremierLeague['Team'] = (self.__DF_PremierLeague['Team'].astype(str).str.title().str.strip()) # Normaliza los nombres de los equipos.
        self.__DF_PremierLeague['Position'] = (self.__DF_PremierLeague['Position'].astype(str).str.upper().str.strip()) # Normaliza las posiciones de los jugadores.
        print('Las categorias de equipo y posicion han sido normalizadas')

#-------------------------------------------------------------------------------------------------------------------#
# 8. Metodo para poder guardar nuestro csv limpio y guardarlo en la carpeta processed.
    def csv_limpio(self, ruta_guardar_csv = 'data/processed/premier_clean.csv'):
        carpeta = os.path.dirname(ruta_guardar_csv) # Obtenemos la carpeta del path proporcionado.
        os.makedirs(carpeta, exist_ok=True) # Creamos la carpeta si no existe.
        self.__DF_PremierLeague.to_csv(ruta_guardar_csv, index=False) # Guardamos el DataFrame como un archivo CSV.
        print('El Dataset limpio se a guardado en la ruta:', {ruta_guardar_csv})

#-------------------------------------------------------------------------------------------------------------------#
#9 Matriz de correlacion
    def eda_matriz_correlacion(self):
    #herramienta estadística que muestra cómo se relacionan entre si las diferentes variables numericas dentro de un conjunto datos

        # Calcular la matriz de correlación
        matriz_correlacion = self.__DF_PremierLeague.corr()

        # Mostrar la matriz como un mapa de calor
        plt.figure(figsize=(10, 8))
        sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Matriz de Correlación')
        plt.show()

        return matriz_correlacion

#-------------------------------------------------------------------------------------------------------------------#
#10 Histograma para cada columna numerica
def eda_histogramas(self):

#Genera un histograma para cada columna numérica del DataFrame.

    columnas_numericas = self.__DF_PremierLeague.select_dtypes(include=['number']).columns

    for columna in columnas_numericas:
        plt.figure(figsize=(8, 5))
        sns.histplot(self.__DF_PremierLeague[columna], kde=True, bins=30, color='skyblue')
        plt.title(f'Distribución de {columna}')
        plt.xlabel(columna)
        plt.ylabel('Frecuencia')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

#-------------------------------------------------------------------------------------------------------------------#
#11 Boxplot

def generar_boxplots(self):

#Genera un boxplot para cada columna numérica del DataFrame.


    columnas_numericas = self.__DF_PremierLeague.select_dtypes(include=['number']).columns

    for columna in columnas_numericas:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=self.__DF_PremierLeague[columna], color='lightgreen')
        plt.title(f'Boxplot de {columna}')
        plt.xlabel(columna)
        plt.grid(True)
        plt.tight_layout()
        plt.show()


#-------------------------------------------------------------------------------------------------------------------#
        print('El Dataset limpio se a guardado en la ruta:', {ruta_guardar_csv})
