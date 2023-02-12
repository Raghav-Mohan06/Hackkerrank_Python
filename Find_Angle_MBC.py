# importing the module
import math

# taking the input from user
ab = float(input())
bc = float(input())

# finding the distance 
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm

# equalizing the sides 
b = mc
c = bm
a = bc

# where b=c
# finding the angle in radian
angel_b_radian = math.acos(a / (2*b))

# converting the radian to degree
angel_b_degree = int(round((180 * angel_b_radian) / math.pi))

# printing with degree
print(angel_b_degree,'\u00B0',sep='')
