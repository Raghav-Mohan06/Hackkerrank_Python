import math
import os
import random
import re
import sys

# Complete the time_delta function below.
# importing the datetime function
from datetime import datetime
def time_delta(t1, t2):
    a=datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    b=datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    
    return str(int(abs((a-b).total_seconds())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
