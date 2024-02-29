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
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1

    coins.sort(reverse=True)
    coin_count = 0
    for i in coins:
        if total % i == 0:
            coin_count += int(total / i)
            return coin_count
        if total - i >= 0:
            if int(total / i) > 1:
                coin_count += int(total / i)
                total = total % i
            else:
                coin_count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
