
from termcolor import colored, cprint
import termcolor

def display_board(board):
    element_colors = [['#', 'grey'], ['█', 'blue'], ['F', 'green'], ['G', 'magenta'], ['S', 'yellow'],
                      ['E', 'red'], ['R', 'cyan'], ["?", "yellow"], ['A', 'magenta'], ['*', 'red']]
    elements = ['#', '█', 'F', 'G', 'S', 'E', 'R', "?", 'A', '*']
    colors = ['grey', 'blue', 'green', 'magenta', 'yellow', 'red', 'cyan', 'yellow', 'magenta', 'red']
    
    for i in range(len(board)):
        row = ''.join(board[i])
        for x in range(len(element_colors)):
            row = row.replace(elements[x], termcolor.colored(elements[x], colors[x]))
        print(row, end='')

def display_stats(player_dict):
    x = player_dict['name']
    print(f'CHARACTER NAME -=-=-> {x}')
    stats = player_dict['stats']
    if 30 < stats['HP'] < 65:
        print('HP (Health Points): ', end='')
        cprint(stats['HP'], 'yellow') 
    elif stats['HP'] > 65:
        print('HP (Health Points): ', end='')
        cprint(stats['HP'], 'green')
    elif stats['HP'] < 30:
        print('HP (Health Points): ', end='')
        cprint(stats['HP'], 'red')
    
    if 30 < stats['att'] < 65:
        print('ATTACK:', end='')
        cprint(stats['att'], 'yellow') 
    elif 100 > stats['att'] > 65:
        print('ATTACK: ', end='')
        cprint(stats['att'], 'green')
    elif stats['att'] < 30:
        print('ATTACK: ', end='')
        cprint(stats['att'], 'red')

    if 30 < stats['def'] < 65:
        print('DEFFENCE: ', end='')
        cprint(stats['def'], 'yellow') 
    elif 100 > stats['def'] > 65:
        print('DEFFENCE: ', end='')
        cprint(stats['def'], 'green')
    elif stats['def'] < 30:
        print('DEFFENCE: ', end='')
        cprint(stats['def'], 'red')

    if 30 < stats['exp'] < 65:
        print('EXPERIENCE: ', end='')
        cprint(stats['exp'], 'yellow') 
    elif 100 > stats['exp'] > 65:
        print('EXPERIENCE: ', end='')
        cprint(stats['exp'], 'green')
    elif stats['exp'] < 30:
        print('EXPERIENCE: ', end='')
        cprint(stats['exp'], 'red')




    '''stats['HP']
    stats['att']
    stats['def']
    stats['exp']'''

    



def display_inventory(player_inventory):
    print('\n _________ INVENTORY _________')
    for inv_key, inv_value in player_inventory.items():
        print(str(inv_key) + ' --=--> ' + str(inv_value))
    print('\n')
