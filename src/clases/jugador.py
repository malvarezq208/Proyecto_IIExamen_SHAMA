class jugador:
    def __init__(self,player="",team="",camisa=0,nation="",position="",age=0):  #Definicion constructor
        self.__player=player
        self.__team=team
        self.__camisa=camisa
        self.__nation= nation
        self.__position=position
        self.__age=age
    
    def __str__(self):
        return f"Player:{self.__player}\n Team:{self.__team} \n Camisa:{self.__camisa} \n Nation:{self.__nation},\n Position:{self.position}\n Age:{self.__age}"
    
    #Player
    @property 
    def player(self):
        return self.__player

    @player.setter 
    def player(self, player):
        self.__player = player
    
    #Team
    @property
    def team(self):
        return self.__team
    
    @team.setter
    def team(self,team):
        self.__team=team
    
    #camisa
    @property
    def camisa(self):
        return self.__camisa
    
    @camisa.setter
    def camisa(self,camisa):
        self.__camisa=camisa
    
    #nation
    @property
    def nation(self):
        return self.__nation
    
    @nation.setter
    def nation(self,nation):
        self.__nation=nation

    #position
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self,position):
        self.__position=position

    #age
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def setter (self,age):
        self.__age=age




        
