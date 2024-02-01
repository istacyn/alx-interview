#!/usr/bin/python3
"""
Determines the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet
    a given total amount using available coin denominations.

    Args:
        coins: Available coin denominations.
        total: Total amount to be reached.

    Returns:
        Fewest number of coins needed to meet total.
        If total is 0 or less - 0
        If total cannot be met by any number of coins - -1
    """

    if total <= 0:
        return 0
    
    coins.sort(reverse=True)

    change = 0

    for coin in coins:
        if total <= 0:
            break
        num_coins = total
        change += num_coins
        total -= (num_coins * coin)

    if total != 0:
        return -1

    return change
