# Changelog

## Alpha 0.2.0 - October 7th, 2018

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

