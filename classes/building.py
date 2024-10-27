class building:
    __name = None
    __architecture= None
    __owner = None
    def __init__(self,name,architecture,owner):
        self.__name = name
        self.__architecture = architecture
        self.__owner = owner

    def __str__(self):
        return f'Name = {self.__name}\nArchitecture = {self.__architecture}\nOwner = {self.__Owner}'

    def getName(self):
        return self.__name
    def getArchitecture(self):
        return self.__architecture
    def getOwner(self):
        return self.__owner
    
