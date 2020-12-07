
'''
warstwy do złączenia:
1 board interfejsu :warstwa board - większa mapa : tła interfejsu

2 game board : 
    warstwa board: wrogów
    warstwa board: Fight_equipments i Food oraz Healing_potions
    warstwa board: plansza z danym światem
    warstwa board: z playerem

3 board planszy walki:
'''



class Universe: # class for going through worlds
    def __init__(self) -> None:
        pass
    

    class Game_board:
        def __init__(self) -> None:
            pass
    
class Fight_board:
    def __init__(self) -> None:
        pass
    

class Interface_board:
    def __init__(self) -> None:
        pass
    

class Player:
    def __init__(self, name: str = "Warrior", icon: str = "@") -> None:
        self.name = name
        self.icon = icon
        self.health_points = {'current':100, 'max':100} 
        self.equipped_armor = Fight_equipments.armor()
        self.experience = 1 #increment by specified points each time enemy is killed
        self.attack =  self.experience + self.equipped_weapon.attack #player level of destruction
        self.equipped_weapon = Fight_equipments.weapon()


        def change_armor(self) -> None:
            pass

        def change_weapon(self) -> None: 
            self.inventory = Inventory()


class key_map:
    def __init__(self, key_to_change_armor = "q", key_to_change_weapon = "e", key_to_right = "d", key_to_left = "a", key_to_up = "w", key_to_down = "s", key_to_show_inventory = "i"):
        self.key_to_change_armor = key_to_change_armor
        self.key_to_change_weapon = key_to_change_weapon
        self.key_to_right = key_to_right
        self.key_to_left = key_to_left
        self.key_to_up = key_to_up
        self.key_to_down = key_to_down
        self.key_to_show_inventory = key_to_show_inventory  
    

class Inventory: # To open anytime after pressing 'I' key
    def __init__(self) -> None:
        
        self.inventory = [] # armor1, healingpotion, weapon2, weapon1, armor3, healingpotion, healingpotion..

    def get(self) -> list:
        pass
        # [armor1, armor3],[weapon3, weapon1, weapon22], [healingpotion]


    ''' def add(self, item: Fight_equipments or Healing_potions) -> None:
            self.inventory.append(item)
                pass
    '''
    
    def delete():
        pass


    def show(self) -> list:
        pass

    
class Enemy: 
    def __init__(self) -> None:
        pass
    
    class Elfs:
        def __init__(self) -> None:
            pass
    


    class Knights:
        def __init__(self) -> None:
            pass
    

    class Orcs:
        def __init__(self) -> None:
            pass
    


    class DragonBoss:
        # The boss is a larger (at least 5-by-5), autonomously moving character.
        def __init__(self) -> None:
            pass
    


class Keys: # after killing at least 3 enemies at given World, player get key for opening gate to another world 
    def __init__(self) -> None:
        pass
    

class Fight_equipments:
    def __init__(self) -> None:
        pass
    
    class weapon:
        def __init__(self, attack: int = 5) -> None:
            self.attack = attack
    
    
    class armor:
        def __init__(self) -> None:
            pass
    

class Food:
    def __init__(self) -> None:
        pass
    

class Healing_potions:
    amount = 0
    def __init__(self) -> None:
        pass
    def add(self) -> None:
        amount += 1
    
    def decrease(self) -> None:
        amount -+ 1

    def get(self) -> int:
        return amount
    

class Rouglike:
    def __init__(self) -> None:
        pass
    

class Scoreboard:
    def __init__(self) -> None:
        pass
    
