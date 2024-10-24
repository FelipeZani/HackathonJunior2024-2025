from classes.alive import alive
from classes.equipment import equipment
from classes.building import building
from classes.shop import shop
from classes.chest import chest
from classes.inventory import inventory
from classes.hstatistic import statistic
from classes.race import race
from classes.role import role 
from classes.item import item
from classes.player import player
from classes.skills import skills
from classes.npc import npc
from classes.region import region
from classes.creature import creature
from classes.consumable import consumable


 

def main():
    print("Bienvenue dans la creation de votre RPG !!!")
    newObject = race('raciste','France','gros porc',None)
    
    print(newObject.getName())
    return 0

