from building import building

class shop(building):
    __shopName = None
    __shopInventory = None
    def __init__(self,chesName,chestInventory):
        self.shopName = shopName
        self.shopInventory = shopInventory
        
    def getShopName(self):
        return self.shopName
    def getShopInventory(self):
        return self.shopInventory
    
    