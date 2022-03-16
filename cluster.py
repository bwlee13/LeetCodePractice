from collections import deque
from queue import PriorityQueue

def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    queue = deque([])
    # queue= PriorityQueue()
    maxLength = 0
    currLength = 1
    start = 0
    end = 0
    currSumProc = processingPower[0]
    queue.append(bootingPower[0])
    while end < len(processingPower):
        currBoot = queue[0]
        currPower = currBoot + currSumProc * currLength

        if currPower <= powerMax:
            maxLength = currLength
            end += 1
            currLength += 1
        else:
            currSumProc -= processingPower[start]
            queue.remove(bootingPower[start])
            start += 1
            end +=1

        if end<len(processingPower):
            queue.append(bootingPower[end])
            currSumProc += processingPower[end]
    return maxLength

processingPower = [2,1,4,6,1]
bootingPower = [9,14,8,15,15]
powerMax = 18

# processingPower = [2,1,3,4,5]
# bootingPower = [3,6,1,3,4]
# powerMax = 25

# processingPower = [4, 1, 4, 5, 3]
# bootingPower = [8, 8, 10, 9, 12]
# powerMax = 33

print(findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax))