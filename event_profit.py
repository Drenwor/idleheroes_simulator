# Author: Drenwor S574
# Idle Heroes Event Simulator V0.1


def get_profit_hs(gemValues):

    hs_reward = gemValues.hs_odds[0] * gemValues.shard3 + gemValues.hs_odds[1] * gemValues.shard4 + gemValues.hs_odds[2] * gemValues.shard5
    hs_reward_event = gemValues.hs_odds_event[0] * gemValues.shard3 + gemValues.hs_odds_event[1] * gemValues.shard4 + gemValues.hs_odds_event[2] * gemValues.shard5  # Still need to add the event rewards

    profit_hs = hs_reward - gemValues.hs_cost
    profit_hs_event = hs_reward_event - gemValues.hs_cost
    return profit_hs, profit_hs_event


def get_profit_coin(gemValues):
    coin_reward = 10 / 8000 * gemValues.shard5 + (0.34 * gemValues.coin_gold_total[gemValues.coin_level_step]) / gemValues.gold + 0.02 * gemValues.shard4 + 0.001 * gemValues.shard5  # + 0.169 * dust + 0.13 * artifact
    coin_reward_event = (10 * 10) / (8 * 8000) * gemValues.shard5 + (
                8 * gemValues.po_cost + 8 * gemValues.supercoin_cost + gemValues.shard5 + gemValues.feather_cost * 5) / 240 + (0.34 * gemValues.coin_gold_total[
        gemValues.coin_level_step]) / gemValues.gold + 0.02 * gemValues.shard4 + 0.001 * gemValues.shard5  # + 0.169 * dust + 0.13 * artifact

    profit_coin = coin_reward - gemValues.coin_cost
    profit_coin_event = coin_reward_event - gemValues.coin_cost
    return profit_coin, profit_coin_event