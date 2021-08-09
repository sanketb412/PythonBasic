# ''""
# @Author: Sanket Bagde
# @Date: 2021-08-08
# @Last Modified by:
# @Last Modified time:
# @Title : Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes..
# '''

from array import *
array_num = array('i', [5,1,8,3,6,9,7,4])
for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[5])
print(array_num[0])
print(array_num[3])