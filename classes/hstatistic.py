class Statistic:
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

        def getHealth(health):
            return self.__health
        def getMana(mana):
            return self.__mana
        def getAttack(attack):
            return self.__attack
        def getDefense(defense):
            return self.__defense
        def getElement(element):
            return self.__element
        def getRacism(racism):
            return self.__racism
        def getCrit(crit):
            return self.__crit
        def getCritModifier(critModifier):
            return self.__critModifier        
