
import os
import ui
import util
import battle_art
import random
import time





def create_board(file_name):
    row = list()
    final_board = list(list())
    with open(file_name) as f:
        board_lines = f.readlines()
    
    for i in range(len(board_lines)):
        board_temp = board_lines[i]
        row_list = str(board_temp)
        for x in row_list:
            row.append(x)
        final_board.append(row)
        row = list()
    return final_board


def create_player(user_name):
    x = str(user_name)
    player_dict = {'name': x, 'player_icon':'█', 'stats':{'att':1, 'def':1, 'exp':0, 'HP':100}}
    player_inventory = {'Armour':{'Leather Armour':3}, 'Weapon':{'Dagger':6}, 'Healing potions':0}
    return (player_dict, player_inventory)





def put_player_on_board(board, player_dict, player_initial_position):
    
    player_icon = player_dict['player_icon']
    board[player_initial_position[0]][player_initial_position[1]] = player_icon


def create_item_list() -> list:
    weapons = [{'dagger':5}, {'sword':10}, {'axe':15}]
    armours = [{'leather_armour':7}, {'chainmail_armour':19}, {'plate_armour':24}]
    healing_potions = [{'healing_potion':1}]
    items_list = []
    items_list.append(weapons)
    items_list.append(armours)
    items_list.append(healing_potions)
    return items_list


def draw_item(items) -> dict:
    draw_cathegory_item = random.choice(range(0,3))
    draw_item_id = random.choice(range(0, len(items[draw_cathegory_item])))
    return items[draw_cathegory_item][draw_item_id]


def add_to_inventory(player_inventory, items_list, item) -> None:
    weapons_list = 0
    armours_list = 1
    healing_potions = 2

    if item in items_list[weapons_list]:
        player_inventory['Weapon'] = item[list(item.keys())[0]]
    elif item in items_list[armours_list]:
        player_inventory['Armour'] = item[list(item.keys())[0]]
    elif item in items_list[healing_potions]:
        player_inventory['Healing potions'] = item[list(item.keys())[0]] + 1

#def use_healing_potion(player_inventory) -> None:
    healing_potions_amount = player_inventory['Healing potions'] 
    if (healing_potions_amount - 1) > 0:
        healing_potions_amount -= 1
    player_inventory['Healing potions'] = healing_potions_amount

def update_player_stats(player_dict, items_list, item: dict) -> None:
    weapons_list = 0
    armours_list = 1
    healing_potions = 2

    if item in items_list[weapons_list]:
        player_dict['stats']['att'] = item[list(item.keys())[0]]
    elif item in items_list[armours_list]:
        player_dict['stats']['def'] = item[list(item.keys())[0]]
    elif item in items_list[healing_potions]:
        player_dict['stats']['healing_potion'] = item[list(item.keys())[0]]
        


def move_player_on_board(key_pressed, board, player_dict, player_current_position):
    row = player_current_position[0]
    col = player_current_position[1]
    player_icon_temp = player_dict['player_icon']
    if key_pressed == 'w':
        #if check_move_is_valid(board):
        board[row-1][col] = player_icon_temp 
    elif key_pressed == 'a':
        board[row][col-1] = player_icon_temp
    elif key_pressed == 's':
        board[row+1][col] = player_icon_temp
    elif key_pressed == 'd':
        board[row][col+1] = player_icon_temp
    board[row][col] = ' '


def update_curr_player_posit(player_current_position, key_pressed):
    if key_pressed == 'w':
        player_current_position[0] = player_current_position[0]-1 
    elif key_pressed == 'a':
        player_current_position[1] = player_current_position[1]-1
    elif key_pressed == 's':
        player_current_position[0] = player_current_position[0]+1
    elif key_pressed == 'd':
        player_current_position[1] = player_current_position[1]+1


