# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to reverse a tuple.
# '''


def reverse_tuple(x):
    return x[::-1]

if __name__ == '__main__':
    tuplex ='First', 4, 8, True, 3, 2, 'Last'
    print("Basic Tuple:-",tuplex)
    print("Reverse Tuple:-",reverse_tuple(tuplex))