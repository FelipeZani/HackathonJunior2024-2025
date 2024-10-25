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
from classes.helmet import helmet
from classes.chestplate import chestplate
from classes.leggings import leggings
from classes.boots import boots
from classes.ring import ring
from classes.weapon import weapon


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
    assert (0<=health<=999_999_999) and (0<=mana<=255) and (0<=attack<=255) and (0<=defense<=255) and (0<=racism<=999_999_999 )and (0<=crit<=1) and (0<=critModifier<=1000), 'Respect  the min and max amount for each stat'
    s = statistic(health,mana,attack,defense,element,racism,crit,critModifier)
    
    return s
     
def createItemStat(itemClass):
    if itemClass == "Null":
        health = 0
        mana = 0
        attack= 0
        defense = 0
        element = 0
        racism = 0
        crit = 0
        critModifier = 0
        i = statistic(health,mana,attack,defense,element,racism,crit,critModifier)
        
    else : 
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
    modif = createAliveStat()
    r = race(name,origine,reputaion,modif)
    return r

def raceValues(race):
    return [race.getName(),race.getOrigine(),race.getReputation(),statValues(race.getModif())]

def createItem():
    name = input("Choose the name of your Item : ")
    itemClass = input("Choose your item CLass : helmet, chetsplate, leggings, boots, ring, weapon, consumable, Null : ")
    weight = float(input("Choose your Item's weight : "))
    stats = createItemStat(itemClass)
    if itemClass == "helmet":
            i= helmet(name,weight,stats)
    elif itemClass == "chestplate":
            i= chestplate(name,weight,stats)
    elif itemClass == "leggings":
            i= leggings(name,weight,stats)
    elif itemClass == "boots":
            i= boots(name,weight,stats)
    elif itemClass == "ring":
            i= ring(name,weight,stats)
    elif itemClass == "weapon":
            i= weapon(name,weight,stats)
    elif itemClass == "consumable":
            i= consumable(name,weight,stats)
    else:
        i=item(name,weight,stats)
    return i

def itemValues(item):
     return [item.getName(),item.getWeight(),statValues(item.getStats())]

def createInventory():
    howMany = 0
    listInventory = []
    maxWeight = input("Choose the max wheight of the inventory : ")
    howMany = int(input("How many items do you  want in your inventory : "))
    for i in range (0,howMany):
         newitem = createItem()
         listInventory.append(newitem)
    invent = hinventory(maxWeight,listInventory)
    return invent

def inventoryValues(inventory):
    return [hinventory.getMaxWeight(),hinventory.getDicObject()]

def createRole():
     name = input("Choose the name of the role : ")
     stats = createAliveStat()
     newRole = role(name,stats)
     return newRole

def roleValues(role):
     return[role.getName(),statValues(role.getStats())]


def createPlayer(listeRace,listeRole,listeSkill):
     name = input("Choose your Player's name : ")
     stats = createAliveStat()
     print(listeRace)
     i=int(input("What race do you want your player to be : "))
     race = listeRace[i-1]
     hostility = 1
     print(listeRole)
     r=int(input("What role do you want your player to be : "))
     role = listeRole[r-1]
     skills=[]
     if listeSkill != []:
          s=int(input("Vous voulez ajoutez des skills au joueurs ? : "))
          while s == 1 and len(skills)<len(listeSkill):
            print(listeSkill)
            i=int(input("What skill do you want to add to your player : "))
            if listeSkill[i-1] not in skills:
                skills.append(listeSkill[i-1]) 
            s=input("Est ce tu veux ajoutez d'autre skill : ")
     inventory = createInventory()
     equipmnt = equipment(None,None,None,None,None,None,None,None)
     player1 = player(name,stats,race,hostility,role,skills,inventory,equipmnt)

     return player1          
def equipmentValues(equipmnt):
    return [equipmnt.getHelmet(),equipmnt.getChestplate(),equipmnt.getLeggings(),equipmnt.getBoots(),equipmnt.getRing1(),equipmnt.getRing2(),equipmnt.getMainHold(),equipmnt.getSecondHold()]

