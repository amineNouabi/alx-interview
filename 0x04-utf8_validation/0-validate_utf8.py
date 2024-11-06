#!/usr/bin/python3

"""
UTF-8 Validation
"""

from typing import List


def validUTF8(data: List[int]):
    """validate utf-8 encoding"""
    n = len(data)
    if n == 1:
        return not ((data[0] | 128) >> 7)
    if n > 4:
        return False

    i = 1
    operand = 0b10000000
    while operand & i < n * 8:
        if not operand & data[i // 8]:
            return False
        operand = operand >> 1
        i += 1
