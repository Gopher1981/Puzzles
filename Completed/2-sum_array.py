"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from random import randint

class Solution():
    def sumArrays(list1):
        answer = []
        subTotal = 1
        for x in range(len(list1)):
            subTotal = 1
            for y in range(len(list1)):
                if y == x:
                    continue
                else:
                    subTotal *= list1[y]
            answer.append(subTotal)
        print("input: ",list1)
        print("Output: ", answer)



listLength = randint(3,6)
list1 = []
for x in range(listLength):
    list1.append(randint(1,9))

# list1 = [3,2,1]

Solution.sumArrays(list1)

# Complete