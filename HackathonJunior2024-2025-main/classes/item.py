from classes.hstatistic import statistic

class item:
    __name = None
    __weight = None
    __stats = None

    def __init__(self,name, weight, stats):
        self.__name = name
        self.__weight = weight
        self.__stats = stats

    def getName(self):
        return self.__name
    def getWeight(self):
        return self.__weight
    def getStats(self):
        return self.__stats
