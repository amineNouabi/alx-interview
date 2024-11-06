#!/usr/bin/python3
"""

Module defining NQueens Class

"""


class NQueens:
    """
        Class that solves NQueens Problem.
    """

    def __init__(self, N):
        self.__N = N
        self.solutions = []

    def safe_position(self, position, board):
        """Determines if a position is safe to place a queen.

        Args:
            position (list): x, y coordinates of the position to check.
            board (list): Previously played queens.

        Returns:
            True or False if the position is safe to place a queen.
        """
        [x, y] = position

        # Filter outside the board case
        if x >= self.__N or y >= self.__N or x < 0 or y < 0:
            return False

        # Filter Queen Attacked by previously played queens.
        for queen in board:
            [queen_x, queen_y] = queen

            # Attaking queen straight
            if queen_x == x or queen_y == y:
                return False

            # Attacking in diagonal or taken position
            if (queen_x - queen_y == x - y) or (queen_x + queen_y == x + y):
                return False

        # Safe Position
        return True

    def backtrack(self, board, column):
        """Backtracking algorithm to solve the NQueens problem."""

        if column == self.__N:
            self.solutions.append(board.copy())
            return True

        for row in range(self.__N):
            position = [column, row]
            if self.safe_position(position, board):
                board.append(position)
                self.backtrack(board, column + 1)
                board.pop()

        return False

    def solve(self):
        """Solves the NQueens problem."""
        board = []
        self.backtrack(board, 0)
        for solution in self.solutions:
            print(solution)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    NQueens(N).solve()
    del NQueens
