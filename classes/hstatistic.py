class statistic:
    __health = None
    __mana = None
    __attack= None
    __defense = None
    __element = None
    __racism = None
    __crit = None
    __critModifier = None

    def __init__(self, health, mana, attack, defense, element, racism, crit, critModifier):
        self.__health = health
        self.__mana = mana
        self.__attack = attack
        self.__defense = defense
        self.__element = element
        self.__racism = racism
        self.__crit = crit
        self.__critModifier = critModifier
    
    def __str__(self):
        return f'      ->Health = {self.__health}\n      ->Mana = {self.__mana}\n      ->Attack = {self.__attack}\n      ->Defense= {self.__defense}\n      ->Element = {self.__element}\n      ->Racism = {self.__racism}\n      ->Crit = {self.__crit}\n      ->CritModifier = {self.__critModifier}'


    def getHealth(self):
        return self.__health
    def getMana(self):
        return self.__mana
    def getAttack(self):
        return self.__attack
    def getDefense(self):
        return self.__defense
    def getElement(self):
        return self.__element
    def getRacism(self):
        return self.__racism
    def getCrit(self):
        return self.__crit
    def getCritModifier(self):
        return self.__critModifier        
