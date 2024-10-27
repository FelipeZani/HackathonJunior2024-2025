class race:
    __name = None
    __origine = None
    __reputation = None
    __modif = None
    def __init__(self,name,origine,reputaion,modif):
        self.__name = name
        self.__origine = origine
        self.__reputation = reputaion
        self.__modif = modif
    
    def __str__(self):
        return f'   +Race Name = {self.__name}\n   +Race Origine = {self.__origine}\n   +Race Reputation = {self.__reputation}\n   +Race Bonus :\n{self.__modif}'

    def getName(self):
        return self.__name
    def getOrigine(self):
        return self.__origine
    def getReputation(self):
        return self.__reputation
    def getModif(self):
        return self.__modif