def effect_of_key(board, player_current_position, key_pressed):
    row = player_current_position[0]
    col = player_current_position[1]
    list_of_bloced_moves = ['-', '|', 'R', '#']
    if key_pressed == 'w':
        if board[row-1][col] in list_of_bloced_moves:
            return 'blocked'
        elif board[row-1][col] == 'F':
            return 'food'
        elif board[row-1][col] in ('?'):
            return 'item'
        elif board[row-1][col] == 'E':
            return 'enemy'
        elif board[row-1][col] == 'G':
            return 'gate'
        elif board[row-1][col] == '█':
            return 'boss_encounter'
        else:
            return 'move'
    elif key_pressed == 's':
        if board[row+1][col] in list_of_bloced_moves:
            return 'blocked'
        elif board[row+1][col] == 'F':
            return 'food'
        elif board[row+1][col] in ('?'):
            return 'item'
        elif board[row+1][col] == 'E':
            return 'enemy'
        elif board[row+1][col] == 'G':
            return 'gate'
        elif board[row-1][col] == '█':
            return 'boss_encounter'
        else:
            return 'move'
    elif key_pressed == 'a':
        if board[row][col-1] in list_of_bloced_moves:
            return 'blocked'
        elif board[row][col-1] == 'F':
            return 'food'
        elif board[row][col-1] in ('?'):
            return 'item'
        elif board[row][col-1] == 'E':
            return 'enemy'
        elif board[row][col-1] == 'G':
            return 'gate'
        elif board[row-1][col] == '█':
            return 'boss_encounter'
        else:
            return 'move'
    elif key_pressed == 'd':
        if board[row][col+1] in list_of_bloced_moves:
            return 'blocked'
        elif board[row][col+1] == 'F':
            return 'food'
        elif board[row][col+1] in ('?'):
            return 'item'
        elif board[row][col+1] == 'E':
            return 'enemy'
        elif board[row][col+1] == 'G':
            return 'gate'
        elif board[row-1][col] == '█':
            return 'boss_encounter'
        else:
            return 'move'



def enemy_encounter(player_dict, player_inventory, enemy_dict):
    def blink():

        time.sleep(0.1)
        os.system('color 74')
        time.sleep(0.1)
        os.system('color 04') 
        time.sleep(0.1)
        os.system('color 74')
        time.sleep(0.1)
        os.system('color 04')
        time.sleep(0.1)
        os.system('color 74')
        time.sleep(0.1)
        os.system('color 04') 
        time.sleep(0.1)
        os.system('color 74')
        time.sleep(0.1)
        os.system('color 04')  
        
        
    os.system('color 04')
    util.clear_screen()
    battle_art.print_battle_art()
    time.sleep(1)
    print(f'      Player is fighting with : {enemy_dict["name"]}')
    os.system('pause')
    util.clear_screen()
    turn = "player"
    player_hit = player_dict["stats"]["att"]
    enemy_hit = enemy_dict["stats"]["att"] - player_dict["stats"]["def"]

    while player_dict["stats"]["HP"] > 0 or enemy_dict["stats"]["HP"] > 0:

        if enemy_dict["stats"]["HP"] <= 0:
            os.system('cls')
            os.system('color F1')
            battle_art.print_battle_art()
            print(f'''
              ---------------------------------------------___
            -- {player_dict['name']} , you won this encounter.                  `|'''''''---------.........,,,,,,,,_____,_'|B
            -- May a good luck be with you next time as well. |''''''----------.........,,,,,,,____,_'|B
            -- Go! Don't loose your time. It's precious. |'''''''----------.........,,,,,,,,______'|B
            -- Dragon is awaken already !!! |------------`
              ------------------------------`
            ''')
            player_dict["stats"]["exp"] += 12
            player_dict["stats"]["HP"] += 13
            player_dict["stats"]["att"] += 13
            return 'win'
        
        elif player_dict["stats"]["HP"] <= 0:
            print("       Player died. Game over.")
            return 'loose'
        
        if turn == "player":
            os.system('cls')
            battle_art.print_battle_art()
            print("       Player's turn")
            while True:
                players_decision = input('       Press "A" for attack, "D" for defeat, "H" for healing potion:\n').upper()
                if players_decision == "A":
                    chance_to_hit = random.randint(1, 60)
                    if chance_to_hit <= (50 + player_dict["stats"]["exp"]):
                        blink()
                        print(f"       You hit {enemy_dict['name']}!")
                        enemy_dict["stats"]["HP"] -= (player_hit + 65)
                        print(f"       {enemy_dict['name']}'s health left: ", enemy_dict["stats"]["HP"], "\n")
                        time.sleep(3)
                        
                        turn = "enemy"
                        break
                    else:
                        blink()
                        print(f"       You missed {enemy_dict['name']}\n")
                        time.sleep(3)
                        
                        turn = "enemy"
                        break
                elif players_decision == "D":
                        pass # escape to the main board
                        break # escape to the main board
                elif players_decision == "H":
                    if player_inventory["Healing potions"] != 0:
                            player_inventory["Healing potions"] -= 1 
                            player_dict["stats"]["HP"] += 20 
                            print("       Player's health left: ", player_dict["stats"]["HP"], "\n")
                            # if player.current_health > player.health:     tutaj chciałem zrobić rozróżnienie między max health i current health, ale przed jutrom można olać
                            #      player.current_health = player.health
                    else:
                        print("No healing potion in player's inventory.")
                else:
                    print("       Wrong input. Try again.")
                
        elif turn == "enemy":
            os.system('cls')
            battle_art.print_battle_art()
            print(f"       - - - {enemy_dict['name']}'s turn - - -\n      PREPARE YOURSELF !\n")
            time.sleep(2)
            chance_to_hit = random.randint(1, 100)
            if chance_to_hit > (50 + player_dict["stats"]["exp"]):
                player_dict["stats"]["HP"] -= enemy_hit
                blink()
                print(f"       {enemy_dict['name']} hit you")
                print("Player's health left: ", player_dict["stats"]["HP"], "\n")
                time.sleep(3)
                
            else:
                blink()
                print(f"       {enemy_dict['name']} missed you\n")
                time.sleep(3)
                
            turn = "player"	



