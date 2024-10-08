#!/usr/bin/python3

"""

Solution for lock boxes problem

"""


def unlock(boxes, openedBoxes, currentIndex):
    """ Recursive unlocking of boxes """
    if currentIndex < 0 or currentIndex >= len(boxes) \
            or openedBoxes[currentIndex]:
        return

    openedBoxes[currentIndex] = True
    for boxIndex in boxes[currentIndex]:
        unlock(boxes, openedBoxes, boxIndex)


def canUnlockAll(boxes):
    """ Returns True if can open all boxes """
    openedBoxes = [False] * len(boxes)

    unlock(boxes, openedBoxes, 0)

    for opened in openedBoxes:
        if not opened:
            return False
    return True
