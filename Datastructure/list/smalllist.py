# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to get the smallest number from a list.
# '''


"""
Description:
    created function for as mul_of_list.
Parameter:
    declare total=1 initially and assign values to the num in form of list.
Return:
    Returning the value of total through print statement.
"""


def small_of_list():
    nums = [2,4,6,8,0]
    print("Lists:-",nums)
    small_element = min(nums)
    print("Sum of the elements in the list is:- ", small_element)

if __name__ == '__main__':
    small_of_list()
