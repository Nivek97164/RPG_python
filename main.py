# V1.5 ALPHA
import os, random, json
from simple_term_menu import *

run = True
menu = True
play = False
about = False
key_dragon = False
fight = False
standing = True
buy = False
speak = False
boss = False

HPplayer = 50
MAXHP = HPplayer
LVL = 0
XPplayer = 0
ATK = 3
pot = 1
elix = 0
GOLD = 0
x = 2
y = 3

        # x = 0    x = 1     x = 2     x = 3     x = 4     x = 5       x = 6
map = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave", "", "", "", ""],     # y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills", "mountain", "", "", "", ""],    # y = 1
       ["forest", "fields", "bridge", "plains", "hills", "forest", "hills", "", "", "", ""],       # y = 2
       ["plains", "shop", "town", "major", "plains", "hills", "mountain", "", "", "", ""],          # y = 3
       ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain", "", "", "", ""]]  # y = 4


y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True,
        "s": "🌱"},
    "forest": {
        "t": "WOODS",
        "e": True,
        "s": "🌳"},
    "fields" : {
        "t": "FIELDS",
        "e": False,
        "s": "🌽"},
    "bridge": {
        "t": "BRIDGE",
        "e": True,
        "s": "🌉"},
    "town" : {
        "t" : "TOWN CENTRE",
        "e" : False,
        "s": "🏙️"},
    "shop" : {
        "t": "SHOP",
        "e": False,
        "s": "🛒"},
    "major" : {
        "t": "MAJOR",
        "e": False,
        "s": "👑"},
    "cave" : {
        "t": "CAVE",
        "e": True,
        "s": "🕳️"},
    "mountain" : {
        "t": "MOUNTAIN",
        "e": True,
        "s": "🏔️"},
    "hills" : {
        "t": "HILLS",
        "e": True,
        "s": "⛰️"},
    "": {
        "t": "VIDE",
        "e": False,
        "s": " "
    }
}   

e_list = ["Goblin", "Orc", "Slime", "Bandit"]

mobs = {
    "Goblin": {
        "hp": 15,
        "atk": 3,
        "gold": 4,
        "XP": 8},
    "Orc": {
        "hp": 35,
        "atk": 5,
        "gold": 7,
        "XP": 13},
    "Slime": {
        "hp": 20,
        "atk": 2,
        "gold": 3,
        "XP": 4},
    "Bandit": {
        "hp": 25,
        "atk": 3,
        "gold": 14,
        "XP": 9,},
    "Dark_Mage": {
        "hp": 75,
        "atk": 7,
        "gold": 5,
        "XP": 50,},
    "Dragon": {
        "hp": 100,
        "atk": 8,
        "gold": 100,
        "XP": 100}
}

current_tile = map[y][x]
#print(current_tile)
name_of_tile = biom[current_tile]["t"]
#print(name_of_tile)
enemy_tile = biom[current_tile]["e"]
#print(enemy_tile)

def clear():
    os.system("clear")

def draw():
    print("xX-------------------------Xx")

def save():
    DATA =  {
            "name": name,
            "HPplayer": HPplayer,
            "XPplayer": XPplayer,
            "LVL": LVL,
            "Pot": pot,
            "elix": elix,
            "GOLD": GOLD,
            "x": x,
            "y": y,
            "key_dragon": key_dragon
        }
    json.dumps(DATA)

    f = open("Saves/load.json", "w")

    f.write(json.dumps(DATA))

def heal(amount):
    global HPplayer
    if HPplayer + amount < MAXHP:
        HPplayer += amount
    else:
        HPplayer = MAXHP
    print(name + "'s HP refilled to " + str(HPplayer) + " !")

