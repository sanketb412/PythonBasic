# ''""
# @Author: Sanket Bagde
# @Date: 2021-08-08
# @Last Modified by:
# @Last Modified time:
# @Title : Write a Python program to print the calendar of a given month and year.
# '''

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))