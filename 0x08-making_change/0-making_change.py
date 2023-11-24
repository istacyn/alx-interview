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
    @coins (list of int): Available coin denominations.
    @total (int): Desired total amount to be reached.

    Returns:
    - int: Fewest number of coins needed to meet the total amount.
           or -1 if total cannot be met by any combination of available coins.
    """
    """if total <= 0:
        return 0

    arr = [float('inf')] * (total + 1)
    arr[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            arr[i] = min(arr[i], arr[i - coin] + 1)

    return arr[total] if arr[total] != float('inf') else -1"""

    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
