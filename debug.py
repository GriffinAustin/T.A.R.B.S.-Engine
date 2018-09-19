import TARBSengine

player = TARBSengine.Player("steve", 5, 1, 5)

TARBSengine.debug = True

loot = ["Sword", "dagger", "bow", "knife"]

player.openchest(loot)
