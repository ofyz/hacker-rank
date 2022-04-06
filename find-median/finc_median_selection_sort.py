#!/bin/python3

import math
import os
import random
import re
import sys


def findMedian(arr):
    for i in range(len(arr)):
      
       
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                  
             
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr[int(len(arr)/2)]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
