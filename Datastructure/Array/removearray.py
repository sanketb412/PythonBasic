# ''""
# @Author: Sanket Bagde
# @Date: 2021-08-08
# @Last Modified by:
# @Last Modified time:
# @Title : Write a Python program to remove the first occurrence of a specified element from an array.
# '''

from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: ",str(array_num))
print("Remove the first occurrence of 3 from the said array:")
array_num.remove(7)
print("New array: ",str(array_num))