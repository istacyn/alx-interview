#!/usr/bin/python3
"""
Module for prime game solution
"""


def isWinner(x, nums):
    """
     Determines the winner of a game played by Maria and Ben.
     The game consists of x rounds, where each round is
     defined by a positive integer n in the array nums.

    Maria and Ben take turns choosing a prime number
    from the set of consecutive integers starting from
    1 up to and including n. They then remove that number
    and its multiples from the set.
    The player who cannot make a move loses the round.

    @x: Number of rounds in the game.
    @nums: Array of integers representing different values
            of n for each round.
    return: Name of the player that won the most rounds,
    or None if winner cannot be determined.
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    primes = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            primes[j] = False
    primes[0] = primes[1] = False
    prime_count = 0
    for i in range(len(primes)):
        if primes[i]:
            prime_count += 1
        primes[i] = prime_count

    maria_wins = 0
    for n in nums:
        maria_wins += primes[n] % 2 == 1

    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
