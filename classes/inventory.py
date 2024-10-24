class Inventory:
    __maxWeight = None
    __weight = None
    __dicObject = None
    def __init__(self,maxWeight,weight,dicObject):
        self.__maxWeight = maxWeight
        self.__weight = weight
        self.__dicObject = dicObject
        
    def getMaxWeight(self):
        return self.__maxWeight
    def getWeight(self):
        return self.__weight
    def getDicObject(self):
        return self.__dicObject
    
    
        