def lower_HP(player_dict):
    player_dict['stats']['HP'] -= 1

def higher_HP(player_dict):
    player_dict['stats']['HP'] += 100

def player_is_going_throug_map(maps_names, world, player_initial_position, user_name, player_dict, player_inventory):
    
    player_current_position = [player_initial_position[0], player_initial_position[1]]  
    
    enemy_dict_1 = {'name':'Elf','stats':{'att':10, 'HP':100}}
    enemy_dict_2 = {'name':'Knight','stats':{'att':45, 'HP':130}} 
    enemy_dict_3 = {'name':'Orc','stats':{'att':80, 'HP':160}}
    enemy_dict_4 = {'boss':{'att':110, 'HP':200}}
    if world == 1:
        enemy_dict = enemy_dict_1
    if world == 2:
        enemy_dict = enemy_dict_2
    if world == 3:
        enemy_dict = enemy_dict_3

    final_board = create_board(maps_names[world-1])
    put_player_on_board(final_board, player_dict, player_initial_position)
    items_list = create_item_list()
    while True:
        util.clear_screen()
        ui.display_board(final_board)
        ui.display_stats(player_dict)
        ui.display_inventory(player_inventory)
        key_pressed = util.key_pressed()
        effect_of_key_pressed = effect_of_key(final_board, player_current_position, key_pressed)
        if effect_of_key_pressed == 'move':
            lower_HP(player_dict)
            move_player_on_board(key_pressed, final_board, player_dict, player_current_position)
            update_curr_player_posit(player_current_position, key_pressed)
        elif effect_of_key_pressed == 'blocked':
            continue
        elif effect_of_key_pressed == 'food':
            higher_HP(player_dict)
            move_player_on_board(key_pressed, final_board, player_dict, player_current_position)
            update_curr_player_posit(player_current_position, key_pressed)
        elif effect_of_key_pressed == 'item':
            #pick random item from item list
             ###dopisane Roman
            picked_item = draw_item(items_list)
            add_to_inventory(player_inventory, items_list, picked_item)
            update_player_stats(player_dict, items_list, picked_item)
            #add to inventory
            #update stats ```ROMAN DZIAŁA NAD TYM```
            move_player_on_board(key_pressed, final_board, player_dict, player_current_position)
            update_curr_player_posit(player_current_position, key_pressed)
        elif effect_of_key_pressed == 'enemy':
            # go to fight ``` ADAM TO ZROBI ```
            move_player_on_board(key_pressed, final_board, player_dict, player_current_position)
            update_curr_player_posit(player_current_position, key_pressed)
            enemy_encounter(player_dict, player_inventory, enemy_dict)
            os.system('pause')
            os.system('color 07')
            enemy_dict_1 = {'name':'Elf','stats':{'att':10, 'HP':100}}
            enemy_dict_2 = {'name':'Knight','stats':{'att':45, 'HP':130}} 
            enemy_dict_3 = {'name':'Orc','stats':{'att':80, 'HP':160}}
            enemy_dict_4 = {'boss':{'att':110, 'HP':200}}
            if world == 1:
                enemy_dict = enemy_dict_1
            if world == 2:
                enemy_dict = enemy_dict_2
            if world == 3:
                enemy_dict = enemy_dict_3
            #return True or False#w zależności czy wygrasz czy przegrasz walkę
        elif effect_of_key_pressed == 'gate':
            return True
        elif effect_of_key_pressed == 'boss_encounter':
            enemy_dict = enemy_dict_4
            enemy_encounter(player_dict, player_inventory, enemy_dict)
            return False
            # intit boss
            # print boss
            # ruszaj bossem
            # walka z bossem - return 'win' or 'loose'