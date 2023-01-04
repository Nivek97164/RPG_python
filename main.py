import os, random

run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

HP = 50
MAXHP = HP
ATK = 3
pot = 1
elix = 0
GOLD = 0
x = 0
y = 0 

        # x = 0    x = 1     x = 2     x = 3     x = 4     x = 5       x =6
map = [["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],     # y = 0
       ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],    # y = 1
       ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],       # y = 2
       ["plains", "shop", "town", "major", "plains", "hills", "mountain"],          # y = 4
       ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"]]  # y = 5

y_len = len(map)-1
x_len = len(map[0])-1

biom = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields" : {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIDGE",
        "e": True},
    "town" : {
        "t" : "TOWN CENTRE",
        "e" : False},
    "shop" : {
        "t": "SHOP",
        "e": False},
    "major" : {
        "t": "MAJOR",
        "e": False},
    "cave" : {
        "t": "CAVE",
        "e": True},
    "mountain" : {
        "t": "MOUNTAIN",
        "e": True},
    "hills" : {
        "t": "HILLS",
        "e": True
    }
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {
        "hp": 15,
        "atk": 3,
        "gold": 8},
    "Orc": {
        "hp": 35,
        "atk": 5,
        "gold": 20},
    "Slime": {
        "hp": 20,
        "atk": 2,
        "gold": 12},
    "Dragon": {
        "hp": 100,
        "atk": 8,
        "gold": 100}
}

current_tile = map[y][x]
print(current_tile)
name_of_tile = biom[current_tile]["t"]
print(name_of_tile)
enemy_tile = biom[current_tile]["e"]
print(enemy_tile)

def clear():
    os.system("clear")

def draw():
    print("xX-------------------------Xx")

def save():
    list =[
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(GOLD),
        str(x),
        str(y),
        str(key),
    ]

    f = open("Saves/load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

def heal(amount):
    global HP
    if HP + amount < MAXHP:
        HP += amount
    else:
        HP = MAXHP
    print(name + "'s HP refilled to " + str(HP) + " !")

def battle():
    global fight, play, run, HP, pot, elix, GOLD, boss

    if not boss:
        enemy = random.choice(e_list)
    else:
        enemy = "Dragon"
    hp = mobs[enemy]["hp"]
    maxhp = hp
    atk = mobs[enemy]["atk"]
    gold = mobs[enemy]["gold"]

    while fight:
        clear()
        draw()
        print("defeat the "+ enemy + " !")
        draw()
        print(enemy + "'s HP : "+ str(hp) + "/" + str(maxhp))
        print(name + "'s HP : "+ str(HP) + "/" + str(MAXHP))
        print("POTIONS: "+ str(pot))
        print("ELIXIR: "+ str(elix))
        draw()
        print("1 - ATTACK")
        if pot > 0:
            print("2 - USE POTION (30HP)")
        if elix > 0:
            print("3 - USE ELIXIR (MAXHP)")
        draw()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
                 
        elif choice == "2":
            if pot > 0:
                pot -= 1
                heal(30)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
            else:
                print("No potions !")
            input("> ")

        elif choice == "3":
            if elix > 0:
                elix -= 1
                heal(50)
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
                input("> ")
            else:
                print("No elixirs !")
            input("> ")

        if HP <=0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
        
        if hp <= 0:
            print(name + " defeated the " + enemy + " !")
            draw()
            fight = False
            GOLD += gold
            print("You've found " + str(gold) + " gold !")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion !")
            if enemy == "Dragon":
                draw()
                print("Congratulation, you've finished the game !")
                boss = False
                play = False
                run = False
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
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if GOLD >= 5:
                pot +=1
                GOLD -= 5
                print("You've bought a potion !")
            else:
                print("Not enought gold !")
            input("> ")
        if choice == "2":
            if GOLD >= 8:
                elix +=1
                GOLD -= 8
                print("You've bought a elixir !")
            else:
                print("Not enought gold !")
            input("> ")
        if choice == "3":
            if GOLD >= 10:
                ATK += 2
                GOLD -= 10
                print("You've upgrade your weapon !")
            else:
                print("Not enought gold !")
            input("> ")
        if choice == "4":
            buy = False

def major():
    global speak, key

    while speak:
        clear()
        draw()
        print("Hello there, " + name + " !")
        if ATK < 10:
            print("You've not strong enought to face the dragon yet ! Keep practicing and come back later !")
        else : 
            print("You might want to take on the dragon now ! Take this key but be careful with the beast !")
            key = True
        
        draw()
        print("1 - LEAVE")
        draw()

        choice = input("#" )

        if choice == "1":
            speak = False

def cave():
    global boss, key, fight

    while boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do ?")
        draw()
        if key:
            print("1 - USE KEY")
        print("2 - TRUN BACK")
        draw()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        if choice == "2":
            boss = False

while run:
    while menu:
        clear()
        draw()
        print("1 - NEW GAME")
        print("2 - LOAD GAME")
        print("3 - RULES")
        print("4 - QUIT GAME")
        draw()

        if rules:
            print("I'm the creator of this game and these are the rules.")
            rules = False
            choice = ""
            input("> ")

        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("# What's your name, hero ? ")
            menu = False
            play = True
        elif choice == "2":
            try:
                f = open("Saves/load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    GOLD = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    clear()
                    print("Welcome back, " + name + "!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupt save file !")
                    input("> ")
            except OSError:
                print("No loadable save file !")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

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
            print("HP: " + str(HP) + "/" + str(MAXHP))
            print("ATK: " + str(ATK))
            print("POTIONS: " + str(pot))
            print("ELIXIRS: " + str(elix))
            print("GOLD: " + str(GOLD))
            print("COORD: ", x, y)
            draw()
            print("0 - SAVE AND QUIT")
            if y > 0:
                print("1 - NORTH")
            if x < x_len:
                print("2 - EAST")
            if y < y_len:
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            if pot > 0:
                print("5 - USE POTION (30HP)")
            if elix > 0:
                print("6 - USE ELIXIR (50HP)")
            if map[y][x] == "shop" or map[y][x] == "major" or map[y][x] == "cave":
                print("7 - ENTER")
            draw()

            dest = input("# ")

            if dest == "0":
                play = False
                menu = True
                save()

            elif dest == "1":
                if y > 0:
                    y -= 1
                    standing = False

            elif dest == "2":
                if x < x_len:
                    x += 1
                    standing = False

            elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
            
            elif dest == "4":
                if x > 0:
                    x -= 1
                    standing = False
            
            elif dest == "5":
                if pot > 0:
                    pot -= 1
                    heal(30)
                    input("> ")
                else:
                    print("No potions !")
                input("> ")
                standing = True

            elif dest == "6":
                if elix > 0:
                    elix -= 1
                    heal(50)
                    input("> ")
                else:
                    print("No elixirs !")
                input("> ")
                standing = True
            elif dest == "7":
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