# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to append a list to the second list.
# '''

"""
Description:
    created function for as append_list.
Parameter:
    declare two list "list1" and "List2" and in list2 append the list1 with append method call.
Return:
    Returning the list2 value through print statement.
"""

def append_list():
    list1 = [2,4,6,8,10]
    print("first Lists:-",list1)
    list2 = [4,5,7,4,2]
    list2.append(list1)
    print("First list append with second list:-", list2)

if __name__ == '__main__':
    append_list()
