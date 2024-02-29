#!/usr/bin/python3
"""
Making changes
"""


def make_change(coins, total):
    """
    Return the minimum number of coins needed to make up a given total
    Args:
       coins (list): A list of available coin denominations.
       total (int): The amount that needs to be made.
    Returns:
        int: The minimum number of coins required to make up the total.
    Raises:
        ValueError: If no combination can add up to the total or if there is an
        invalid input type.
    """
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1


if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
