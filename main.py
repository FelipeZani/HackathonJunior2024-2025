from classes.alive import alive
from classes.equipment import equipment
from classes.building import building
from classes.shop import shop
from classes.chest import chest
from classes.inventory import hinventory
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

def createStat():
     
    health = int(input("Choose the amount of Health from 1 to 999 999 999: "))
    mana = int(input("Choose the amount of Mana from 1 to 255 :"))
    attack= int(input("Choose the attack from 1 to 255 : "))
    defense = int(input("Choose the defense from 1 to 255 : "))
    element = 0
    racism = int(input("Choose the stat of racism of the Player from 1 to JM Lepen (999 999 999) : "))
    crit = float(input("Choose the probability of crit attack from 0 to 1 : "))
    critModifier = int(input("Choose the multiplier of a crit attack from 1 to 1000 : "))
    assert (0<health<=999_999_999) and (0<mana<=255) and (0<attack<=255) and (0<defense<=255) and (0<racism<=999_999_999 )and (0<=crit<=1) and (0<critModifier<=1000), 'Respect  the min and max amount for each stat'
    s = statistic(health,mana,attack,defense,element,racism,crit,critModifier)
    
    return s

def createBuilding():
    name = input("Choose the name of the building")
    architecture = input("Choose the architecture of the building")
    owner = input("Choose the name of the owner of the building")
    build = building(name,architecture,owner)
    return build

def main():
    s = createStat()
    Ls = [s.getHealth(),s.getMana(),s.getAttack(),s.getDefense(),s.getElement(),s.getRacism(),s.getCrit(),s.getCritModifier()]
    print(Ls)
    return 0

