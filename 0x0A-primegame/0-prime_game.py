#!/usr/bin/python3
""" Module Solving Prime Game.
"""

from math import sqrt, ceil


class PrimeGame:
    """ Class to solve Prime game.
    """

    def __init__(self, x, nums, players):
        """ Initializes the PrimeGame class.
        """
        self.rounds = x
        self.ns = nums
        self.max_n = max(self.ns)
        self.players = players
        self.scores = [0] * len(self.players)
        self.erathsthenes_generate()

    def start_game(self):
        """ Starts the game.
        """
        for i in range(self.rounds):
            turn = 0
            round_primes = self.__isPrime[:self.ns[i] + 1]

            while True:
                picked_prime = False
                for j in range(len(round_primes)):
                    if round_primes[j]:
                        round_primes[j] = False
                        picked_prime = True
                        turn += 1
                        turn %= len(self.players)
                        break
                if not picked_prime:

                    for j in range(len(self.scores)):
                        if j == turn:
                            continue
                        self.scores[j] += 1
                    break

    def erathsthenes_generate(self):
        """ Generates prime numbers using Erathosthenes sieve.
        """
        self.__isPrime = [True] * (self.max_n + 1)
        self.__isPrime[0] = self.__isPrime[1] = False

        i = 2
        end = ceil(sqrt(self.max_n + 1))
        while i <= end:
            if self.__isPrime[i]:
                j = i ** 2
                while j <= self.max_n:
                    self.__isPrime[j] = False
                    j = j + i
            i = i + 1

    def get_winner(self):
        """ Returns the winner of the game.
        """

        max_score = max(self.scores)
        if self.scores.count(max_score) > 1:
            return None
        return self.players[self.scores.index(max_score)]


def isWinner(x, nums):
    """ Determines the winner of the game.
    """
    pg = PrimeGame(x, nums, ['Maria', 'Ben'])
    pg.start_game()
    return pg.get_winner()


if __name__ == '__main__':
    isWinner(3, [4, 5, 1])