def battle():
    global fight, play, run, HPplayer, pot, elix, GOLD, boss, XPplayer, menu

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    maxhp = hp
    atk = mobs[enemy]["atk"]
    gold = mobs[enemy]["gold"]
    XP = mobs[enemy]["XP"]

    while fight:
        clear()
        draw()
        print("defeat the "+ enemy + " !")
        draw()
        print(enemy + "'s HP : "+ str(hp) + "/" + str(maxhp))
        print(name + "'s HP : "+ str(HPplayer) + "/" + str(MAXHP))
        print("POTIONS: "+ str(pot))
        print("ELIXIR: "+ str(elix))
        draw()
        fight_menu = []
        #print("1 - ATTACK")
        fight_menu.append("ATTACK")
        if pot > 0:
            fight_menu.append("USE POTION (30HP)")
            #print("2 - USE POTION (30HP)")
        if elix > 0:
            fight_menu.append("USE ELIXIR (50HP)")
            #print("3 - USE ELIXIR (MAXHP)")
        fight_menu.append("RUN")

        terminal_fight_menu = TerminalMenu(fight_menu)
        fight_entry_index = terminal_fight_menu.show()
        #choice = input("# ")

        if fight_menu[fight_entry_index] == "ATTACK":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HPplayer -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
                 
        elif fight_menu[fight_entry_index] == "USE POTION (30HP)":
            if pot > 0:
                pot -= 1
                heal(30)
                HPplayer -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
            else:
                print("No potions !")
            

        elif fight_menu[fight_entry_index] == "USE ELIXIR (50HP)":
            if elix > 0:
                elix -= 1
                heal(50)
                HPplayer -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
            else:
                print("No elixirs !")
        
        elif fight_menu[fight_entry_index] == "RUN":
            if random.randint(0, 1) < 0.5:
                fight = False
                play = True
                clear()
            else:
                print("Your can't run !")
                HPplayer -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
                clear()
        else: 
            print("Error")
            continue    

        if HPplayer <=0:
            clear()
            draw()
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
            clear()
        
        if hp <= 0:
            print(name + " defeated the " + enemy + " !")
            draw()
            fight = False
            GOLD += gold
            XPplayer += XP
            print("You've found " + str(gold) + " gold !")
            print("You've won " + str(XP) + " XP !")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion !")
            if enemy == "Dragon":
                draw()
                print("Congratulation, you !")
                boss = False
                play = True
            input("> ")
            clear()

def shop():
    global buy, GOLD, pot, elix, ATK

    while buy:
        clear()
        draw()
        print("Welcome to the shop !")
        draw()
        print("GOLD: "+ str(GOLD))
        print("POTIONS: "+ str(pot))
        print("ELIXIRS: "+ str(elix))
        print("ATK: "+ str(ATK))
        draw()
        shop_menu = ["BUY POTION (30HP) - 5 GOLD","BUY ELIXIR (50HP) - 8 GOLD","LEAVE"]


        terminal_shop_menu = TerminalMenu(shop_menu)
        shop_entry_index = terminal_shop_menu.show()
        #choice = input("# ")

        if shop_menu[shop_entry_index] == "BUY POTION (30HP) - 5 GOLD":
            if GOLD >= 5:
                pot +=1
                GOLD -= 5
                print("You've bought a potion !")
            else:
                print("Not enought gold !")
            input("> ")
        if shop_menu[shop_entry_index] == "BUY ELIXIR (50HP) - 8 GOLD":
            if GOLD >= 8:
                elix +=1
                GOLD -= 8
                print("You've bought a elixir !")
            else:
                print("Not enought gold !")
            input("> ")
        if shop_menu[shop_entry_index] == "LEAVE":
            buy = False

def major():
    global speak, key_dragon

    while speak:
        clear()
        draw()
        print("Hello there, " + name + " !")
        if ATK < 10:
            print("You've not strong enought to face the dragon yet ! Keep practicing and come back later !")
        else : 
            print("You might want to take on the dragon now ! Be careful with the beast !")
            key_dragon = True
        
        draw()
        major_menu = ["LEAVE"]
        #print("1 - LEAVE")

        terminal_major_menu = TerminalMenu(major_menu)
        major_entry_index = terminal_major_menu.show()
        #choice = input("#" )

        if major_menu[major_entry_index] == "LEAVE":
            speak = False

def cave():
    global boss, key_dragon, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do ?")
        draw()
        cave_menu = []
        if key_dragon:
            cave_menu.append("FIGHT THE DRAGON")
            #print("1 - USE KEY")
        cave_menu.append("TRUN BACK")
        #print("2 - TRUN BACK")

        terminal_cave_menu = TerminalMenu(cave_menu)
        cave_entry_index = terminal_cave_menu.show()
        #choice = input("# ")

        if cave_menu[cave_entry_index] == "FIGHT THE DRAGON":
            if key_dragon:
                fight = True
                battle()
        if cave_menu[cave_entry_index] == "TRUN BACK":
            boss = False
    
def LVL_UP():   
    global LVL, XPplayer, ATK

    if XPplayer > 15:
        LVL += 1

