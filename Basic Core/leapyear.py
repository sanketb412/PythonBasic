# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by:
# @Last Modified time:Sanket
# @Title : Checking year as a leap year or not
# '''

print("---checking leap year or not---")
raw_year = input("Enter Year to check:- ")

year = int(raw_year)

a = year % 4
b = year % 100
c = year % 400

if a == 0 and b != 0 or c == 0:
    print(year,"is a Leap year")

else:
    print(year,"is not a leap year")