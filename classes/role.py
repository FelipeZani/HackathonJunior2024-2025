from hstatistic import Statistic

class Role:
    __nom = None
    __type = None
    __stats = None

    def __init__(self, nom, type, stats):
        self.__nom = nom
        self.__type = type
        self.__stats = stats

        def getNom(nom):
            return self.__nom
        def getType(type):
            return self.__type
        def getStats(stats):
            return self.__stats
