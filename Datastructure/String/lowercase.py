# ''""
# @Author: Sanket Bagde
# @Date: 2021-09-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python program to lowercase first n characters in a string
# '''

str1 = 'BRIDGELABZ'
print(str1)
n = int(input("Enter n value upto which Upper case has to update:-"))
print(str1[:n].lower() + str1[n:])