# ''""
# @Author: Sanket Bagde
# @Date: 2021-06-08
# @Last Modified by: 
# @Last Modified time: 
# @Title : Print Distance between two points provided by User.
# '''

import math

def point_distance(i, j):
    return math.sqrt((i*i) + (j*j))

x = int(input("Enter x-cordinate:- "))
y = int(input("Enter y-cordinate:- "))

print("Euclidean distance is:-",point_distance(x, y))