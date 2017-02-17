# -*- coding: utf-8 -*-


class PoketChange(object):
    coins = [1, 3, 5, 10]
    sum = None
    min_number_of_coins = []
    default_value = 100000

    def __init__(self, s):
        self.sum = s
        # plus one because we want to allocate the 0 postition
        for s in range(self.sum+1):
            self.min_number_of_coins.insert(s, self.default_value)
        # for 0 moneys, we have to give 0 coins
        self.min_number_of_coins[0] = 0

    def get_change(self):
        """
        Set Min[i] equal to Infinity for all of i
        Min[0]=0

        For i = 1 to S
            For j = 0 to N - 1
                If (Vj<=i AND Min[i-Vj]+1<Min[i])
                Then Min[i]=Min[i-Vj]+1

        Output Min[S]

        """
        for current_sum in range(1, self.sum+1):
            for coin in self.coins:
                if coin <= current_sum and \
                        self.min_number_of_coins[current_sum-coin] < self.min_number_of_coins[current_sum]:
                    self.min_number_of_coins[current_sum] = \
                    self.min_number_of_coins[current_sum - coin] + 1

        if self.min_number_of_coins[self.sum] == self.default_value:
            return "No change"
        else:
            return self.min_number_of_coins[self.sum]