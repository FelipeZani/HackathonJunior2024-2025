class role:
    __name = None
    __stats = None

    def __init__(self, name, stats):
        self.__name = name
        self.__stats = stats
    def __str__(self):
        return f'   +Role Name = {self.__name}\n   +Role Bonus :\n{self.__stats}'

    def getName(self):
        return self.__name
    def getStats(self):
        return self.__stats
