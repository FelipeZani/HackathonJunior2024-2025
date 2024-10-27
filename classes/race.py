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
        return f'Name = {self.__name}\nOrigine = {self.__origine}\nReputation = {self.__reputation}\nModif = {self.__modif}'

    def getName(self):
        return self.__name
    def getOrigine(self):
        return self.__origine
    def getReputation(self):
        return self.__reputation
    def getModif(self):
        return self.__modif
