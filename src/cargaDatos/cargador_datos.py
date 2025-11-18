

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Definicion clase cargador_datos CSV de la carpeta data-raw
class cargador_datos:

    #Definicion del construcutor
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo #Variable que guarda la ruta del archivo
        self.encabezado = None #Variable que me
        self.separador = None #Variable que determina el tipo de separador del CSV
        self.columnas_validas = None
        self.decimal = None #Variable que determina el decimal del csv
        self.df = None #Varible que guarda el archivo CSV en un dataframe

    #Metodo deteccion_archivo
    #Dicho metodo nos ayuda a conocer el tipo de separador y decimal para realizar la carga de archivo
    def deteccion_archivo(self):
    #With Permite cerrar el archivo cuando se termine de usar
    #f.readline() lee la primera linea del archivo y la guarda en un CSV
        with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
            primera_linea = f.readline()

        # Detectar separador
        #csv.Sniffer() analiza automaticamente el formato de un archivo CSV en este caso usamos delimiter
        self.separador = csv.Sniffer().sniff(primera_linea).delimiter

        # Detectar decimal (Verificacion de la primera linea )
        # Si hay comas y no hay puntos entonces se asume que la coma es el separador decimal
        self.decimal = ',' if ',' in primera_linea and '.' not in primera_linea else '.'

        #Metodo leer_archivo
        #Dicho metodo carga el metodo deteccion_archivo y lo proceso para crear el dt
        def leer_archivo(self):
            self.deteccion_archivo()  # Asegura que los parámetros estén definidos

            # Leer el encabezado para contar columnas válidas
            #strip()= Elimina espacios en blanco al principio y final de la cadena de texto
            #split()= Divide una cadena de texto en partes
            with open(ruta) as f:
                encabezado = f.readline().strip().split(self.separador)
                self.columnas_validas = [col for col in encabezado if col]  # Eliminar vacíos

            # Leer el archivo con los parámetros detectados tomados del metodo deteccion_archivo()
            self.df = pd.read_csv(
                self.ruta_archivo,
                sep=self.separador,
                decimal=self.decimal,
                usecols=self.columnas_validas, #Especifica la columnas que se desean cargar
                skiprows=1, #omite la primera fila del archivo csv
                names=self.columnas_validas #Asigna nombres a las columnas
            )

            print("Su archivo fue cargado correctamente.")
            return self.df #Devuelve el CSV procesado

cargador = cargador_datos("ejemplo_estudiantes.csv")


# Visualización de Distribuciones Univariadas:

# Visualización de Distribuciones Univariadas:

# Histograma para cada columna numérica
for columna in cargador.df.select_dtypes(include=['number']).columns:
    sns.histplot(cargador.df[columna])
    plt.title(f'Distribución de {columna}')
    plt.show()

# Boxplot para cada columna numérica
for columna in cargador.df.select_dtypes(include=['number']).columns:
    sns.boxplot(x=cargador.df[columna])
    plt.title(f'Boxplot de {columna}')
    plt.show()



