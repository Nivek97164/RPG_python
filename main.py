# V2 ALPHA
import os, random, json
from simple_term_menu import *

run = True
menu = True
Save_Menu = False
Stock_menu = False
play = False
about = False
key_dragon = False
key_mage = False
fight = False
standing = True
buy = False
speak = False
boss = False
boss2 = False

HPplayer = 50
MAXHP = HPplayer
LVL = 0
XPplayer = 0
LVL_next = [25, 38, 57, 86, 129, 194, 291, 437, 656, 984, 9999]
ATK = 3
pot = 1
elix = 0    
GOLD = 0
x = 2
y = 3

        # x = 0    x = 1     x = 2     x = 3     x = 4     x = 5       x = 6
map = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave", "mountain", "hills", "hills", "mountain"],     # y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills", "mountain", "mountain", "forest", "hills", "mountain"],    # y = 1
       ["forest", "fields", "bridge", "plains", "plains", "forest", "forest", "hills", "mountain", "forest", "forest"],       # y = 2
       ["plains", "shop", "town", "mayor", "plains", "hills", "mountain", "plains", "bridge", "tower", "forest"],          # y = 3
       ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain", "mountain", "forest", "forest", "forest"]]  # y = 4

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "PLAINES",
        "e": True,
        "s": "🌱"},
    "forest": {
        "t": "BOIS",
        "e": True,
        "s": "🌳"},
    "fields" : {
        "t": "CHAMPS",
        "e": False,
        "s": "🌽"},
    "bridge": {
        "t": "PONT",
        "e": True,
        "s": "🌉"},
    "town" : {
        "t" : "CENTRE-VILLE",
        "e" : False,
        "s": "🏰"},
    "shop" : {
        "t": "MAGASIN",
        "e": False,
        "s": "🛒"},
    "mayor" : {
        "t": "MAIRIE",
        "e": False,
        "s": "👑"},
    "cave" : {
        "t": "GROTTE",
        "e": False,
        "s": "🕳️"},
    "mountain" : {
        "t": "MONTAGNE",
        "e": True,
        "s": "🏔️"},
    "hills" : {
        "t": "COLLINES",
        "e": True,
        "s": "⛰️"},
    "": {
        "t": "VIDE",
        "e": False,
        "s": " "},
    "tower" : {
        "t": "TOUR",
        'e': False,
        "s": "🗼"},
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
    "Magusar": {
        "hp": 250,
        "atk": 9,
        "gold": 0,
        "XP": 0,},
    "Alduin": {
        "hp": 150,
        "atk": 8,
        "gold": 120,
        "XP": 250}
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

def draw2():
    print("xX-------------------------------------Xx")

def draw3():
    print("xX------------------------------------------------------------------Xx")

