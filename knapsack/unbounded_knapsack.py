# -*- coding: utf-8 -*-


class Item(object):
    def __init__(self, value, weigth):
        self.value = value
        self.weigth = weigth


class KnapsackBag(object):
    # for a capacity of '0' we have a max value of 0
    value_for_capacity = [0]
    capacity = 0
    available_items = []

    def __init__(self, capacity, items):
        self.capacity = capacity
        self.available_items = items
        default_value = -10000
        for cap in xrange(capacity+1):
            self.value_for_capacity.insert(cap, default_value)

    def fit_items(self):
        for cap in xrange(1, self.capacity+1):
            for item in self.available_items:
                # check each item It it fits, it sits.
                # if there is another with better value, replace it
                if self.value_for_capacity[cap - item.weigth] < 0:
                    self.value_for_capacity[cap - item.weigth] = 0

                print cap, self.value_for_capacity[cap - item.weigth] + item.value
                if item.weigth <= cap and \
                        self.value_for_capacity[cap-item.weigth]+item.value > self.value_for_capacity[cap]:

                    self.value_for_capacity[cap] = \
                        self.value_for_capacity[cap - item.weigth] + item.value
        return self.value_for_capacity[self.capacity]


bag = KnapsackBag(
    5,
    [
        Item(value=1, weigth=3),
        Item(value=2, weigth=2),
        Item(value=3, weigth=4),
    ]
)