import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizador: # Clase para realizar visualizaciones del dataset de premier_clean.csv
    def __init__(self, DF_PremierClean= pd.DataFrame()): 
        self.__DF_PremierClean = DF_PremierClean

    @property # Se crea el property para obtener el DataFrame
    def DF_PremierClean(self):
        return self.__DF_PremierClean
    
    @DF_PremierClean.setter # Se crea el setter para modificar el DataFrame
    def DF_PremierClean(self, DF_PremierClean):
        self.__DF_PremierClean = DF_PremierClean

# Iniciaremos a realizar algunos gráficos para poder interpretar esos resultados de una mejor manera.
# 1. Metodo: Grafico de distribución de goles 'Colmna Goals'.
    def grafico_goles(self): # Inicio del método.
        plt.figure(figsize=(10,6)) # Tamaño de la figura.
        sns.histplot(self.__DF_PremierClean['Goals'], bins=30, kde=True, color='blue') # Histograma con línea KDE (KDE: Dibuja una curva en nuestro grafico).
        plt.title('Distribución de Goles por Partido', fontsize=16) # Título del gráfico.
        plt.xlabel('Número de Goles', fontsize=14) # Titulo del eje X.
        plt.ylabel('Frecuencia', fontsize=14) # Titulo del eje Y.
        plt.grid(True) # Esta funcion realiza una cuadricula en el grafico para una mejor visualizacion.
        plt.show() # Muestra el gráfico.

#-------------------------------------------------------------------------------------------------------------------#
# 2. Metodo: Grafico de scatter plot entre las columnas 'Total Shoot' y 'Goals'.
    def grafico_shoot_goles(self): # Inicio del método.
        plt.figure(figsize=(10,6)) # Tamaño de la figura.
        sns.scatterplot(data=self.__DF_PremierClean, x='Total Shoot', y='Goals', color='green') # Scatter plot entre 'Total Shoot' y 'Goals'.
        plt.title('Relación entre Tiros Totales y Goles', fontsize=16) # Título del gráfico.
        plt.xlabel('Tiros Totales', fontsize=14) # Titulo del eje X.
        plt.ylabel('Goles', fontsize=14) # Titulo del eje Y.
        plt.grid(True) # Esta funcion realiza una cuadricula en el grafico para una mejor visualizacion.
        plt.show() # Muestra el gráfico.

#-------------------------------------------------------------------------------------------------------------------#
# 3. Metodo: Grafico heatmap de correlación entre las variables 'Yellow Cards', 'Red Cards' y 'Tackles'.
    def heatmap_correlacion(self): # Inicio del método.
        plt.figure(figsize=(8,6)) # Tamaño de la figura.
        correlacion = self.__DF_PremierClean[['Yellow Cards', 'Red Cards', 'Tackles']].corr() # Cálculo de la matriz de correlación.
        sns.heatmap(correlacion, annot=True, cmap='coolwarm', vmin=-1, vmax=1) # Mapa de calor con anotaciones.
        plt.title('Mapa de Calor de Correlación', fontsize=16) # Título del gráfico.
        plt.show() # Muestra el gráfico.

#-------------------------------------------------------------------------------------------------------------------#
# 4. Metodo: Grafico con el Top 10 de los goleadores de la Premier League.
    def top_10_goleadores(self): # Inicio del método.
        top_10 = self.__DF_PremierClean.groupby('Player')['Goals'].sum().nlargest(10).reset_index() # Esta linea agrupa por jugador, suma los goles, ordena del que hizo mas goles al que menos hizo y devuelve solo a los 10 jugadores con más goles.
        plt.figure(figsize=(12,6)) # Tamaño de la figura.
        sns.barplot(data=top_10, x='Player', y='Goals', palette='viridis') # Gráfico de barras para el top 10 de goleadores.
        plt.title('Top 10 Goleadores de la Premier League', fontsize=16) # Título del gráfico.
        plt.xlabel('Jugador', fontsize=14) # Titulo del eje X.
        plt.ylabel('Goles', fontsize=14) # Titulo del eje Y.
        plt.xticks(rotation=45) # Rotación de las etiquetas del eje X para mejor visualización.
        plt.show() # Muestra el gráfico.

#-------------------------------------------------------------------------------------------------------------------#
# 5. Metodo: Grafico con el Top 10 de los jugadores con más asistencias en la Premier League.
    def top_10_asistencias(self): # Inicio del método.
        top_10 = self.__DF_PremierClean.groupby('Player')['Assists'].sum().nlargest(10).reset_index() # Esta linea agrupa por jugador, suma las asistencias, ordena del que hizo mas asistencias al que menos hizo y devuelve solo a los 10 jugadores con más asistencias.
        plt.figure(figsize=(12,6)) # Tamaño de la figura.
        sns.barplot(data=top_10, x='Player', y='Assists', palette='magma') # Gráfico de barras para el top 10 de asistencias.
        plt.title('Top 10 Jugadores con Más Asistencias en la Premier League', fontsize=16) # Título del gráfico.
        plt.xlabel('Jugador', fontsize=14) # Titulo del eje X.
        plt.ylabel('Asistencias', fontsize=14) # Titulo del eje Y.
        plt.xticks(rotation=45) # Rotación de las etiquetas del eje X para mejor visualización.
        plt.show() # Muestra el gráfico.

#-------------------------------------------------------------------------------------------------------------------#
#6 Metodo: Grafico que determine en cual minuto del partido se anotan la mayor cantidad de goles.
#Para determinar en apuestas cual seria el mejor momento para apostar y acertar puntajes


#-------------------------------------------------------------------------------------------------------------------#
#7 Metodo: Grafico que muestre las tarjetas amrillas y rojas por  posiciones de los jugadores para determinar cual
# es la posicion con mas tarjetas.



