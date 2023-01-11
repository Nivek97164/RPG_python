
# from simple_term_menu import TerminalMenu


# def main():
#     terminal_menu = TerminalMenu(
#         ["dog", "cat", "mouse", "squirrel"],
#         multi_select=True,
#         show_multi_select_hint=True,
#     )
#     menu_entry_indices = terminal_menu.show()
#     print(menu_entry_indices)
#     print(terminal_menu.chosen_menu_entries)

    


# if __name__ == "__main__":
#     main()



# if play:
#             draw()
#             print("LOCATION: " + biom[map[y][x]]["t"])
#             draw()
#             print("NAME: " + name)
#             print("HP: " + str(HP) + "/" + str(MAXHP))
#             print("ATK: " + str(ATK))
#             print("POTIONS: " + str(pot))
#             print("ELIXIRS: " + str(elix))
#             print("GOLD: " + str(GOLD))
#             print ("COORD: ", x, y)
#             draw()
#             game_menu = ["[0] - SAVE AND QUIT", "[1] - NORTH","[2] - EAST", "[3] - SOUTH", "[4] - WEST", "[5] - USE POTION (30HP)", "[6] - USE ELIXIR (50HP)", "[7] - ENTER"]
#             terminal_menu2 = TerminalMenu(game_menu)
#             menu_entry_index = terminal_menu2.show()
#             if game_menu[menu_entry_index] == "[0] - SAVE AND QUIT":
#                 play = False
#                 menu = True
#                 save() 

#             elif game_menu[menu_entry_index] == "[1] - NORTH":
#                 if y > 0:
#                     y -= 1
#                     standing = False
            
            
#             elif game_menu[menu_entry_index] == "[2] - EAST":
#                 if x < x_len:
#                     x += 1
#                     standing = False
            
#             elif game_menu[menu_entry_index] == "[3] - SOUTH":
#                 if y < y_len:
#                     y += 1
#                     standing = False
            
#             elif game_menu[menu_entry_index] == "[4] - WEST":
#                 if x > 0:
#                     y += 1
#                     standing = False
            
#             elif game_menu[menu_entry_index] == "[5] - USE POTION (30HP)":
#                 if pot > 0:
#                     pot -= 1
#                     heal(30)
#                     input("> ")
#                 else:
#                     print("No potions !")
#                 input("> ")
#                 standing = True
            
#             elif game_menu[menu_entry_index] == "[6] - USE ELIXIR (50HP)":
#                 if elix > 0:
#                     elix -= 1
#                     heal(50)
#                     input("> ")
#                 else:
#                     print("No elixirs !")
#                 input("> ")
#                 standing = True
            
#             elif game_menu[menu_entry_index] == "[7] - ENTER":
#                 if map[y][x] == "shop" or map[y][x] == "major" or map[y][x] == "cave":
#                     if map[y][x] == "shop":
#                         buy = True
#                         shop()
#                     if map[y][x] == "major":
#                         speak = True
#                         major()
#                     if map[y][x] == "cave":
#                         boss = True
#                         cave()
#                 else:
#                     standing = True
#                 draw()