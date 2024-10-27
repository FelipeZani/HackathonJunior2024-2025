from classes.hstatistic import statistic

class role:
    __name = None
    __stats = None

    def __init__(self, name, stats):
        self.__name = name
        self.__stats = stats

    def __str__(self):
        return f'Name = {self.__name}\nStatistic = {self.__stats}'

    def getName(self):
        return self.__name
    def getStats(self):
        return self.__stats
