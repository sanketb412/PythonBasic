# ''""
# @Author: Sanket Bagde
# @Date: 2021-08-08
# @Last Modified by:
# @Last Modified time:
# @Title : write a program to concatinate the element inside of a string
# '''

def concatenate_list(list):
    output= ''
    for element in list:
        output += str(element)
    return output

print(concatenate_list([7, 0, 11, 222]))