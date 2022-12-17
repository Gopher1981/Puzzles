'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
from random import randint

class Solution:
    def addTwoNumbers(l1, l2):
        print("Input: l1 = ",l1,", l2 = ",l2)
        list1 = list(l1)
        list2 = list(l2)
        list1.reverse()
        list2.reverse()
        l1a = int(''.join(str(e) for e in list1))
        l2a = int(''.join(str(e) for e in list2))
        answer = l1a + l2a
        answerList = [int(x) for x in str(answer)]
        print("Reversing Output: ",answerList)

    def altAddTwoNumbers(l1, l2):
        # print("Input: l1 = ",l1,", l2 = ",l2)
        answer = []
        tmpAnswer = 0
        nextAnswer = 0
        for x in range(max(len(l1), len(l2))):
            try:
                tmpAnswer = l1[x] + l2[x]
            except:
                try:
                    tmpAnswer = l1[x]
                except:
                    tmpAnswer = l2[x]
            tmpAnswer += nextAnswer
            if tmpAnswer > 9:
                nextAnswer = 1
                tmpAnswer -= 10
                answer.insert(0,tmpAnswer)
            elif tmpAnswer <= 9:
                nextAnswer = 0
                answer.insert(0,tmpAnswer)
        if answer[0] == 0:
            del answer[0]
        if nextAnswer == 1:
            answer.insert(0,tmpAnswer)
        print("Alternate Output: ",answer)

l1 = []
l2 = []
i = randint(1, 15)
j = randint(1, 15)
for x in range (i):
    l1.append(randint(0,9))
for x in range (j):
    l2.append(randint(0,9))

Solution.addTwoNumbers(l1,l2)
Solution.altAddTwoNumbers(l1,l2)

# Completed