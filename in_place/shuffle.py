# -*- coding: utf-8 -*-
import random


def shuffle_list(the_list):
    """
    The shuffle must be "uniform," meaning each item in the original list
    must have the same probability of ending up in each spot in the final list.

    :param the_list: a list of integers
    :type the_list: list
    :return: the same list, shuffled
    :rtype: list
    """
    shuffled = len(the_list)
    while shuffled > 0:
        index_to_shuffle = random.randrange(0, shuffled)
        the_list.append(the_list.pop(index_to_shuffle))
        shuffled -= 1
    return the_list
