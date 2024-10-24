from classes.hstatistic import statistic

class role:
    __nom = None
    __type = None
    __stats = None

    def __init__(self, nom, stats):
        self.__nom = nom
        self.__stats = stats

        def getNom(nom):
            return self.__nom
        def getStats(stats):
            return self.__stats