while run:
    while menu:
        clear()
        draw()
        print("NAME OF THE GAME")
        draw()
        main_menu = ["[1] - NEW GAME", "[2] - LOAD GAME","[3] - ABOUT", "[4] - QUIT GAME"]
        terminal_menu = TerminalMenu(main_menu)
        menu_entry_index = terminal_menu.show()
        if main_menu[menu_entry_index] == "[1] - NEW GAME":
            clear()
            draw()
            print("*** Ajouter une histois ***")
            draw()
            name = input("# So what is your name ? \n> ")
            HPplayer = 50
            MAXHP = HPplayer
            LVL = 0
            XPplayer = 0
            ATK = 3
            pot = 1
            elix = 0
            GOLD = 0
            x = 2
            y = 3
            menu = False
            play = True

        elif main_menu[menu_entry_index] == "[2] - LOAD GAME":
            try:
                with open("Saves/load.json") as f:
                    data = json.load(f)

                    name = data['name']
                    HPplayer = data['HPplayer']
                    XPplayer = data['XPplayer']
                    LVL = data['LVL']
                    Pot = data['Pot']
                    elix = data['elix']
                    GOLD = data['GOLD']
                    x = data['x']
                    y = data['y']
                    key_dragon = data['key_dragon']

                    clear()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
            except OSError:
                print("No loadable save file !")
                input("> ")

        elif main_menu[menu_entry_index] == "[3] - ABOUT":
            about = True

        elif main_menu[menu_entry_index] == "[4] - QUIT GAME":
            clear()
            quit()
        draw()

        if about:
            clear()
            draw()
            print("I'm the creator of this game !")
            draw()
            about = False
            choice = ""
            input("> ")

    while play:
        save() # autosave
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()
        
        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HPplayer) + "/" + str(MAXHP))
            print("ATK: " + str(ATK))
            print("LVL: " + str(LVL))
            print("XP: "+ str(XPplayer))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(GOLD))
            print("COORD: ", x, y)
            for coor_y in range(0, y_len+1):
                str_map = ""
                for coor_x in range(0, x_len+1):
                    if coor_x == x and coor_y == y:
                        str_map += " 😃 "
                    else:
                        str_map += " " + biom[map[coor_y][coor_x]]["s"] + " "
                print(str_map)
            draw()

            action_menu = []
            #print("0 - SAVE AND QUIT")
            if y > 0:
                action_menu.append("NORTH")
                #print("1 - NORTH")
            if x < x_len:
                action_menu.append("EAST")
                #print("2 - EAST")
            if y < y_len:
                action_menu.append("SOUTH")
                #print("3 - SOUTH")
            if x > 0:
                action_menu.append("WEST")
                #print("4 - WEST")
            if pot > 0:
                action_menu.append("USE POTION (30HP)")
                #print("5 - USE POTION (30HP)")
            if elix > 0:
                action_menu.append("USE ELIXIR (50HP)")
                #print("6 - USE ELIXIR (50HP)")
            if map[y][x] == "shop" or map[y][x] == "major" or map[y][x] == "cave":
                action_menu.append("ENTER")
               #print("7 - ENTER")
            action_menu.append("SAVE AND QUIT")



            terminal_action_menu = TerminalMenu(action_menu)
            action_entry_index = terminal_action_menu.show()
            #if main_menu[menu_entry_index] == "[1] - NEW GAME":
        
            #dest = input("# ")

            if action_menu[action_entry_index] == "SAVE AND QUIT":
                play = False
                menu = True
                save()

            elif action_menu[action_entry_index] == "NORTH":
                if y > 0:
                    y -= 1
                    standing = False

            elif action_menu[action_entry_index] == "EAST":
                if x < x_len:
                    x += 1
                    standing = False

            elif action_menu[action_entry_index] == "SOUTH":
                if y < y_len:
                    y += 1
                    standing = False
            
            elif action_menu[action_entry_index] == "WEST":
                if x > 0:
                    x -= 1
                    standing = False
            
            elif action_menu[action_entry_index] == "USE POTION (30HP)":
                if pot > 0:
                    pot -= 1
                    heal(30)
                    input("> ")
                else:
                    print("No potions !")
                standing = True

            elif action_menu[action_entry_index] == "USE ELIXIR (50HP)":
                if elix > 0:
                    elix -= 1
                    heal(50)
                    input("> ")
                else:
                    print("No elixirs !")
                standing = True

            elif action_menu[action_entry_index] == "ENTER":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "major":
                    speak = True
                    major()
                if map[y][x] == "cave":
                    boss = True
                    cave()
            else:
                standing = True