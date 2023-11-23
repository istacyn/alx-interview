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
    arr = [float("inf")] * (total + 1)

    arr[0] = 0

    for coin in coins:
        for value in range(coin, total + 1):
            arr[value] = min(arr[value], arr[value - coin] + 1)

    return arr[total] if arr[total] < float("inf") else -1
