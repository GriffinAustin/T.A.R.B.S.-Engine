# ILY A
from random import randint, choice
import logging
from datetime import datetime

currenttime = datetime.now().strftime("%I.%M.%S")

log = "{}_log.log".format(currenttime)
logging.basicConfig(filename=log, level=logging.DEBUG)

logging.debug(" Run from {}".format(datetime.now().strftime("%I:%M:%S")))

# Enable debugging and logging var
debug = False
enable_logging = False

version = "Alpha 0.3.0"


# Debug output
def debugout(text):
    if debug:
        print(text)
    else:
        pass


def log(text):
    if enable_logging:
        logging.debug(" {}: {}".format(datetime.now().strftime("%I:%M:%S"), text))
    else:
        pass


# noinspection PyMethodMayBeStatic
class Player:
    def __init__(self, name, hp, maxhp, minatk, maxatk):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.minAtk = minatk
        self.maxAtk = maxatk
        self.weapon_one = None
        self.weapon_one_atk = 0
        self.shield = None
        self.shield_protect = 0

    def additem(self, item, amnt):
        item.amnt += amnt
        debugout("Debugger: item given: {} x {}".format(item.name, amnt))
        log("Debugger: item given: {} x {}".format(item.name, amnt))

    # Remove an item from the player
    def removeitem(self, item, amnt):
        item.amnt -= amnt
        debugout("Debugger: removed: {} x {} from player".format(amnt, item.name))
        log("Debugger: removed: {} x {} from player".format(amnt, item.name))

    # Attack an enemy
    def atk(self, opponent):
        atk = randint(self.minAtk, self.maxAtk)
        totalatk = atk + self.weapon_one_atk
        opponent.hp -= totalatk
        debugout("Damage done: {}".format(totalatk))
        log("Damage done: {}".format(totalatk))
        debugout("Enemy HP: {}".format(opponent.hp))
        log("Enemy HP: {}".format(opponent.hp))
        if opponent.hp <= 0:
            del opponent
            log("Debugging: {} deleted".format(opponent))

    def equipweapon(self, weapon):
        if weapon.amnt > 0:
            self.weapon_one = weapon
            self.weapon_one_atk = weapon.atk
            debugout("Equipped weapon: {}, Damage: {}".format(weapon.name, weapon.atk))
            log("Equipped weapon: {}, Damage: {}".format(weapon.name, weapon.atk))
            weapon.amnt -= 1
        else:
            print("You don't have any!")
            log("Player doesn't have {}".format(weapon))

    def equipshield(self, shield):
        if shield.amnt > 0:
            self.shield = shield.name
            self.shield_protect = shield.defense
            debugout("Equipped shield: {}, Damage reduction: {}".format(shield.name, shield.defense))
            log("Equipped shield: {}, Damage reduction: {}".format(shield.name, shield.defense))
            shield.amnt -= 1
        else:
            print("You don't have any!")
            log("Player doesn't have {}".format(shield))

    def unequipweapon(self, weapon):
        if self.weapon_one:
            Player.weapon_one = None
            Player.weapon_one_atk = 0
            weapon.amnt += 1
            debugout("Debugger: {} unequipped.".format(weapon.name))
            log("Debugger: {} unequipped.".format(weapon.name))
        else:
            debugout("Debugger: Player doesn't have a weapon equipped.")
            log("Debugger: Player doesn't have a weapon equipped.")

    def unequipshield(self, shield):
        if self.shield:
            Player.shield = None
            Player.shield_protect = 0
            shield.amnt += 1
            debugout("Debugger: {} unequipped.".format(shield.name))
            log("Debugger: {} unequipped.".format(shield.name))
        else:
            debugout("Debugger: Player doesn't have a weapon equipped.")
            log("Debugger: Player doesn't have a weapon equipped.")

    def usepotion(self, potion):
        if self.hp >= self.maxhp:
            debugout("HP already at max!")
            log("HP already at max!")
        else:
            self.hp += potion.hp
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            debugout("{} health restored, current health: {}".format(potion.hp, self.hp))
            log("{} health restored, current health: {}".format(potion.hp, self.hp))
            potion.amnt -= 1

    # Make the player speak (more functionality planned)
    def say(self, text):
        print("{}: {}".format(self.name, text))
        log("{}: {}".format(self.name, text))

    # Thanks Antti Haapala
    def drawborder(self, string):
        return (string[0 + i:26 + i] for i in range(0, len(string), 26))

    def think(self, thought):
        print('+-' + '-' * 26 + '-+')
        for line in self.drawborder(thought):
            print('| {0:^{1}} |'.format(line, 26))
        print('+-' + '-' * 26 + '-+')
        log("Player thought: {}".format(thought))

    # Open a lootbox with specified loot (in list form)
    def openchest(self, loot):
        reward = choice(loot)
        debugout("Reward from chest: {}".format(reward.name))
        log("Reward from chest: {}".format(reward.name))
        self.additem(reward, 1)

    # noinspection PyMethodMayBeStatic
    def kill(self, deathmessage, *endgame):
        print(deathmessage)
        log("Player died: {}".format(deathmessage))

        # Decides if the game should exit at death
        if endgame:
            log("Game ended")
            exit()
        else:
            log("Game didn't end on player death")
            pass

    def getinput(self, prompt):
        usr = input(prompt)
        debugout("User input: {}".format(usr))
        log("User input: {}".format(usr))
        return usr


class Enemy:
    def __init__(self, name, hp, minatk, maxatk):
        self.name = name
        self.hp = hp
        self.minAtk = minatk
        self.maxAtk = maxatk

    def atk(self, opponent):
        atk = randint(self.minAtk, self.maxAtk)
        totalatk = atk - opponent.shield_protect
        opponent.hp -= totalatk
        debugout("Damage done: {}".format(totalatk))
        log("Enemy: Damage done: {}".format(totalatk))
        debugout("Player HP: {}".format(opponent.hp))
        log("Enemy player HP: {}".format(opponent.hp))

    # Make the enemy speak (more functionality planned)
    def say(self, text):
        print("{}: {}".format(self.name, text))
        log("{}: {}".format(self.name, text))

    # Debug use
    def __del__(self):
        debugout("{} is dead".format(self.name))
        log("{} is dead".format(self.name))


class NPC:
    def __init__(self, name):
        self.name = name

    def talkto(self, text, *name, ):
        if name:
            print("{}: {}".format(self.name, text))
            log("{}: {}".format(self.name, text))
        else:
            print("{}".format(text))
            log("NPC: {}".format(text))


class Weapon:
    def __init__(self, name, atk):
        self.amnt = 0
        self.name = name
        self.atk = atk


class Potion:
    def __init__(self, name, hp):
        self.amnt = 0
        self.name = name
        self.hp = hp


class Shield:
    def __init__(self, name, defense):
        self.amnt = 0
        self.name = name
        self.defense = defense
