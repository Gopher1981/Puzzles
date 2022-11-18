# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint

class Solution:
    def addTwoNumbers(l1, l2):
        print("Input: l1 = ",l1,", l2 = ",l2)
        l1.reverse()
        l2.reverse()
        l1a = int(''.join(str(e) for e in l1))
        l2a = int(''.join(str(e) for e in l2))
        answer = l1a + l2a
        print("Output: ",answer)

l1 = []
l2 = []
i = randint(1, 15)
j = randint(1, 15)
for x in range (i):
    l1.append(randint(0,9))
for x in range (j):
    l2.append(randint(0,9))

Solution.addTwoNumbers(l1,l2)