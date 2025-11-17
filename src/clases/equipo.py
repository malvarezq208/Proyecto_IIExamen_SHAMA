class Equipo:
    def __init__(self, estadio, tecnico, jugadores, nom_equipo, titulos_ganados=0):
        self.__estadio = estadio
        self.__tecnico = tecnico
        self.__jugadores = jugadores
        self.__nom_equipo = nom_equipo
        self.__titulos_ganados = titulos_ganados

# Creamos un str para poder observar la informacion del equipo.
    def __str__(self):
        return f'Informacion General:\nEquipo: {self.__nom_equipo}\nEstadio: {self.__estadio}\nTécnico: {self.__tecnico}\nJugadores: {", ".join(self.__jugadores)}\nTítulos Ganados: {self.__titulos_ganados}'
        # Aqui el .join se utiliza para convertir la lista de jugadores en una cadena separada por comas.

# Creamos los gettter (property) para obtener los atributos privados.
    @property
    def estadio(self):
        return self.__estadio

    @property
    def tecnico(self):
        return self.__tecnico

    @property
    def jugadores(self):
        return self.__jugadores

    @property
    def nom_equipo(self):
        return self.__nom_equipo

    @property
    def titulos_ganados(self):
        return self.__titulos_ganados
    
# Creamos los setter para modificar los atributos privados.
    @estadio.setter
    def estadio(self, nuevo_estadio):
        self.__estadio = nuevo_estadio

    @tecnico.setter
    def tecnico(self, nuevo_tecnico):
        self.__tecnico = nuevo_tecnico

    @jugadores.setter
    def jugadores(self, nuevos_jugadores):
        self.__jugadores = nuevos_jugadores

    @nom_equipo.setter
    def nom_equipo(self, nuevo_nombre):
        self.__nom_equipo = nuevo_nombre
    
    @titulos_ganados.setter
    def titulos_ganados(self, nuevos_titulos):
        self.__titulos_ganados = nuevos_titulos

# Iniciamos con algunos metodos para el modelo de equipo.
# 1. Metdod para agregar un jugador al equipo.
    def agregar_jugador(self, jugador):
        self.__jugadores.append(jugador)    

# 2. Metodo para poder eliminar a un jugador si esta en la lista.
    def eliminar_jugador(self, jugador):
        if jugador in self.__jugadores:
            self.__jugadores.remove(jugador)
        else:
            print(f'El jugador {jugador} no está en el equipo.')

# 3. Metodod para saber cuantos titulos ha ganado el equipo.
    def ganar_titulo(self):
        self.__titulos_ganados += 1
