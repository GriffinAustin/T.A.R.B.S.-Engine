import classes

play = classes.Player("steve", 5, 5, 100)
classes.debug = True

play.editinv("coins", 10)
play.editinv("coins", 5)
