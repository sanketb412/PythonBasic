# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to sum all the items in a list..
# '''


"""
Description:
    created function for as sum_of_list.
Parameter:
    declare total as 0 initially and assign values to the num in form of list.
Return:
    Returning the value of total through print statement.
"""

def sum_of_list():
    total = 0
    nums = [2,4,6,8,10]
    print("Lists:-",nums)
    for x in range(0, len(nums)):
        total = total + nums[x]
    print("Sum of the elements in the list is:- ", total)

if __name__ == '__main__':
    sum_of_list()


