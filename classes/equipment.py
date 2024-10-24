class equipment:
    __helmet = None
    __chestplate = None
    __leggings = None
    __boots = None
    __ring1 = None
    __ring2 = None
    __mainHold = None
    __secondHold = None
    
    def __init__(self,helmet,chestplate,leggings,boots,ring1,ring2,mainHold,secondHold):
        self.__helmet = helmet
        self.__chestplate = chestplate
        self.__leggings = leggings
        self.__boots = boots
        self.__ring1 = ring1
        self.__ring2 = ring2
        self.__mainHold = mainHold
        self.__secondHold = secondHold
        
    def getHelemet(self):
        return self.helmet
    def getChestplate(self):
        return self.chestplate
    def getLeggings(self):
        return self.leggings
    def getBoots(self):
        return self.boots
    def getRing1(self):
        return self.ring1
    def getRing2(self):
        return self.ring2
    def getMainHold(self):
        return self.mainHold
    def getSecondHold(self):
        return self.secondHold
    
        
        
