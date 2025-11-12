class jugador:
    def __init__(self,player="",team="",camisa=0,nation="",position="",age=0):  #Definicion constructor
        self.__player=player
        self.__team=team
        self.__camisa=camisa
        self.__nation= nation
        self.position=position
        self.__age=age
    
    def __str__(self):
        return f"Player:{self.__player}\n Team:{self.__team} \n Camisa:{self.__camisa} \n Nation:{self.__nation},\n Position:{self.position}\n Age:{self.__age}"
    


        
