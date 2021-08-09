# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to remove duplicates from a list.
# '''


"""
Description:
    created function for as duplicates_of_list.
Parameter:
    declare list of elements in nums and passes it through the dict to form keys and convert it to list again 
Return:
    Returning the value of list without duplicates elements through print statement.
"""

def duplicates_of_list():
    nums = [2,4,6,8,10,10,6,2]
    
    print("Lists:-",nums)
    mylist = list(dict.fromkeys(nums))
    print("Duplicates remove:-",mylist)      
        
if __name__ == '__main__':
    duplicates_of_list()
