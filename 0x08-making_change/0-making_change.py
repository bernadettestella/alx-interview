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
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    count = 0
    for c in coins:
        if total % c == 0:
            count += int(total / c)
            return count
        if total > c >= 0:
            if int(total / c) > 1:
                count += int(total / c)
                total = total % c
            else:
                count += 1
                total -= c
                if total == 0:
                    break
    if total > 0:
        return -1
    return count
