from classes.alive import alive

class player(alive):
    
    def __init__(self,name,stats,race,hostility,role,skills,inventory,equipment):
        super().__init__(name,stats,race,hostility,role,skills,inventory,equipment)

    