import TARBSengine

TARBSengine.debug = True

player = TARBSengine.Player("Steven", 10, 5, 100)

hp = TARBSengine.Potion("HP Potion", 5)

player.editinv(hp, 1)

player.usepotion(hp)
