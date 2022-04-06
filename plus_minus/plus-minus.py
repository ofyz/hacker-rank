import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #n = arr[1]

    zeroCounter=0
    posCounter=0
    negCounter=0
    result = []
    for i in range(0,len(arr)):
        if arr[i]== 0:
            zeroCounter+=1
        elif arr[i] < 0:
            negCounter+=1
        else:
            posCounter+=1
    
    print(posCounter/n)
    print(negCounter/n)
    print(zeroCounter/n)
    
    #return result

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
