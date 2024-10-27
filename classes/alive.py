class alive:
    __name = None
    __statistic = None
    __race = None
    __hostility = None
    __role = None
    __skills = None
    __inventory = None
    __equipment = None
    
    def __init__(self,name,stats,race,hostility,role,skills,inventory,equipment):
        self.__name = name
        self.__statistic= stats
        self.__race = race
        self.__hostility = hostility
        self.__role = role
        self.__skills = skills
        self.__inventory = inventory
        self.__equipment = equipment
    
    def __str__(self):
        return f'-Alive Name = {self.__name}\n-Alive Statistic :\n{self.__statistic}\n-Alive Race :\n{self.__race}\n-Alive Hostility = {self.__hostility}\n-Alive Role :\n{self.__role}\n-Alive SKills= {self.__skills}\n-Alive Inventory = {self.__inventory}\n-Alive Equipment = {self.__equipment}'

    
    def getName(self):
        return self.__name
    def getStats(self):
        return self.__statistic
    def getRace(self):
        return self.__race
    def getHostility(self):
        return self.__hostility
    def getRole(self):
        return self.__role
    def getSkills(self):
        return self.__skills
    def getInventory(self):
        return self.__inventory
    def getEquipment(self):
        return self.__equipment
    

        


