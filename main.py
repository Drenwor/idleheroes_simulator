# Author: Drenwor S574
# Idle Heroes Main Simulator V0.1

# ToDo: change cards nomenclature
# ToDo: add more tavern strats
# ToDo: count shards/branches in tavern balance

import gold_gem_rate
import event_profit
import spend_gems
import tavern_profit

# Variable declaration
vip = 4
level = 98
cards = 1
whale = 0
tavern_strat = 5  # Currently only strat 5 supported
celestial_gem_mine_level = 20
celestial_gem_mine_number = 2

if cards == 1:
    priv_card = 0.81081
    norm_card = 0.189189
elif cards == 0.8:
    priv_card = 0.81081
    norm_card = 0
elif cards == 0.2:
    priv_card = 0
    norm_card = 0.189189
else:
    priv_card = 0
    norm_card = 0


class IngemValue(object):

    def __init__(self, vip, level, cards, whale):
        self.hs_odds = [0.7842, 0.20, 0.0158]
        self.hs_odds_event = [0.7784, 0.19, 0.0316]

        # We assume we never go for the least gold option...makes no sense if we want gold
        self.coin_gold_base = [20, 60, 160, 200, 250]
        self.coin_gold_total = [(base * 0.95 + base * 0.05 * 1.5) for base in self.coin_gold_base]
        self.coin_level_steps_possible = [1, 41, 81, 111, 141]
        self.coin_level_step = [(steps - level) <= 0 for steps in self.coin_level_steps_possible].count(True) - 1

        self.fodder_to_e3 = 179
        self.heroes_to_e3 = 7
        self.hs_cost = 125
        self.po_cost = 500
        self.coin_cost = 30
        self.gold_method, self.gold = gold_gem_rate.get_gold_ratio(vip, level, cards + whale)
        self.shard3 = 300/self.gold
        self.shard4 = 1500/self.gold
        self.shard5 = (self.hs_cost - self.shard3 * self.hs_odds_event[0] - self.shard4 * self.hs_odds_event[1]) / self.hs_odds_event[2]
        self.supercoin_cost = 5 * self.coin_cost
        self.feather_cost = ((self.fodder_to_e3/self.heroes_to_e3) * self.shard5)/60


##################################################################################################

print("\n\nResults for user VIP " + str(vip) + " with lvl " + str(level))
gemValues = IngemValue(vip, level, cards, whale)
print(gold_gem_rate.get_gold_ratio(vip, level, cards+whale))
print(gemValues.shard3, gemValues.shard4, gemValues.shard5)
profit_hs, profit_hs_event = event_profit.get_profit_hs(gemValues)
print('\nHeroic Scroll profit:')
print("Daily:\t" + str(profit_hs))
print("Event:\t" + str(profit_hs_event))


profit_coin, profit_coin_event = event_profit.get_profit_coin(gemValues)
print('\nCoin profit:')
print("Daily:\t" + str(profit_coin))
print("Event:\t" + str(profit_coin_event))

# Should we do the daily quest?
#
# Normally, two things matter: HS + WC. Let's breakdown both

# We do daily:
output_daily = profit_coin * 2 + profit_hs + 120

# We save for events
output_events = profit_coin_event * 2 + profit_hs_event

print('\nProfit from burning HS and coins for daily quest:')
print("Daily:\t" + str(output_daily))
print("Event:\t" + str(output_events))


print("\n\nTavern Gem Reroll cost")
print(tavern_profit.getGemRerollCost(vip, tavern_strat))
print("Tavern absolute rewards")
print("Gems // Scrolls // PO //  Coins")
abs_tavern_rewards = tavern_profit.getAbsoluteRewards(vip, tavern_strat)
print(abs_tavern_rewards)
print("Rewards in gems (not counting shards/branches)")
print(tavern_profit.getRewardsInGem(vip, tavern_strat))
print("Tavern balance in gems (not counting shards/branches)")
print(tavern_profit.getRewardsInGem(vip, tavern_strat) - tavern_profit.getGemRerollCost(vip, tavern_strat))

# My particular case...don't get much gems so...where to spend them?

myRes = spend_gems.GetResources(priv_card + norm_card, vip, tavern_strat, celestial_gem_mine_number, celestial_gem_mine_level)
myRes.add_campaign('po', 8)
myRes.add_po()
myRes.add_casino()
myRes.add_militants()
myRes.add_tavern()
myRes.add_fusion()
myRes.add_summon(1)
print("\n\nMonthly resource calculation:")
print("Gems // Scrolls // PO // Super coins //  Coins // Arena Tickets")
results = myRes.show_resources()
print(results)
print("If rolling super chips...")
myRes.roll_casinochips()
results = myRes.show_resources()
print(results)
print("Monthly balance in gems (Arena Tickets not added):")
print(results[0] + results[1] * gemValues.hs_cost + results[2] * gemValues.po_cost + results[4] * gemValues.coin_cost)
print(str(abs(results[5] * 60)) + "K gold in arena tickets or " + str(abs(results[5] * 12)) + " gems")
