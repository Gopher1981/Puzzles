"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""


from random import randint


class solution:
    def isSumToK(numList,k):
        numList.sort()
        size = len(numList)
        done = False
        print("List is : ", numList)
        print("Trying to find : ", k)
        for x in range(0, size - 1):
            for y in range(x + 1, size):
                if (numList[x] + numList[y] == k):
                    print(numList[x]," + ",numList[y]," = ",k)
                    done = True
        if done == False:
            print("No matches found")
            
nums = []
for x in range (randint(4,10)):
    nums.append(randint(1,20))
k = randint(8,30)

solution.isSumToK(nums,k)

# Complete