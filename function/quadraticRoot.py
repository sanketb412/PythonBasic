# ''""
# @Author: Sanket Bagde
# @Date: 2021-06-08
# @Last Modified by: 
# @Last Modified time: 
# @Title : To find roots of a equation a*X*X + b*X + c
# '''

import math

def get_input():
    a = int(input("Enter co-efficient for x^2:- "))
    b = int(input("Enter co-efficient for x:- "))
    c = int(input("Enter constant co-efficient:- "))
    return a, b, c

def root(a, b, c):

    delta = b*b - 4*a*c

    root1_x = (-b + math.sqrt(delta))/(2*a)
    root2_x = (-b - math.sqrt(delta))/(2*a)

    print("The roots of qudratic equation is:- ", root1_x, root2_x)

if __name__ == '__main__':
    a, b, c = get_input()
    root(a, b, c)
    