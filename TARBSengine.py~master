from random import randint, choice

debug = False


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

    def removeitem(self, item):
        self.inv.pop(item)
        debugout("Debugger: removed {} from player".format(item))

    def atk(self, opponent):
        atk = randint(self.minAtk, self.maxAtk)
        opponent.hp -= atk
        print(atk)
        print(opponent.hp)

    def say(self, text):
        print("{}: {}".format(self.name, text))

    def openchest(self, loot):
        reward = choice(loot)
        debugout("Reward from chest: {}".format(reward))
        self.editinv(reward, 1)

    def killplayer(self, deathmessage, *endgame):
        print(deathmessage)
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

    def say(self, text):
        print("{}: {}".format(self.name, text))

    def __del__(self):
        print("{} is dead".format(self.name))
