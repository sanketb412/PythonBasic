# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by:
# @Last Modified time:Sanket
# @Title : Power of 2 till N
# '''

raw_range = input("Enter N value:- ")

N = int(raw_range)

if N < 0 or N > 31:
    print("Please enter positive value less then 31")
else:    
    for x in range(N):
	    print(2**x)