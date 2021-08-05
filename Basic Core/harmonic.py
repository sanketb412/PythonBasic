# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by:
# @Last Modified time:Sanket
# @Title : Displaying nth Harmonic number value
# '''

raw_number = input("Enter Nth value for know harmonic number:- ")

n = int(raw_number)

i = 1
s = 0.0
for i in range(1, n+1):
    s = s + 1/i
print("The",n,"th","Harmonic Value is ",s)