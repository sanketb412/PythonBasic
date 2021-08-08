# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: Sanket
# @Last Modified time: 12:30pm
# @Title : Write a Python program to print the calendar of a given month and year.
# '''

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))