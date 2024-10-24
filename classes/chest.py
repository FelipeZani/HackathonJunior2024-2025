class chest:
    __name = None
    __inventory = None
    def __init__(self,name,inventory):
        self.__name = name
        self.__inventory = inventory

    def getName(self):
        return self.__name
    def getInventory(self):
        return self.__inventory
