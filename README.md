# idleheroes_simulator
Open source simulator for mobile game [Idle Heroes](https://www.facebook.com/Idleheroes/)

This is an open source simulator to help each Idle Hero player. Currently under development.

## Dependencies

The program is written in **Python**.

You can either [download](https://www.python.org/downloads/) it or use [this online tool](https://www.tutorialspoint.com/execute_python_online.php)

## Currently Supported (V0.1)

The following features are currently supported in the simulator:
* Gold/Gem ratio per player. Gives best ingame ratio possible and where to get it.
* Tavern profit in absolute and relative gem values.
* Event balance versus daily quest. Profit in events (Heroic Scroll, Wishing Coin) versus out of it.
* Monthly resource balance.

## Assumptions

The following assumptions are used in the simulator:
* Idle Heroes uses multiple random variables. Hence, values obtain from this simulator are *mean values* that can vary per player.
* Mostly 5* shards become fodder. Currently, I assume all shards will give fooder. This will be changed in the future.
* Monthly resource balance does not consider: Arena fight rewards (daily and end of season), marauder friendship rewards, aspen dungeon rewards

## Known Bugs

These bugs have been reported and tested to be wrong in the current version (V0.1):
* Event Heroic Scroll Profit do not include the event rewards. This will be fixed with the addition of different stages in the event (see ToDo)

## ToDo

Internal features:
* Change Priviledge/Normal cards nomenclature
* Include more tavern strategies
* Improve VIP separation
* Add different possible stages in event fulfillment 
* Count shards/branches in tavern balance
* Battle simulator
* Adding Machine Learning to the algorithms

External features:
* Add Doxygen for easy reading
* Launch webpage
* Add dashboard/graphical interface

## About the author

Idle Heroes Simulator Version 0.1
Drenwor. Server S574.

If you have any questions please write an email.
email: drenwor_gaming@gmail.com

### Supporting and patreon

Programming the simulator takes some time. I would love to improve it, and I will probably do. But of course, things will go faster with some motivation :D.

If you want to support my work you can do it via [Paypal](https://www.paypal.me/robertotorre93)
 or [Patreon](https://www.patreon.com/drenwor_gaming)
.