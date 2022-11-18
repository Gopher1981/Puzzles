"""
from a random list. Check if two seperate numbers
make the sum of another number
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