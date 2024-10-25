from classes.item import item

class equipment():
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
        
    def __str__(self):
        return f'Helmet = {self.__helmet}\nChestplate = {self.__chestplate}\nLeggings = {self.__leggings}\nBoots = {self.__boots}\nRing1 = {self.__ring1}\nRing2 = {self.__ring2}\nMainHold = {self.__mainHold}\nSecondHold = {self.__secondHold}'

        
    def getHelemet(self):
        return self.__helmet
    def getChestplate(self):
        return self.__chestplate
    def getLeggings(self):
        return self.__leggings
    def getBoots(self):
        return self.__boots
    def getRing1(self):
        return self.__ring1
    def getRing2(self):
        return self.__ring2
    def getMainHold(self):
        return self.__mainHold
    def getSecondHold(self):
        return self.__secondHold
    
    
    def changeHelmet(self,itm):
        self.__helmet = itm
    def changeChestplate(self,itm):
        self.__chestplate = itm
    def changeLeggings(self,itm):
        self.__leggings = itm
    def changeBoots(self,itm):
        self.__boots = itm
    def changeRing1(self,itm):
        self.__ring1 = itm
    def changeRing2(self,itm):
        self.__ring2 = itm
    def changeMainHold(self,itm):
        self.__mainHold = itm
    def changeSecondHold(self,itm):
        self.__secondHold = itm
        
    
    def delHelmet(self):
        self.__helmet = None
    def delChestplate(self):
        self.__chestplate = None
    def delLeggings(self):
        self.__leggings = None
    def delBoots(self):
        self.__boots = None
    def delRing1(self):
        self.__ring1 = None
    def delRing2(self):
        self.__ring2 = None
    def delMainHold(self):
        self.__mainHold = None
    def delSecondHold(self):
        self.__secondHold = None
