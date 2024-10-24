
class skills:
    __name = None
    __level = None
    __description = None
    __delay = None
    def __init__(self,name,level,description,delay):
        self.__name = name
        self.__level = level
        self.__description = description
        self.__delay = delay

    def getName(self):
        return self.__name
    def getLevel(self):
        return self.__level
    def getDescription(self):
        return self.__description
    def getDelay(self):
        return self.__delay