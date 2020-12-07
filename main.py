
import engine
import os
import sys
import util
import ui
import titlepage


def main():
    maps_names = ['map1.txt', 'map2.txt', 'map3.txt']
    titlepage.print_title_page()
    user_name = str(input('PROVIDE YOUR CHARACTERS NAME:'))
    in_game = True
    world = 1
    player = engine.create_player(user_name)
    player_dict = player[0]
    player_inventory = player[1]
    player_initial_position = (8, 8)
    while in_game == True:
        in_game = engine.player_is_going_throug_map(maps_names, world, player_initial_position, user_name, player_dict, player_inventory)
        world += 1
        if in_game == False:
            #print('you won') or you lose
            break
    #print effect
    #print 1 main menu or 2 exit
    #easter egg shift+5



if __name__ == '__main__':
    main()
