#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s.find("PM")!= -1:
        hour = int(s[0:2])
        if hour==12:
            return str(hour) + s[2:8]
        hour += 12
        return str(hour) +  s[2:8]
    
    elif s.find("AM")!= -1:
        hour = int(s[0:2])
        if hour == 12:
            hour-= 12
            return "0" +str(hour) +  s[2:8]
        else:
            return "0" +str(hour) +  s[2:8]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
