# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to create a tuple.
# '''

"""
Description:
    created function for as unpack_tuple with argument as x passes through tuple.
Parameter:
    used n1, n2, n3, n4 to store the element after its get unpacked from tuple
Return:
    Returning addition of all individual elements after unpacked from tuple
"""

def unpack_tuple(x):
    n1, n2, n3, n4 = x
    return n1 + n2 + n3 + n4

if __name__ == '__main__':
    tuplex = 4, 8, 3, 2
    print("Basic tuple:-",tuplex)
    print("unpack tuple with addition:-",unpack_tuple(tuplex))