import classes

play = classes.Player("steve", 5, 5, 100)
classes.debug = True

loot = ["sword", "condom", "STDS"]
chest = classes.Chest(loot)

play.editinv("coins", 10)
play.editinv("coins", 5)
chest.openchest(loot)