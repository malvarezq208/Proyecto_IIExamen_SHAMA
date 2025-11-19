#Importacion de modulos
from cargaDatos.cargador_datos import cargador_datos
from eda.procesador_eda import ProcesadorEDA as pe


#-------------------------------------------------------------------------------------------------------------------#
#Carga de archivo CSV
#Instancias de la clase premier con clase cargador_datos
premier=cargador_datos("src/data/raw/premier.csv")
#Llamado al metodo de la clase cargador_datos
premier.leer_archivo()

#-------------------------------------------------------------------------------------------------------------------#
#Limpieza del archivo CSV premier
#Instancia de la clase ProcesadorEDA
procesador_eda=pe(premier.df)
#Llamado del metodo de la clase ProcesadorEDA
procesador_eda.ejecutar_eda()
#-------------------------------------------------------------------------------------------------------------------#