def playerValues(player):
    
    listeSkills = player.getSkills()
    skills=[]
    for i in range(listeSkills):
        skills.append(skillValues(i))
    values=[player.getName(),statValues(player.getStats()),raceValues(player.getRace()),player.getHostility(),roleValues(player.getRole()),skills,inventoryValues(player.inventory),equipmentValues(player.equipment)]
    for i in values:
        print(i)
    return values

def createskills(): #creating skill
    name = input("name your skill")
    level = 1
    description = input("Choose the description of your skill")
    delay = int(input("Choose the delay of action of your skill"))
    skill = skills(name,level,description,delay)
    return skill

def skillValues(skill):
    return [skill.getName(),skill.getLevel(),skill.getDescription(),skill.getDelay()]
            
def main():
    ListRaces = []
    ListPlayer = []
    ListNPC = []
    ListCreature = []
    ListItem = []
    ListSkills = []
    ListRoles = []
    ListBuilding = []
    
    print("________________________________________________________________________________________________")
    print("________________________________________________________________________________________________")
    print("WELCOME IN HACKATHON RPG MAKER !")
    print("You will be able to create your RPG")
    print("________________________________________________________________________________________________")
    print("________________________________________________________________________________________________")
    print("\n"*3)
    running = 0
    while running == 0:
        print("________________________________________________________________________________________________")
        print("________________________________________________________________________________________________")
        print("What do you want to do ?")
        print("0 : stop\n1 : Race\n2 : Alive\n3 : Skills\n4 : Items\n5 : Building\n6 : Role")
        print("________________________________________________________________________________________________")
        print("________________________________________________________________________________________________")
        ask = input("")
        if ask == "0":
            running = 1
        elif ask == "1":
            loop = 0
            while loop == 0:
                
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                print("What do you want to do ?")
                print("10 : back\n11 : Create Race\n12 : View Races\n")
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                ask = input("")
                if ask == "10":
                    loop = 1
                elif ask == "11":
                    r = createRace()
                    print(raceValues(r))
                    ListRaces.append(raceValues(r))
                elif ask == "12":
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    print("This is all your races :")
                    print("Race : ")
                    if len(ListRaces)==0:
                        print("")
                    else :
                        for j in range(len(ListRaces)):
                            print(ListRaces[j])
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    input("Click entry to continue")
                    print("\n"*100)
        
        elif ask == "2":
            loop=0
            while loop ==0:
                
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                print("What do you want to do ?")
                print("20 : back\n21 : Player\n22 : NPC\n23 : Creature")
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                ask = input("")
                if ask == "20":
                    loop = 1
                elif ask == "21":
                    loop1 = 0
                    while loop1 == 0:
                        if ListRoles == [] or ListRaces == []:
                            print("You need to create Role and Race before, to had them to your player")
                            loop1 = 1
                            
                        print("________________________________________________________________________________________________")
                        print("________________________________________________________________________________________________")
                        print("What do you want to do ?")
                        print("210 : back\n211 : Create Player\n212 : View Players\n")
                        print("________________________________________________________________________________________________")
                        print("________________________________________________________________________________________________")
                        ask = input("")
                        if ask =="210":
                            loop = 1
                        elif ask =="211":
                            p = createPlayer(ListRaces,ListRoles,ListSkills)
                            print(playerValues(p))
                            ListPlayer.append(playerValues(p))
                        elif ask == "212":
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            print("This is all your Players :")
                            print("Player List : ")
                            if len(ListPlayer)==0:
                                print("")
                            else :
                                for j in range(len(ListPlayer)):
                                    print(ListPlayer[j])
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            input("Click entry to continue")
                            print("\n"*100)
                elif ask == "22":
                    loop2 = 0
                    while loop2 == 0:
                        if ListRoles == [] or ListRaces == []:
                            print("You need to create Role and Race before, to had them to your player")
                            loop2 = 1
                            
                        print("________________________________________________________________________________________________")
                        print("________________________________________________________________________________________________")
                        print("What do you want to do ?")
                        print("220 : back\n221 : Create NPC\n222 : View NPCs\n")
                        print("________________________________________________________________________________________________")
                        print("________________________________________________________________________________________________")
                        ask = input("")
                        if ask =="220":
                            loop2 = 1
                        elif ask =="221":
                            npc = createNPC()
                        elif ask == "222":
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            print("This is all your NPCs :")
                            print("NPCs List : ")
                            if len(ListNPC)==0:
                                print("")
                            else :
                                for j in range(len(ListNPC)):
                                    print(ListNPC[j])
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            input("Click entry to continue")
                            print("\n"*100)
                            
                elif ask == "23":
                    loop3 = 0
                    while loop3 == 0:
                        if ListRoles == [] or ListRaces == []:
                            print("You need to create Role and Race before, to had them to your player")
                            loop3 = 1
                            
                        print("________________________________________________________________________________________________")
                        print("________________________________________________________________________________________________")
                        print("What do you want to do ?")
                        print("230 : back\n231 : Create Creature\n232 : View Creatures\n")
                        print("________________________________________________________________________________________________")
                        print("________________________________________________________________________________________________")
                        ask = input("")
                        if ask =="230":
                            loop3 = 1
                        elif ask =="231":
                            cre = createCreature()
                        elif ask == "232":
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            print("This is all your NPCs :")
                            print("NPCs List : ")
                            if len(ListCreature)==0:
                                print("")
                            else :
                                for j in range(len(ListCreature)):
                                    print(ListCreature[j])
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            input("Click entry to continue")
                            print("\n"*100)
        elif ask == "3":
            loop = 0
            while loop == 0:
                
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                print("What do you want to do ?")
                print("30 : back\n31 : Create Skills\n32 : View all Skills\n")
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                ask = input("")
                if ask == "30":
                    loop = 1
                elif ask == "31":
                    s = createskills()
                    print(skillValues(s))
                    ListRaces.append(skillValues(s))
                elif ask == "32":
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    print("This is all your Skills :")
                    print("Skills List : ")
                    if len(ListSkills)==0:
                        print("")
                    else :
                        for j in range(len(ListSkills)):
                            print(ListSkills[j])
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    input("Click entry to continue")
                    print("\n"*100)
        elif ask == "4":
            loop = 0
            while loop == 0:
                
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                print("What do you want to do ?")
                print("40 : back\n41 : Create Item\n42 : View All Items\n")
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                ask = input("")
                if ask == "40":
                    loop = 1
                elif ask == "41":
                    i = createItem()
                    print(itemValues(i))
                    ListItem.append(itemValues(i))
                elif ask == "42":
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    print("This is all your Items :")
                    print("Items : ")
                    if len(ListItem)==0:
                        print("")
                    else :
                        for j in range(len(ListItem)):
                            print(ListItem[j])
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    input("Click entry to continue")
                    print("\n"*100)
        elif ask == "5":
            loop = 0
            while loop == 0:
                
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                print("What do you want to do ?")
                print("50 : back\n51 : Create Building\n52 : View All Building\n")
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                ask = input("")
                if ask == "50":
                    loop = 1
                elif ask == "51":
                    b = createBuilding()
                    print(roleValues(b))
                elif ask == "52":
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    print("This is the all the building created :")
                    print("Buildings list : ")
                    if len(ListBuilding)==0:
                        print("")
                    else :
                        for j in range(len(ListBuilding)):
                            print(ListBuilding[j])
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    input("Click entry to continue")
                    print("\n"*100)
        elif ask == "6":
            loop = 0
            while loop == 0:
                
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                print("What do you want to do ?")
                print("60 : back\n61 : Create Role\n62 : View All Roles\n")
                print("________________________________________________________________________________________________")
                print("________________________________________________________________________________________________")
                ask = input("")
                if ask == "60":
                    loop = 1
                elif ask == "61":
                    ro = createRole()
                    print(roleValues(ro))
                    ListRoles.append(roleValues(ro))
                elif ask == "62":
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    print("This is the roles :")
                    print("Roles : ")
                    if len(ListRoles)==0:
                        print("")
                    else :
                        for j in range(len(ListRoles)):
                            print(ListRoles[j])
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    input("Click entry to continue")
                    print("\n"*100)
    
    
    return 0
