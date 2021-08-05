# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by:
# @Last Modified time:Sanket
# @Title : Display the Factor of a Input Number
# '''
import math
raw_number = input("Enter N value:- ")

n = int(raw_number)

while n % 2 == 0:
    print (2),
    n = n / 2

for i in range(3,int(math.sqrt(n))+1,2):
    while n % i == 0:
        print (i),
        n = n / i
