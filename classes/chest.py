from classes.building import building

class chest(building):

    __inventory = None
    __build = None
    def __init__(self,name,architecture,owner,inventory,build):
        super().__init__(name,architecture,owner)
        self.__inventory = inventory
        self.__build = build

    def getInventory(self):
        return self.__inventory
    def getBuild(self):
        return self.__build
