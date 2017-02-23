# -*- coding: utf-8 -*-


def is_riffle_shuffled(half1, half2, shuffled_deck):
    """ function to tell us if a full deck of cards shuffled_deck is a
    single riffle of two other halves half1 and half2.

    :param half1: an array of numbers (card)
    :type half1: list
    :param half2: an array of numbers (card)
    :type half2: list
    :param shuffled_deck: The shulffled deck form half 1 and 2
    :type shuffled_deck: list
    :return: a boolean indicating if the shuffled_deck is a single riffle
    :rtype: bool
    """
    index_half1 = 0
    index_half2 = 0
    len1 = len(half1)
    len2 = len(half2)
    if len1 + len2 != len(shuffled_deck):
        return False
    for elem in shuffled_deck:
        if index_half1 < len1 and half1[index_half1] == elem:
            index_half1 += 1
        elif index_half2 < len2 and half2[index_half2] == elem:
            index_half2 += 1
        else:
            return False
    return True
