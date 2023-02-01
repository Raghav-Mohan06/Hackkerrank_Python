# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
N, M = map(int, input().split()) 
for i in range(0,math.floor(N/2)): 
    s='.|.'*i
    print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))
print ('WELCOME'.center(M,'-'))
for i in reversed(range(0,math.floor(N/2))): 
    s='.|.'*i
    print (s.rjust(math.floor((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(math.floor((M-2)/2),'-'))
