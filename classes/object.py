from hstatistics import Statistics

class Object:
    __weight = None
    __type = None
    __stats = None

    def __init__(self, weight,type, stats):
        self.__weight = weight
        self.__type = type
        self.__stats = stats

    def getWeight(self):
        return self.__weight
    def getType(self):
        return self.__type
    def getStats(self):
        return self.__stats