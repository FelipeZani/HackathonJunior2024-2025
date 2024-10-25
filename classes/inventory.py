class hinventory:
    __maxWeight = None
    __dicItem = None
    def __init__(self,maxWeight,dicItem):
        self.__maxWeight = maxWeight
        self.__dicItem = dicItem
    
    def __str__(self):
        return f'MaxWeight = {self.__maxWeight}\nDicItem = {self.__dicItem}\n'
        
    def getMaxWeight(self):
        return self.__maxWeight
    def getDicItem(self):
        return self.__dicItem
    
    
        