def save():
    DATA =  {
            "name": name,
            "HPplayer": HPplayer,
            "MAXHP": MAXHP,
            "XPplayer": XPplayer,
            "LVL": LVL,
            "LVL_next": LVL_next,
            "ATK": ATK,
            "pot": pot,
            "elix": elix,
            "GOLD": GOLD,
            "x": x,
            "y": y,
            "key_dragon": key_dragon,
            "key_mage": key_mage
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
    print(name + "HP rechargé à " + str(HPplayer) + " HP !")

def battle():
    global fight, play, run, HPplayer, pot, elix, GOLD, boss, boss2, XPplayer, menu, key_mage

    if not boss and not boss2:
        enemy = random.choice(e_list)
    elif boss:
        enemy = "Alduin"
    elif boss2:
        enemy = "Magusar"

    hp = mobs[enemy]["hp"]
    maxhp = hp
    atk = mobs[enemy]["atk"]
    gold = mobs[enemy]["gold"]
    XP = mobs[enemy]["XP"]

    while fight:
        clear()
        draw()
        print("Vaincre "+ enemy + " !")
        draw()
        print(enemy + "'s HP : "+ str(hp) + "/" + str(maxhp))
        print(name + "'s HP : "+ str(HPplayer) + "/" + str(MAXHP))
        print("LVL: "+ str(LVL))
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
            print(name + " fait " + str(ATK) + " de dégâts à " + enemy + ".")
            if hp > 0:
                HPplayer -= atk
                print(enemy + " fait " + str(atk) + " de dégâts à " + name + ".")
                input("> ")
                 
        elif fight_menu[fight_entry_index] == "USE POTION (30HP)":
            if pot > 0:
                pot -= 1
                heal(30)
                HPplayer -= atk
                print(enemy + " fait " + str(atk) + " de dégâts à " + name + ".")
                input("> ")
            else:
                print("Vous n'avez plus de potions !")
            

        elif fight_menu[fight_entry_index] == "USE ELIXIR (50HP)":
            if elix > 0:
                elix -= 1
                heal(50)
                HPplayer -= atk
                print(enemy + " fait " + str(atk) + " de dégâts à " + name + ".")
                input("> ")
            else:
                print("Vous n'avez plus d'elixirs !")
        
        elif fight_menu[fight_entry_index] == "RUN":
            if random.randint(0, 1) < 0.5:
                fight = False
                play = True
                clear()
            else:
                print("Vous ne pouvez pas fuire !")
                HPplayer -= atk
                print(enemy + " fait " + str(atk) + " de dégâts à " + name + ".")
                input("> ")
                clear()
        else: 
            print("Error")
            continue    

        if HPplayer <=0:
            clear()
            draw()
            print(enemy + " à vaincue " + name + "...")
            draw()
            fight = False
            boss = False
            play = False
            menu = True
            print("GAME OVER")
            input("> ")
            clear()

        if hp <= 0:
            print(name + " à vaincu " + enemy + " !")
            draw()
            fight = False
            GOLD += gold
            if LVL < 10:
                XPplayer += XP
                print("Vous avez gagné " + str(XP) + " XP !")
            print("Vous avez trouvé " + str(gold) + " or !")
            if random.randint(0, 100) < 20:
                pot += 1
                print("Vous avez trouvé une potion !")
            if random.randint(0, 100) < 5:
                elix += 1
                print("Vous avez trouvé un elixir !")

            if enemy == "Alduin":
                draw()
                print("Vous...vous avez réussi ! *parle dans sa barbe*...il pourrait faire l'affaire....* \nVous regarde avec un air sérieux ce qui est bizarre pour une personne ivre* Bien ! \nJ'ai une dernière chose à vous demandez. *Vous le regarder intriguer* La vrai source est un magicien noir nommer Magusar, \ndepuis longtemps il fait des sacrifices humain pour rajeunir. Mettez fin à ses folies et je vous donnerais tout mon vin !\n*Vous acceptez la quête mais pas le vin pour des raisons évidante...* Il est situer au sud-est dans une grande tour.")
                boss = False
                key_mage = True
                play = True
            input("> ")
            clear()

            if enemy == "Magusar":
                draw()
                print("Mais qui êtes vous ? Co..Comment avez vous fait ? \nJe vous suis éternellment reconnaissant...*titube de droite à gauche* Vous êtes le plus grand de tout les hérooooooooos..... \n*Tombe au sol ivre mort, vous soupirez et parter de la tour à la conquête d'une nouvelle aventure*")
                boss2 = False
                play = False
                menu = True
                input("> ")
                clear()

def shop():
    global buy, GOLD, pot, elix

    while buy:
        clear()
        draw()
        print("         MARCHAND : ")
        draw()
        print("-J'ai des choses rare à vendre étranger. \n-Vous voulez regardé ? J'ai des tas de choses à offrir .")
        draw3()
        print("GOLD: "+ str(GOLD))
        print("POTIONS: "+ str(pot))
        print("ELIXIRS: "+ str(elix))
        draw()
        shop_menu = ["BUY POTION (30HP) - 5 GOLD","BUY ELIXIR (50HP) - 8 GOLD","LEAVE"]


        terminal_shop_menu = TerminalMenu(shop_menu)
        shop_entry_index = terminal_shop_menu.show()
        #choice = input("# ")

        if shop_menu[shop_entry_index] == "BUY POTION (30HP) - 5 GOLD":
            if GOLD >= 5:
                pot +=1
                GOLD -= 5
                print("Vous avez acheté une potion !")
            else:
                print("Vous n'avez pas assez d'or !")
            input("> ")
        if shop_menu[shop_entry_index] == "BUY ELIXIR (50HP) - 8 GOLD":
            if GOLD >= 8:
                elix +=1
                GOLD -= 8
                print("Vous avez acheté un élixir !")
            else:
                print("Vous n'avez pas assez d'or !")
            input("> ")
        if shop_menu[shop_entry_index] == "LEAVE":
            buy = False

def mayor():
    global speak, key_dragon

    while speak:
        clear()
        draw()
        print("         MAIRE :")
        draw()
        if LVL < 3:
            print("Malheureusement "+ name +", vous m'avez l'air un peu faiblard....")
            print("Revenez avec plus de puissance pour rivaliser avec lui.")
        else : 
            print("Vous avez gagné en muscle non ? \n*Vous regarde avec un air douteux* On dirait moi dans ma jeunesse haha ! \nJe pense que vous avez la puissance pour le détruire. Voici la clé ouvrant la grotte. \n*Il vous tend une clé en forme de losange qui malgré son joyaux aux couleur du soleil, \ndégage une odeur d'alcool vous prend au nez. \nVous rangez donc rapidement la clé avant de vous mettre à vomir.*")
            key_dragon = True
        
        draw3()
        mayor_menu = ["LEAVE"]
        #print("1 - LEAVE")

        terminal_mayor_menu = TerminalMenu(mayor_menu)
        mayor_entry_index = terminal_mayor_menu.show()
        #choice = input("#" )

        if mayor_menu[mayor_entry_index] == "LEAVE":
            speak = False

def cave():
    global boss, key_dragon, fight

    while boss:
        clear()
        draw()
        print("BOSS INTERMEDIRAIRE :")
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

def tower():
    global boss2, key_mage, fight

    while boss2:
        clear()
        draw()
        print("BOSS FINAL :")
        draw()
        tower_menu = []
        if key_mage:
            tower_menu.append("FIGHT THE MAGE")
            #print("1 - USE KEY")
        tower_menu.append("TRUN BACK")
        #print("2 - TRUN BACK")

        terminal_tower_menu = TerminalMenu(tower_menu)
        tower_entry_index = terminal_tower_menu.show()
        #choice = input("# ")

        if tower_menu[tower_entry_index] == "FIGHT THE MAGE":
            if key_mage:
                fight = True
                battle()
        if tower_menu[tower_entry_index] == "TRUN BACK":
            boss2 = False

while run:
    while menu:
        clear()
        draw()
        print("     THE DRUNK QUEST")
        draw()
        main_menu = ["[1] - NEW GAME", "[2] - LOAD GAME","[3] - ABOUT", "[4] - QUIT GAME"]
        terminal_menu = TerminalMenu(main_menu)
        menu_entry_index = terminal_menu.show()
        if main_menu[menu_entry_index] == "[1] - NEW GAME":
            clear()
            draw()
            print("         HISTOIRE :")
            draw()
            print("Vous êtes un pelerin cherchant l'aventure et le danger. \nPendant vôtre voyage vous entendez parlé d'une ville du nom d'Unlucky \ndemandant de l'aide à quiconque voulant gloire et argent. \nVous vous dirigez donc vers la ville quelque peut étrange avec un maire \ntrès légèrment alcoliser. \nLes habitants vous regarde très peu comme si vous n'existiez pas. \nUne fois que vous avez parlez au maire il vous demande d'une voix quelque \npeu tremblante et sentent le vin de basse qualité :")
            draw3()
            name = input("# Alors ? Qu'elle est votre nom héros ? *inch* \n> ")
            HPplayer = 50
            MAXHP = HPplayer
            LVL = 0
            XPplayer = 0
            LVL_next = [25, 38, 57, 86, 129, 194, 291, 437, 656, 984, 9999]
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
                    MAXHP = data['MAXHP']
                    XPplayer = data['XPplayer']
                    LVL_next = data['LVL_next']
                    ATK = data['ATK']
                    LVL = data['LVL']
                    pot = data['pot']
                    elix = data['elix']
                    GOLD = data['GOLD']
                    x = data['x']
                    y = data['y']
                    key_dragon = data['key_dragon']
                    key_mage = data['key_mage']

                    clear()
                    print("Bon retour, " + name + " !")
                    input("> ")
                    menu = False
                    play = True
            except OSError:
                print("Aucun fichier de sauvegarde chargeable !")
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
            print("Ce jeu est un RPG en tour par tour, \nen mode textuel, programmé par : \nKevin \nAlexendre \nRubbens")
            draw()
            about = False
            choice = ""
            input("> ")

    while play:
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()

        if LVL < len(LVL_next) and XPplayer - LVL_next[LVL] >= 0:
            XPplayer = XPplayer - LVL_next[LVL]
            LVL += 1
            if LVL == 1:
                ATK = ATK + 2
            elif LVL == 2:
                ATK = ATK + 1
                MAXHP = MAXHP + 6
            elif LVL == 3:
                ATK = ATK + 4
                MAXHP = MAXHP + 4
            elif LVL == 4:
                ATK = ATK + 6
                MAXHP = MAXHP + 1
            elif LVL == 5:
                ATK = ATK + 1
                MAXHP = MAXHP + 1
            elif LVL == 6:
                ATK = ATK + 1
                MAXHP = MAXHP + 7
            elif LVL == 7:
                ATK = ATK + 3
                MAXHP = MAXHP + 10
            elif LVL == 8:
                ATK = ATK + 1
                MAXHP = MAXHP + 1
            elif LVL == 9:
                ATK = ATK + 1
                MAXHP = MAXHP + 2
            elif LVL == 10:
                ATK = ATK + 5
                MAXHP = MAXHP + 3

        if play:
            draw()
            print("LOCATION: " + biom[map[y][x]]["t"])
            draw()
            print("NAME: " + name)
            print("HP: " + str(HPplayer) + "/" + str(MAXHP))
            print("ATK: " + str(ATK))
            print("LVL: " + str(LVL))
            if LVL < 10:
                print("XP: "+ str(XPplayer))
                print("NEXT LVL: " + str(LVL_next[LVL]))
            print("COORD: ", x, y)
            draw2()
            for coor_y in range(0, y_len+1):
                str_map = ""
                for coor_x in range(0, x_len+1):
                    if coor_x == x and coor_y == y:
                        str_map += " 😃 "
                    else:
                        str_map += " " + biom[map[coor_y][coor_x]]["s"] + " "
                print(str_map)
            draw2()

            action_menu = []

            if y > 0:
                action_menu.append("NORTH")

            if x < x_len:
                action_menu.append("EAST")

            if y < y_len:
                action_menu.append("SOUTH")

            if x > 0:
                action_menu.append("WEST")

            action_menu.append("INVENTORY")

            if map[y][x] == "shop" or map[y][x] == "mayor" or map[y][x] == "cave" or map[y][x] == "tower":
                action_menu.append("ENTER")

            action_menu.append("SAVE")



            terminal_action_menu = TerminalMenu(action_menu)
            action_entry_index = terminal_action_menu.show()

            if action_menu[action_entry_index] == "SAVE":
                play = False
                Save_Menu = True

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
            
            elif action_menu[action_entry_index] == "INVENTORY":
                play = False
                Stock_menu = True
            
            

            elif action_menu[action_entry_index] == "ENTER":
                if map[y][x] == "shop":
                    buy = True
                    shop()
                if map[y][x] == "mayor":
                    speak = True
                    mayor()
                if map[y][x] == "cave":
                    boss = True
                    cave()
                if map[y][x] == "tower":
                    boss2 = True
                    tower()
            else:
                standing = True

    while Save_Menu:
        clear()
        draw()
        print("LOCATION: " + biom[map[y][x]]["t"])
        draw()
        print("NAME: " + name)
        print("HP: " + str(HPplayer) + "/" + str(MAXHP))
        print("ATK: " + str(ATK))
        print("LVL: " + str(LVL))
        if LVL < 10:
            print("XP: "+ str(XPplayer))
            print("NEXT LVL: " + str(LVL_next[LVL]))
        print("GOLD: " + str(GOLD))
        print("COORD: ", x, y)
        draw()
        print("Dans l'inventaire : ")
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        draw2()
        for coor_y in range(0, y_len+1):
                str_map = ""
                for coor_x in range(0, x_len+1):
                    if coor_x == x and coor_y == y:
                        str_map += " 😃 "
                    else:
                        str_map += " " + biom[map[coor_y][coor_x]]["s"] + " "
                print(str_map)
        draw2()

        Save_Menu = ["SAVE AND CONTINUE", "SAVE AND QUIT"]

        terminal_Save_menu = TerminalMenu(Save_Menu)
        Save_entry_index = terminal_Save_menu.show()

        if Save_Menu[Save_entry_index] == "SAVE AND CONTINUE":
            print("Partie sauvegarder avec succès !")
            input("> ")
            save()
            play = True
            Save_Menu = False

        elif Save_Menu[Save_entry_index] == "SAVE AND QUIT":
            print("Partie sauvegarder avec succès !\nA la prochaine " + name + " !")
            input("> ")
            save()
            Save_Menu = False
            menu = True

    while Stock_menu:
        clear()
        draw()
        print("INVENTAIRE : " + name)
        draw()
        print("HP: " + str(HPplayer) + "/" + str(MAXHP))
        print("GOLD: " + str(GOLD))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        draw()
        

        Stock_menu = []

        if pot > 0:
            Stock_menu.append("USE POTION (30HP)")

        if elix > 0:
            Stock_menu.append("USE ELIXIR (50HP)")

        Stock_menu.append("QUIT INVENTORY")

        terminal_Stock_menu = TerminalMenu(Stock_menu)
        Stock_entry_index = terminal_Stock_menu.show()

        if Stock_menu[Stock_entry_index] == "QUIT INVENTORY":
            play = True
            Stock_menu = False

        elif Stock_menu[Stock_entry_index] == "USE POTION (30HP)":
            if pot > 0:
                pot -= 1
                heal(30)
                input("> ")
            else:
                print("No potions !")
            standing = True

        elif Stock_menu[Stock_entry_index] == "USE ELIXIR (50HP)":
            if elix > 0:
                elix -= 1
                heal(50)
                input("> ")
            else:
                print("No elixirs !")
            standing = True