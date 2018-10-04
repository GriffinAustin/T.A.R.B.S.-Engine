# Changelog

## Alpha 0.3.0 - October 3rd, 2018

### Added
* Logging separate from debugging. Information here.
* Custom function for getting user input (`userinput()`). This is used so logging and debugging is easier.

### Changes
* A new log is generated every time the program is run.

## Alpha 0.2.2 - October 3rd, 2018

### Fixes

* Fixed an error with the `Player.openchest` function that resulted in using 
`Player.editinv` which is a deprecated function. 

### Added

* Logging: on every run, a log file keeps track of all of the events that have debug output.

## Alpha 0.2.0 - October 2th, 2018

### Changes

* Completely changed how the inventory works
  * The amount of items the player has is now contained in the class for each individual item.
  * Example:
    * ```python
      print(sword.amnt)
      # 1  
      # Within the instance of the `Sword` class, the amnt var says that the player has 1 sword.
      ```
* Changed how inventory editing works:
  * You now add items to the player's inventory with `Player.additem`.
  * Items are now are subtracted from the player's inventory with `Player.removeitem`.

### Fixed

* Debug output for `Player.openchest` now returns the proper output.
* One Shield/Weapon is now removed from the player's inventory when equipped.
* Cleaned up the player class and removed unused vars.

### Added

* `Player.equipweapon` and `Player.equipshield` now have debug output.
* You can now communicate player thoughts by using `Player.think`. \(Thanks Antti Haapala3\)
* Added `Player.unequipweapon` and `Player.unequipshield` to un-equip weapons and shields.

