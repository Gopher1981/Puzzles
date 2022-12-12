"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


class Solution():
    def lowestMissedInt(array):
        for x in range(len(array)+1):
            if x in array:
                continue
            elif x > 0:
                print("Input: ",array)
                print("Answer: ",x)
                return

from random import randint
array = []
for i in range(randint(1,20)):
    array.append(randint(-9,9))

# array = [-1, -2, 0, -3, -2, 3, 4]

Solution.lowestMissedInt(array)

# Completed