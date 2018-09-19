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

    def editinv(self, item, amnt):
        self.inv[item] = amnt
        debugout("Debugger: item given {} x {}".format(item, amnt))

    # Remove an item from the player
    def removeitem(self, item):
        self.inv.pop(item)
        debugout("Debugger: removed {} from player".format(item))

    # Attak an enemy
    def atk(self, opponent):
        atk = randint(self.minAtk, self.maxAtk)
        opponent.hp -= atk
        print(atk)
        print(opponent.hp)

    # Make the player speak (more functionality planned)
    def say(self, text):
        print("{}: {}".format(self.name, text))

    # Open a lootbox with specified loot (in list form)
    def openchest(self, loot):
        reward = choice(loot)
        debugout("Reward from chest: {}".format(reward))
        self.editinv(reward, 1)

    # noinspection PyMethodMayBeStatic
    def killplayer(self, deathmessage, *endgame):
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

    def talkto(self, name, text, *text2, **text3):
        if name:
            print("{}: {}".format(self.name, text))
            print("{}: {}".format(self.name, text2))
            print("{}: {}".format(self.name, text3))
        else:
            print("{}".format(text))
            print("{}".format(text2))
            print("{}".format(text3))