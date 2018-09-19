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
        debugout("debug: inv: {}".format(self.inv))

    def removeitem(self, item):
        self.inv.pop(item)

    def atk(self, opponent):
        atk = randint(self.minAtk, self.maxAtk)
        opponent.hp -= atk
        print(atk)
        print(opponent.hp)

    def say(self, text):
        print("{}: {}".format(self.name, text))

    def __del__(self):
        print("Game Over")


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


class Chest(Player):
    def __init__(self, loot):
        self.loot = loot
        super(Player, self).__init__()

    def openchest(self, loot):
        reward = choice(loot)
        Player.editinv(self, reward, 1)
        debugout("Item given: {}".format(reward))
