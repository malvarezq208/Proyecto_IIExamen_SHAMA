

import pandas as pd


class cargador_datos:

    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.encabezado = None
        self.separador = None
        self.columnas_validas = None
        self.decimal = None
        self.df = None

    def deteccion_archivo(self):
        with open(self.ruta_archivo, 'r', encoding='utf-8') as f:
            primera_linea = f.readline()

        # Detectar separador
        self.separador = csv.Sniffer().sniff(primera_linea).delimiter

        # Detectar decimal
        self.decimal = ',' if ',' in primera_linea and '.' not in primera_linea else '.'

        def leer_archivo(self):
            self.deteccion_archivo()  # Asegura que los parámetros estén definidos

            # Leer el encabezado para contar columnas válidas
            with open(ruta) as f:
                encabezado = f.readline().strip().split(self.separador)
                self.columnas_validas = [col for col in encabezado if col]  # Eliminar vacíos

            # Leer el archivo con los parámetros detectados
            self.df = pd.read_csv(
                self.ruta_archivo,
                sep=self.separador,
                decimal=self.decimal,
                usecols=self.columnas_validas,
                skiprows=1,
                names=self.columnas_validas
            )

            print("✅ Archivo cargado correctamente.")
            return self.df



