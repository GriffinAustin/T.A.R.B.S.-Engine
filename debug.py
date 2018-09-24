import TARBSengine

TARBSengine.debug = True

player = TARBSengine.Player("Steven", 5, 10, 5, 100)

hp = TARBSengine.Potion("HP Potion", 5)

print(player.inv)

player.editinv(hp, 1)

print(player.inv)

player.usepotion(hp)

print(player.hp)

print(player.inv)