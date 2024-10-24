from alive import alive
from equipment import equipment
from building import building
from shop import shop
from chest import chest
from inventory import Inventory
from hstatistic import statistic
from race import race
from role import role 
from item import item
from player import player
from skills import skills
from npc import npc
from region import region
from creature import creature
from consumable import consumable


 

def main():
    print("Bienvenue dans la creation de votre RPG !!!")
    newObject = race('raciste','France','gros porc',None)
    
    print(newObject.getName())
    return 0

