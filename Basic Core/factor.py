# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: Sanket
# @Last Modified time: 12:30pm
# @Title : Display the Factor of a Input Number
# '''

import math
n_value = int(input("Enter N value:- "))

while n_value % 2 == 0:
    print (2),
    n_value = n_value / 2

for i in range(3,int(math.sqrt(n_value))+1,2):
    while n_value % i == 0:
        print (i),
        n_value = n_value / i
