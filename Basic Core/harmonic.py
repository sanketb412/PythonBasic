# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: Sanket
# @Last Modified time:  12:30pm
# @Title : Displaying nth Harmonic number value
# '''

n_value = int(input("Enter Nth value for know harmonic number:- "))

i = 1
s = 0.0
for i in range(1, n_value+1):
    s = s + 1/i
    print("The",n_value,"th","Harmonic Value is ",s)
