# -*- coding: utf-8 -*-


class Elementary(object):
    sequence_a = []
    non_decreacing_sequence = []

    def __init__(self, sequence):
        """

        :param sequence: an iterable of ints
        :type sequence: list
        """
        self.sequence_a = sequence

    def get_non_decreasing_length(self):
        length = 1
        biggest_until_now = 1
        for index, elem in enumerate(self.sequence_a):

            if index == 0:
                # For the first index, it is already the longest sequence
                continue
            else:
                last_value = self.sequence_a[index-1]

            print length
            if last_value <= elem:
                length += 1
            else:
                # A decrease in the sequence
                if length > biggest_until_now:
                    biggest_until_now = length
                    length = 1
        return biggest_until_now
