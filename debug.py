import TARBSengine

villager = TARBSengine.NPC("Strange Villager")

TARBSengine.debug = True

villager.talkto(True, "This is some debug text")
villager.talkto(False, "This is laskdjaskldjl debug text")


sword = TARBSengine.Weapon("Devil Sword", 5)

zombie = TARBSengine.Enemy("Evil zombie", 10, 5, 10)
player = TARBSengine.Player("steve", 5, 1, 1)
player.equiptweapon(sword)
print(player.weapon_one.name, player.weapon_one_atk)
player.atk(zombie)
