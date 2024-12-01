#!/usr/bin/python3

""" Module defining makeChange function.
"""


class CoinChange:

    def __init__(self, coins) -> None:
        """ Constructor
        """
        self.coins = coins
        self.coins_len = len(coins)
        self.current_min = None

    def recursiveSolve(self, total, current, current_length):
        """ Reccursion logic solution.
        """
        if total == 0:
            if (self.current_min is None or current_length < self.current_min)\
                    and current_length > 0:
                self.current_min = current_length
        if current >= self.coins_len or total < 0:
            return

        self.recursiveSolve(
            total - self.coins[current], current, current_length + 1)
        self.recursiveSolve(total, current + 1, current_length)


def makeChange(coins, total):
    """ Solves coin change problem.
    Returns:
            Fewest number of coins needed.
    """
    if total <= 0:
        return 0
    prblm = CoinChange(coins)
    prblm.recursiveSolve(total, 0, 0)

    if prblm.current_min is None:
        return -1
    else:
        return prblm.current_min
