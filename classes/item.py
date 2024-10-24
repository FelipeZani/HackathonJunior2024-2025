from hstatistics import Statistics

class item:
    __weight = None
    __stats = None

    def __init__(self, weight, stats):
        self.__weight = weight
        self.__stats = stats

    def getWeight(self):
        return self.__weight
    def getStats(self):
        return self.__stats
