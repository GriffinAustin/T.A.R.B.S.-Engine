# Quickstart Guide

Quick-start guide on how to get up and running quickly and easily The main reason why T.A.R.B.S. engine is different from other engines is due to the limitations. It isn't limited at all. T.A.R.B.S. engine doesn't limit you with GUI or story-line. You aren't even required to build a story. That's all up to you. T.A.R.B.S. engine provides all of the functionality, all you have to do is the easy part. You just need to call the functions.

First, you need to import the module.

```python
import TARBSengine
```

An important step in software development is debugging. Luckily, T.A.R.B.S. comes with a debugger. We can enable it by setting the `TARBSengine.debug` variable to true.

```python
TARBSengine.debug = True
```

Next, you need to create a player instance from the Player class

To do that, you need five arguments: name, HP, maximum HP, minimum Attack damage, and maximum attack damage.

```python
player = TARBSengine.Player("Steven", 20, 20, 5, 10)
```

Now, we can create an enemy from the Enemy class.

For the enemy class, you will need only four arguments: name, HP, \(this is the same as maximum HP.\) \(This is because enemies cannot heal as of now\) minimum Attack damage, and maximum attack damage.

```python
zombie = TARBSengine.Enemy("Dave the Zombie", 11, 5, 10)
```

We have an enemy. Let's give him a purpose. His purpose is to defend a princess. We need a princess though. For that, we will use the `NPC` class.

```python
princess = TARBSengine.NPC("The Princess")
```

Now, lets attack Dave. We can do that by calling the `Player.atk()` function.

```python
player.atk(zombie)
```

Let's have Dave attack the player now. That can be done with the `Enemy.atk()` function.

```python
zombie.atk(player)
```

Thanks to debugging, we can see exactly how much damage the attack did and how much HP the player has left. Let's attack Dave one more time.

```python
player.atk(zombie)
```

Dave is dead. We can now talk to the princess. The princess is going to give us something. We can create a potion using the `Potion` class. Let's make a healing potion.

```python
magic_potion = TARBSengine.Potion("Magic Health Potion", 5)
```

Now, let's make the Princess talk to us and give us the potion. We can do that by using the `NPC.talkto()` function in the `NPC` class.

```python
princess.talkto("Thank you for saving me", True)
```

{% hint style="info" %}
Using True or False as a second argument will decide if the NPC's name will show up when speaking
{% endhint %}

Now, let's edit the player's inventory to add a potion.

```python
princess.talkto("You look hurt, here is a magic potion to heal you", True) 
player.editinv(magic_potion, 1)
```

Now that the player has the magic potion, let's use the `Player.usepotion()` function to drink the potion and heal.

```python
player.usepotion(magic_potion)
```

Here is the full code if you want to copy it:

```python
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
```

That basic information should be enough to get a simple game up and running. If you would like to learn more about the engine, you can read about it here



