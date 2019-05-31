# Author: Drenwor S574
# Idle Heroes Tavern Simulator V0.1

quest_count = [5, 6, 6, 7, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15]
refresh_cost = 10

quest4_odds = 0.15
quest5_odds = 0.08
quest6_odds = 0.01
quest7_odds = 0.002

gem_odds = 0.4
hs_odds = 0.1
wc_odds = 0.1
po_odds = 0.1
shard4_odds = 0.2
shard5_odds6 = 0.2
shard5_odds7 = 0.25
at_odds = 0.2
branch_odds = 0.2
greenart_odds = 0.1
redart_odds = 0.05


gemquest4 = 50
gemquest5 = 90
gemquest6 = 160
gemquest7 = 315
shard4quest4 = 6
shard4quest5 = 15
shard5quest6 = 4
shard5quest7 = 15
hsquest4 = 1
hsquest5 = 2
atquest4 = 2
atquest5 = 3
wcquest4 = 1
wcquest5 = 2
branchquest6 = 40
branchquest7 = 90
poquest6 = 1
poquest7 = 2


tavern_strat = 5


def getGemRerollCost(vip, tavern_strat):
    total_quests = quest_count[vip] * 30
    if tavern_strat == 5:
        gemcost = refresh_cost * total_quests/(1 - 0.849)
    return gemcost


def getAbsoluteRewards(vip, tavern_strat):
    total_quests = quest_count[vip] * 30
    if tavern_strat == 5:
        reroll_success = 0.151
        gems = ((quest7_odds/reroll_success) * gem_odds * gemquest7 + \
               (quest6_odds/reroll_success) * gem_odds * gemquest6 \
               + (((gem_odds + shard4_odds + hs_odds + wc_odds) * quest5_odds)/reroll_success) * gem_odds * gemquest5 \
               + (((gem_odds + hs_odds) * quest4_odds)/reroll_success) * gem_odds * gemquest4) * total_quests
        hs = ((((gem_odds + shard4_odds + hs_odds + wc_odds) * quest5_odds)/reroll_success) * hs_odds * hsquest5 \
               + (((gem_odds + hs_odds) * quest4_odds)/reroll_success) * hs_odds * hsquest4) * total_quests
        wc = ((((gem_odds + shard4_odds + hs_odds + wc_odds) * quest5_odds)/reroll_success) * wc_odds * wcquest5) * total_quests
        po = ((quest7_odds/reroll_success) * po_odds * poquest7 + \
               (quest6_odds/reroll_success) * po_odds * poquest7) * total_quests
        return gems, hs, po, wc


def getRewardsInGem(vip, tavern_strat):
    gems, hs, po, wc = getAbsoluteRewards(vip, tavern_strat)
    return gems + hs * 125 + po * 500 + wc * 30

