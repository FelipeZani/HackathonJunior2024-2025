from classes.building import building

class chest(building):

    __inventory = None
    def __init__(self,name,architecture,owner,inventory):
        super.__init__(name,architecture,owner)
        self.__inventory = inventory

    def getInventory(self):
        return self.__inventory
