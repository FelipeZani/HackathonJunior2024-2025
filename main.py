from classes.alive import alive
from classes.equipment import equipment
from classes.building import building
from classes.shop import shop
from classes.chest import chest
from classes.inventory import Inventory
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
    health = input("Choose the amount of Health from 1 to 999 999 999: ")
    mana = input("Choose the amount of Mana from 1 to 255 :")
    attack= input("Choose the attack from 1 to 255 : ")
    defense = input("Choose the defense from 1 to 255 : ")
    element = 0
    racism = input("Choose the stat of racism of the Player from 1 to JM Lepen (999 999 999) : ")
    crit = input("Choose the probability of crit attack from 0 to 1 : ")
    critModifier = input("Choose the multiplier of a crit attack from 1 to 1000 : ")
    s = statistic(health,mana,attack,defense,element,racism,crit,critModifier)
    return s

def main():
    s = createStat()
    Ls = [s.getHealth(),s.getMana(),s.getAttack(),s.getDefense(),s.getElement(),s.getRacism(),s.getCrit(),s.getCritModifier]
    return 0

