# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to remove an item from a tuple.
# '''

mytuple = (2, 4, 5, 67, 7, 4)
print("Tuple:-",mytuple)
tempTuple = list(mytuple)
tempTuple.pop(3)
print("Tuple after removing single element:-",tuple(tempTuple))
