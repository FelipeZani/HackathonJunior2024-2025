from building import building

class shop(building):
    
    __shopInventory = None
    def __init__(self,name,architecture,owner,shopInventory):
        super.__init__(self, name, architecture)
        self.shopInventory = shopInventory
        
    def getShopInventory(self):
        return self.shopInventory
    
    