import json
from functions import *

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
from classes.helmet import helmet
from classes.chestplate import chestplate
from classes.leggings import leggings
from classes.boots import boots
from classes.ring import ring
from classes.weapon import weapon





def saveData(listData): 
    for data in listData:
     print(type(data))
     with open("./saves/"+data.getName(), "w") as final:
         
        json.dump(objToDic(data), final)


def objToDic(data):
    newDict = data.__dict__
    for key in newDict:
       try:
        newDict[key] = objToDic(newDict[key])
       except:
            pass
    return newDict
           
