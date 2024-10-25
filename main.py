from functions import *

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
        print("0 : stop\n1 : Race\n2 : Player\n3 : Skills\n4 : Items\n5 : Building\n6 : Role")
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
                    print(str(r))
                    ListRaces.append(r)
                elif ask == "12":
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    print("This is all your races :")
                    print("Race : ")
                    if len(ListRaces)==0:
                        print("")
                    else :
                        for j in range(len(ListRaces)):
                            print("-------------------------")
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
                            print(str(p))
                            ListPlayer.append(p)
                        elif ask == "212":
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            print("This is all your Players :")
                            print("Player List : ")
                            if len(ListPlayer)==0:
                                print("")
                            else :
                                for j in range(len(ListPlayer)):
                                    print("-------------------------")
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
                            npc = createNPC(ListRaces,ListRoles,ListSkills)
                            print(str(npc))
                            ListNPC.append(npc)
                        elif ask == "222":
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            print("This is all your NPCs :")
                            print("NPCs List : ")
                            if len(ListNPC)==0:
                                print("")
                            else :
                                for j in range(len(ListNPC)):
                                    print("-------------------------")
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
                            cre = createCreature(ListRaces,ListRoles,ListSkills)
                            print(str(cre))
                            ListCreature.append(cre)
                        elif ask == "232":
                            print("________________________________________________________________________________________________")
                            print("________________________________________________________________________________________________")
                            print("This is all your creatures :")
                            print("creatures List : ")
                            if len(ListCreature)==0:
                                print("")
                            else :
                                for j in range(len(ListCreature)):
                                    print("-------------------------")
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
                    print(str(s))
                    ListRaces.append(s)
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
                    print(str(i))
                    ListItem.append(i)
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
                    print(str(b))
                    ListBuilding.append(b)
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
                    print(str(ro))
                    ListRoles.append(ro)
                elif ask == "62":
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    print("This is the roles :")
                    print("Roles : ")
                    if len(ListRoles)==0:
                        print("")
                    else :
                        for j in range(len(ListRoles)):
                            print("-------------------------")
                            print(ListRoles[j])
                    print("________________________________________________________________________________________________")
                    print("________________________________________________________________________________________________")
                    input("Click entry to continue")
                    print("\n"*100)
    
    
    return 0
main()