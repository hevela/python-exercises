# -*- coding: utf-8 -*-
import sys


class Strct(object):
    j = 0
    i = 0
    sum = 0


def kadane():
    arr = [-1, -2, 3, 4, -5, 6]

    max_curr = Strct()
    max_ = Strct()
    result = Strct()

    max_curr.sum = -sys.maxint - 1
    max_.sum = -sys.maxint - 1
    result.i = 0
    result.j = 0

    for index, element in enumerate(arr):
        if max_curr.sum < 0:
            max_curr.sum = arr[index]
            max_curr.i = index
            max_curr.j = index
        else:
            max_curr.sum += arr[index]
            max_curr.j = index

        if max_curr.sum > max_.sum:
            max_.sum = max_curr.sum
            max_.i = max_curr.i
            max_.j = max_curr.j
    print(max_.sum, arr[max_.i:max_.j+1], max_.i, max_.j)


def parentesis(strng):
    cont = 0
    for index, char in enumerate(strng):
        if char == '(':
            cont += 1
        elif char == ')':
            cont -= 1
    if cont == 0:
        return True
    return False


def match_p(strng):
    dct = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    left = dct.keys()
    right = dct.values()
    arr = []
    for ch in strng:
        if ch in left:
            arr.append(ch)
        elif ch in right:
            if arr:
                popped = arr.pop()
                if ch != dct[popped]:
                    return False
    return True if not arr else False


def is_palindrome(strng):
    strng = strng.replace(' ', '')
    reverse_strng = strng[::-1]
    if strng == reverse_strng:
        return True
    return False


def compute_palindromes(words):
    results = []
    for word in words:
        letters = dict()
        for letter in word:
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 1
        odd_char = 0
        for char_count in letters.values():
            #odd count of chars

            if char_count % 2:
                odd_char += 1
        if odd_char > 1:
            results.append(-1)
        else:
            left = []
            middle = ''

            for letter, count in letters.iteritems():
                # middle letter
                if count % 2:
                    middle = letter * count
                else:
                    left.append(letter * (count/2))
                pal = left + list(middle) + left[::-1]
            else:
                results.append(''.join(pal))
    return results