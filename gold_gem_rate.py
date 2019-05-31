# Author: Drenwor S574
# Idle Heroes Gold/Gem Value Simulator V0.1

# Gold_value is the value the user give to gold compared to gems.
# VIP players get more gems daily so, the value that gems have decrease
# there are some breakpoints, I propose the IGC (Income gem coefficient):
# - VIP 0
# - VIP 1 to VIP 6 - Normally monthly card users and some small extras in events (spent between up to 500 USD)
# - VIP 7 to VIP 13 - Getting a huge amount of gems, buying packs everytime
#
# Select the group you belong to in the input data

import math


# Input declaration
vip = 2
level = 95
income_gem_coefficient = 2

# Some important values
HoM_vip = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3.5, 4.0, 4.0]
Raid = [100, 150, 200, 250, 300, 350, 450, 450, 700]
Raid_odds = [0.8, 0.15, 0.05]


def get_gold_ratio(vip, level, income_gem_coefficient):
    if income_gem_coefficient < 0.5:
        gold_value = 56  # When 0.5<IGC<1.5 * 3.5 -> Extra gems are 15k, and 6k is the basic for IGC=1. (15+6)/6 = 3.5
    elif 0.5 <= income_gem_coefficient < 1.5:
        gold_value = 16  # Raid 20 shard3 + 10 shard4 = 300k + 500k
    elif income_gem_coefficient > 1.5:
        gold_value = 1  # They can mainly get the gms they want and exchange it for gold
    else:
        print("Error, select IGC: 1 -> F2P, 2 -> Card & Small expenses, 3 -> P2P")
        return -1

    HoM_rate = (1 + HoM_vip[vip]) * ((49.5 + (level * 1.5))/50)
    if level > 150:
        level = 150
    raid_rate = (Raid[math.floor((level - 30)/15)] * (1 * Raid_odds[0] + 2 * Raid_odds[1] + 3 * Raid_odds[2]))/50
    if max(HoM_rate, raid_rate, gold_value) == HoM_rate:
        return 'HoM', max(HoM_rate, raid_rate, gold_value)
    elif max(HoM_rate, raid_rate, gold_value) == raid_rate:
        return 'raid', max(HoM_rate, raid_rate, gold_value)
    else:
        return 'none', max(HoM_rate, raid_rate, gold_value)


# print(get_gold_ratio(vip, level, income_gem_coefficient))

