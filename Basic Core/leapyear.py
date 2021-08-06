# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: Sanket
# @Last Modified time: 12:40pm
# @Title : Checking year as a leap year or not
# '''

print("---checking leap year or not---")
year = int(input("Enter Year to check:- "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,"is a Leap year")

else:
    print(year,"is not a leap year")