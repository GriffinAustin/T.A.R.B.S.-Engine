from random import randint, choice

# Enable debugging Var
debug = False


# Debug output
def debugout(text):
    if debug:
        print(text)
    else:
        pass


class Player:
    def __init__(self, name, hp, minatk, maxatk):
        self.name = name
        self.hp = hp
        self.inv = {}
        self.minAtk = minatk
        self.maxAtk = maxatk
        self.inv = {}
        self.weapon_one = None
        self.weapon_one_atk = 0
        self.shield = None
        self.shield_protect = 0

    def editinv(self, item, amnt):
        self.inv[item] = amnt
        debugout("Debugger: item given {} x {}".format(item.name, amnt))

    # Remove an item from the player
    def removeitem(self, item):
        self.inv.pop(item)
        debugout("Debugger: removed {} from player".format(item))

    # Attak an enemy
    def atk(self, opponent):
        atk = randint(self.minAtk, self.maxAtk)
        totalatk = atk + self.weapon_one_atk
        opponent.hp -= totalatk
        debugout("Damage done: {}".format(totalatk))
        debugout("Enemy HP: {}".format(opponent.hp))

    def equiptweapon(self, weapon):
        self.weapon_one = weapon
        self.weapon_one_atk = weapon.atk

    def usepotion(self, potion):
        self.hp += potion.hp
        debugout("{} health restored, current health: {}".format(potion.hp, self.hp))

    # Make the player speak (more functionality planned)
    def say(self, text):
        print("{}: {}".format(self.name, text))

    # Open a lootbox with specified loot (in list form)
    def openchest(self, loot):
        reward = choice(loot)
        debugout("Reward from chest: {}".format(reward))
        self.editinv(reward, 1)

    # noinspection PyMethodMayBeStatic
    def kill(self, deathmessage, *endgame):
        print(deathmessage)

        # Decides if the game should exit at death
        if endgame:
            exit()
        else:
            pass


class Enemy:
    def __init__(self, name, hp, minatk, maxatk):
        self.name = name
        self.hp = hp
        self.minAtk = minatk
        self.maxAtk = maxatk

    # Make the enemy speak (more functionality planned)
    def say(self, text):
        print("{}: {}".format(self.name, text))

    # Debug use
    def __del__(self):
        print("{} is dead".format(self.name))


class NPC:
    def __init__(self, name):
        self.name = name

    def talkto(self, name, text):
        if name:
            print("{}: {}".format(self.name, text))
        else:
            print("{}".format(text))


class Weapon:
    def __init__(self, name, atk):
        self.name = name
        self.atk = atk


class Potion:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
