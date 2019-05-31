# Author: Drenwor S574
# Idle Heroes Resource Simulator V0.1

# Things i'm still not counting:
# Arena fight rewards // end of season rewards // marauder frienship rewards
# Aspen dungeon rewards

# This is based in the fact that we complete monthly quests, wishing coin heroic miracle
# PO = prophet orb
# HS = heroic scroll
# SWC = super wishing coin
# WC = wishing coin
# AT = arena ticket

import tavern_profit

marauder_odds = 0.2
marauder_reward = 320
marauder_friends = 80


class GetResources(object):

    def __init__(self, cards, vip, tavern_strat, cel_gem_mine_number, cel_gem_mine_level):
        if vip == 0:
            vip_coin = 0
        elif 0 < vip < 5:
            vip_coin = 1
        elif 5 <= vip < 7:
            vip_coin = 2
        elif 7 <= vip < 9:
            vip_coin = 3
        elif 9 <= vip < 11:
            vip_coin = 4
        elif vip >= 11:
            vip_coin = 5
        else:
            print("Error, Wrong vip level")
            vip_coin = -100
        tav_gems, tav_hs, tav_po, tav_wc = tavern_profit.getAbsoluteRewards(vip, tavern_strat)
        cel_island_gems = (cel_gem_mine_level + 20) * cel_gem_mine_number * 30
        self.gems = 930 + 3000 + (40 * 15 + 160 * 15) + marauder_odds * marauder_reward + marauder_friends * 30 + \
                    cel_island_gems + tav_gems - tavern_profit.getGemRerollCost(vip, tavern_strat)  # Daily login / Advertisements / Daily quest
        self.po = 7 + tav_po  # Events login
        self.hs = 25 + tav_hs  # Events login
        self.swc = 7  # Events login
        self.wc = 60 + (cards > 0.5) * 30 * vip_coin + tav_wc  # Daily quest
        self.at = 150 + 30  # Daily market buy + daily quest
        setattr(self, 'gems', int(getattr(self, 'gems')) + cards * 14800)  # Gems per card
        if cards > 0.5:
            setattr(self, 'gems', int(getattr(self, 'gems')) + vip * 20 * 30)  # Extra gems priviledge card

    def add_militants(self):
        setattr(self, 'gems', int(getattr(self, 'gems')) + 3500)
        setattr(self, 'po', int(getattr(self, 'po')) + 5)
        setattr(self, 'swc', int(getattr(self, 'swc')) + 10)
        setattr(self, 'at', int(getattr(self, 'at')) - 10 - 300)

    def add_tavern(self):
        setattr(self, 'po', int(getattr(self, 'po')) + 20)
        setattr(self, 'hs', int(getattr(self, 'hs')) + 10)
        setattr(self, 'swc', int(getattr(self, 'swc')) + 6)

    def add_fusion(self):
        setattr(self, 'swc', int(getattr(self, 'swc')) + 8)

    def add_summon(self, target):  # Target is: 1 for 100, 2 for 500
        if target == 1:
            setattr(self, 'hs', int(getattr(self, 'hs')) + 20 - 100)
            setattr(self, 'po', int(getattr(self, 'po')) + 6)
        elif target == 2:
            setattr(self, 'hs', int(getattr(self, 'hs')) + 30 - 500)
            setattr(self, 'po', int(getattr(self, 'po')) + 15)

    def add_po(self):
        setattr(self, 'po', int(getattr(self, 'po')) - 80)

    def add_casino(self):
        setattr(self, 'po', int(getattr(self, 'po')) + 8)
        setattr(self, 'swc', int(getattr(self, 'swc')) + 8)
        setattr(self, 'wc', int(getattr(self, 'wc')) - 240)

    def add_miracle(self):
        setattr(self, 'po', int(getattr(self, 'po')) + 10)
        setattr(self, 'hs', int(getattr(self, 'hs')) + 24)

    def add_campaign(self, target, value):  # Decide what to buy with 2.5k. Target: "po", "hs", Value: integer
        setattr(self, target, int(getattr(self, target)) + value)

    def show_resources(self):
        return self.gems, self.hs, self.po, self.swc, self.wc, self.at

    def roll_casinochips(self):
        chips = getattr(self, "swc")
        setattr(self, 'po', int(getattr(self, 'po')) + chips * 0.085)
        setattr(self, 'hs', int(getattr(self, 'hs')) + chips * 0.165)
        setattr(self, 'swc', 0)
