import sys
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

def createRegion():

    regionCoordinateX = input("Choose intenger numbers to be the coordinates of your region, the form is a square of edge x: ") # coordinate to add onto the canvas
        
    try: 
        regionCoordinateX = int(regionCoordinateX)  
    except:
        print("Invalid values, stop program")
        sys.exit(1) #exiting program in case of error 
    
    #add security on the edge's canvas

    topography = input("Choose the topography of your region: 1- forest 2-swamp 3- mountains 4- desert: ")

    try:
        topography = int(topography)
    except:
        print("Invalid value, stop program")
        sys.exit(1) #exiting program in case of error 

    assert 1 <= topography <= 4 , "Value out of range"

    constructionLM = input("Choice of landMark: 1- City 2- Dungeon 3- Tower 4-Keeps 5-Villages: ")
    
    try:
        constructionLM = int(constructionLM)
    except:
        print("Invalid values, stop program")
        sys.exit(1) #exiting program in case of error 

    assert 1 <= constructionLM <= 5 , "Value out of range"


    return region(topography,regionCoordinateX,constructionLM)


def createAliveStat():
     
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
     
def createItemStat():
     
    health = int(input("Choose the Health bonus from 0 to 999 999 999: "))
    mana = int(input("Choose the Mana bonus from 0 to 255 :"))
    attack= int(input("Choose the Attack bonus 0 to 255 : "))
    defense = int(input("Choose the Defense bonus from 0 to 255 : "))
    element = 0
    racism = 0
    crit = float(input("Choose the probability of crit attack bonus from 0 to 1 : "))
    critModifier = int(input("Choose the multiplier of a crit attack bonus from 0 to 1000 : "))
    assert (0<=health<=999_999_999) and (0<=mana<=255) and (0<=attack<=255) and (0<=defense<=255) and (0<=racism<=999_999_999 )and (0<=crit<=1) and (0<=critModifier<=1000), 'Respect  the min and max amount for each stat'
    i = statistic(health,mana,attack,defense,element,racism,crit,critModifier)
    return i 

def statValues(stat):
    return [stat.getHealth(),stat.getMana(),stat.getAttack(),stat.getDefense(),stat.getElement(),stat.getRacism(),stat.getCrit(),stat.getCritModifier()]

def createBuilding():
    name = input("Choose the name of the building")
    architecture = input("Choose the architecture of the building")
    owner = input("Choose the name of the owner of the building")
    build = building(name,architecture,owner)
    return build

def buildingValues(build):
    return [build.getName(),build.getArchitecture(),build.getOwner()]

def createRace():
    name = str(input('Choose the name of the race : '))
    origine = 'EMPTYY'
    reputaion = int(input('Choose the reputation of the race from 1 to 255, (1 means bad reputation, 255 means good reputation): '))
    modif = createStat()
    r = race(name,origine,reputaion,modif)
    return r

def raceValues(race):
    return [race.getName(),race.getOrigine(),race.getReputation(),statValues(race.getModif())]

def createItem():
    name = input("Choose the name of your Item : ")
    weight = input("Choose your Item's weight : ")
    stats = createItemStat()
    
    i= item(name,weight,stats)

    return i

def itemValues(item):
     return [item.getName(),item.getWeight(),statValues(item.getStats())]

def main():
    s = createStat()
    Ls = [s.getHealth(),s.getMana(),s.getAttack(),s.getDefense(),s.getElement(),s.getRacism(),s.getCrit(),s.getCritModifier()]
    print(Ls)
    return 0

