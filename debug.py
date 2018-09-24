import TARBSengine

TARBSengine.debug = True

player = TARBSengine.Player("Steven", 20, 20, 5, 10)

zombie = TARBSengine.Enemy("Dave the Zombie", 11, 5, 10)

princess = TARBSengine.NPC("The Princess")

player.atk(zombie)

zombie.atk(player)

player.atk(zombie)

magic_potion = TARBSengine.Potion("Magic Health Potion", 5)

princess.talkto("Thank you for saving me", True)

princess.talkto("You look hurt, here is a magic potion to heal you", True)

player.editinv(magic_potion, 1)

player.usepotion(magic_potion)
