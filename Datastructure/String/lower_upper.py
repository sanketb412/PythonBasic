# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python script that takes input from the user and displays that input back in lower and uppercase.
# '''

def case(str2):
    low = str2.lower()
    upper = str2.upper()
    return low, upper

if __name__ == '__main__':
    str1 = input("Enter any String to get lower case and upper cacse:- ")
    print(case(str1))