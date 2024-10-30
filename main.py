from functions import *
from saveLoadData import *
import shutil

def main():
    ListRaces = []
    ListPlayer = []
    ListNPC = []
    ListCreature = []
    ListItem = []
    ListSkills = []
    ListRoles = []
    ListBuilding = []
    
    print("_"*shutil.get_terminal_size().columns)
    print("_"*shutil.get_terminal_size().columns)
    print("\033[1;32m   WELCOME IN HACKATHON RPG MAKER !".center(shutil.get_terminal_size().columns))
    print("You will be able to create your RPG\033[0m".center(shutil.get_terminal_size().columns))
    print("_"*shutil.get_terminal_size().columns)
    print("_"*shutil.get_terminal_size().columns)
    print("\n"*3)
    running = 0
    while running == 0:
        print("_"*shutil.get_terminal_size().columns)
        print("_"*shutil.get_terminal_size().columns)
        print("\033[1;32mWhat do you want to do ?")
        print("0 : stop       ".center(shutil.get_terminal_size().columns))
        print("1 : Race       ".center(shutil.get_terminal_size().columns))
        print("2 : Player     ".center(shutil.get_terminal_size().columns))
        print("3 : Skills     ".center(shutil.get_terminal_size().columns))
        print("4 : Items      ".center(shutil.get_terminal_size().columns))
        print("5 : Building   ".center(shutil.get_terminal_size().columns))
        print("6 : Role       ".center(shutil.get_terminal_size().columns))
        print("\033[0m_"*shutil.get_terminal_size().columns)
        print("_"*shutil.get_terminal_size().columns)
        ask = input("\033[0;36m>>> \033[0m")
        if ask == "0":
            running = 1
        elif ask == "1":
            loop = 0
            while loop == 0:
                
                print("_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                print("\033[1;32mWhat do you want to do ?")
                print("10 : back       ".center(shutil.get_terminal_size().columns))
                print("11 : Create Race".center(shutil.get_terminal_size().columns))
                print("12 : View Races ".center(shutil.get_terminal_size().columns))
                print("\033[0m_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                ask = input("\033[0;36m>>> \033[0m")
                if ask == "10":
                    loop = 1
                elif ask == "11":
                    r = createRace()
                    print("-------------------------")
                    print(str(r))
                    ListRaces.append(r)
                elif ask == "12":
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    print("This is all your races :")
                    print("Race : ")
                    if len(ListRaces)==0:
                        print("")
                    else :
                        for j in range(len(ListRaces)):
                            print("-------------------------")
                            print(f"{j+1}) ")
                            print(str(ListRaces[j]))
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    input("Click entry to continue")
                    print("\n"*100)
        
        elif ask == "2":
            loop=0
            while loop ==0:
                
                print("_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                print("\033[1;32mWhat do you want to do ?".center(shutil.get_terminal_size().columns))
                print("20 : back    ".center(shutil.get_terminal_size().columns))
                print("21 : Player  ".center(shutil.get_terminal_size().columns))
                print("22 : NPC     ".center(shutil.get_terminal_size().columns))
                print("23 : Creature".center(shutil.get_terminal_size().columns))
                print("\033[0m_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                ask = input("\033[0;36m>>> \033[0m")
                if ask == "20":
                    loop = 1
                elif ask == "21":
                    loop1 = 0
                    while loop1 == 0:
                        if ListRoles == [] or ListRaces == []:
                            print("\033[0;31mYou need to create Role and Race before, to had them to your player\033[0m")
                            loop1 = 1
                            
                        print("_"*shutil.get_terminal_size().columns)
                        print("_"*shutil.get_terminal_size().columns)
                        print("\033[1;32mWhat do you want to do ?")
                        print("210 : back         ".center(shutil.get_terminal_size().columns))
                        print("211 : Create Player".center(shutil.get_terminal_size().columns))
                        print("212 : View Players ".center(shutil.get_terminal_size().columns))
                        print("\033[0m_"*shutil.get_terminal_size().columns)
                        print("_"*shutil.get_terminal_size().columns)
                        ask = input("\033[0;36m>>> \033[0m")
                        if ask =="210":
                            loop1 = 1
                        elif ask =="211":
                            p = createPlayer(ListRaces,ListRoles,ListSkills)
                            print("-------------------------")
                            print(str(p))
                            ListPlayer.append(p)
                        elif ask == "212":
                            print("_"*shutil.get_terminal_size().columns)
                            print("_"*shutil.get_terminal_size().columns)
                            print("This is all your Players :")
                            print("Player List : ")
                            if len(ListPlayer)==0:
                                print("")
                            else :
                                for j in range(len(ListPlayer)):
                                    print("-------------------------")
                                    print(f"{j+1}) ")
                                    print(ListPlayer[j])
                            print("_"*shutil.get_terminal_size().columns)
                            print("_"*shutil.get_terminal_size().columns)
                            input("Click entry to continue")
                            print("\n"*100)
                        

                elif ask == "22":
                    loop2 = 0
                    while loop2 == 0:
                        if ListRoles == [] or ListRaces == []:
                            print("\033[0;31mYou need to create Role and Race before, to had them to your NPCs\033[0m")
                            loop2 = 1
                            
                        print("_"*shutil.get_terminal_size().columns)
                        print("_"*shutil.get_terminal_size().columns)
                        print("\033[1;32mWhat do you want to do ?")
                        print("220 : back      ".center(shutil.get_terminal_size().columns))
                        print("221 : Create NPC".center(shutil.get_terminal_size().columns))
                        print("222 : View NPCs ".center(shutil.get_terminal_size().columns))
                        print("\033[0m_"*shutil.get_terminal_size().columns)
                        print("_"*shutil.get_terminal_size().columns)
                        ask = input("\033[0;36m>>> \033[0m")
                        if ask =="220":
                            loop2 = 1
                        elif ask =="221":
                            npc = createNPC()
                            print(str(npc))
                            ListNPC.append(npc)
                        elif ask == "222":
                            print("_"*shutil.get_terminal_size().columns)
                            print("_"*shutil.get_terminal_size().columns)
                            print("This is all your NPCs :")
                            print("NPCs List : ")
                            if len(ListNPC)==0:
                                print("")
                            else :
                                for j in range(len(ListNPC)):
                                    print(f"{j+1}) ")
                                    print(ListNPC[j])
                            print("_"*shutil.get_terminal_size().columns)
                            print("_"*shutil.get_terminal_size().columns)
                            input("Click entry to continue")
                            print("\n"*100)
                            
                elif ask == "23":
                    loop3 = 0
                    while loop3 == 0:
                        if ListRoles == [] or ListRaces == []:
                            print("\033[0;31mYou need to create Role and Race before, to had them to your Creatures\033[0m")
                            loop3 = 1
                            
                        print("_"*shutil.get_terminal_size().columns)
                        print("_"*shutil.get_terminal_size().columns)
                        print("\033[1;32mWhat do you want to do ?")
                        print("230 : back           ".center(shutil.get_terminal_size().columns))
                        print("231 : Create Creature".center(shutil.get_terminal_size().columns))
                        print("232 : View Creatures ".center(shutil.get_terminal_size().columns))
                        print("_"*shutil.get_terminal_size().columns)
                        print("_"*shutil.get_terminal_size().columns)
                        ask = input("\033[0;36m>>> \033[0m")
                        if ask =="230":
                            loop3 = 1
                        elif ask =="231":
                            cre = createCreature()
                            print(str(cre))
                            ListCreature.append(cre)
                        elif ask == "232":
                            print("_"*shutil.get_terminal_size().columns)
                            print("_"*shutil.get_terminal_size().columns)
                            print("This is all your NPCs :")
                            print("NPCs List : ")
                            if len(ListCreature)==0:
                                print("")
                            else :
                                for j in range(len(ListCreature)):
                                    print(f"{j+1}) ")
                                    print(ListCreature[j])
                            print("_"*shutil.get_terminal_size().columns)
                            print("_"*shutil.get_terminal_size().columns)
                            input("Click entry to continue")
                            print("\n"*100)
        elif ask == "3":
            loop = 0
            while loop == 0:
                
                print("_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                print("\033[1;32mWhat do you want to do ?")
                print("30 : back           ".center(shutil.get_terminal_size().columns))
                print("31 : Create Skills  ".center(shutil.get_terminal_size().columns))
                print("32 : View all Skills".center(shutil.get_terminal_size().columns))
                print("\033[0m_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                ask = input("\033[0;36m>>> \033[0m")
                if ask == "30":
                    loop = 1
                elif ask == "31":
                    s = createskills()
                    print(str(s))
                    ListRaces.append(s)
                elif ask == "32":
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    print("This is all your Skills :")
                    print("Skills List : ")
                    if len(ListSkills)==0:
                        print("")
                    else :
                        for j in range(len(ListSkills)):
                            print(f"{j+1}) ")
                            print(ListSkills[j])
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    input("Click entry to continue")
                    print("\n"*100)
        elif ask == "4":
            loop = 0
            while loop == 0:
                
                print("_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                print("\033[1;32mWhat do you want to do ?")
                print("40 : back          ".center(shutil.get_terminal_size().columns))
                print("41 : Create Item   ".center(shutil.get_terminal_size().columns))
                print("42 : View All Items".center(shutil.get_terminal_size().columns))
                print("\033[0m_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                ask = input("\033[0;36m>>> \033[0m")
                if ask == "40":
                    loop = 1
                elif ask == "41":
                    i = createItem()
                    print(str(i))
                    ListItem.append(i)
                elif ask == "42":
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    
                    print("\033[0;31mHelmets : \033[0m")
                    for u in range(len(triItem(ListItem)[0])):
                        print(triItem(ListItem)[0][u])
                        print("-------------------------")
                    print()
                    print("\033[0;31mChestplates : \033[0m")
                    for u in range(len(triItem(ListItem)[1])):
                        print(triItem(ListItem)[1][u])
                        print("-------------------------")
                    print()
                    print("\033[0;31mLeggings : \033[0m")
                    for u in range(len(triItem(ListItem)[2])):
                        print(triItem(ListItem)[2][u])
                        print("-------------------------")
                    print()
                    print("\033[0;31mBoots : \033[0m")
                    for u in range(len(triItem(ListItem)[3])):
                        print(triItem(ListItem)[3][u])
                        print("-------------------------")
                    print()
                    print("\033[0;31mRings : \033[0m")
                    for u in range(len(triItem(ListItem)[4])):
                        print(triItem(ListItem)[4][u])
                        print("-------------------------")
                    print()
                    print("\033[0;31mWeapons : \033[0m")
                    for u in range(len(triItem(ListItem)[5])):
                        print(triItem(ListItem)[5][u])
                        print("-------------------------")
                    print()
                    print("\033[0;31mUnclassed : \033[0m")
                    for u in range(len(triItem(ListItem)[6])):
                        print(triItem(ListItem)[6][u])
                        print("-------------------------")
                    print()
                    print(triItem(ListItem))
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    input("Click entry to continue")
                    print("\n"*100)

        elif ask == "5":
            loop = 0
            while loop == 0:
                
                print("_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                print("\033[1;32mWhat do you want to do ?")
                print("50 : back             ".center(shutil.get_terminal_size().columns))
                print("51 : Create Building  ".center(shutil.get_terminal_size().columns))
                print("52 : View All Building".center(shutil.get_terminal_size().columns))
                print("\033[0m_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                ask = input("\033[0;36m>>> \033[0m")
                if ask == "50":
                    loop = 1
                elif ask == "51":
                    b = createBuilding()
                    print(str(b))
                    ListBuilding.append(b)
                elif ask == "52":
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    print("This is the all the building created :")
                    print("Buildings list : ")
                    if len(ListBuilding)==0:
                        print("")
                    else :
                        for j in range(len(ListBuilding)):
                            print(ListBuilding[j])
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    input("Click entry to continue")
                    print("\n"*100)
        elif ask == "6":
            loop = 0
            while loop == 0:
                
                print("_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                print("\033[1;32mWhat do you want to do ?")
                print("60 : back          ".center(shutil.get_terminal_size().columns))
                print("61 : Create Role   ".center(shutil.get_terminal_size().columns))
                print("62 : View All Roles".center(shutil.get_terminal_size().columns))
                print("\033[0m_"*shutil.get_terminal_size().columns)
                print("_"*shutil.get_terminal_size().columns)
                ask = input("\033[0;36m>>> \033[0m")
                if ask == "60":
                    loop = 1
                elif ask == "61":
                    ro = createRole()
                    print(str(ro))
                    ListRoles.append(ro)
                elif ask == "62":
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    print("This is the roles :")
                    print("Roles : ")
                    if len(ListRoles)==0:
                        print("")
                    else :
                        for j in range(len(ListRoles)):
                            print("-------------------------")
                            print(f"{j+1}) ")
                            print(ListRoles[j])
                    print("_"*shutil.get_terminal_size().columns)
                    print("_"*shutil.get_terminal_size().columns)
                    input("Click entry to continue")
                    print("\n"*100)
    
    
    return 0

main()
