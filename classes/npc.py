from alive import Alive

class creature(Alive):
    
    def __init__(self,name,stats,race,hostility,role,skills,inventory,equipment):
        super.__init__(name,stats,race,hostility,role,skills,inventory,equipment)