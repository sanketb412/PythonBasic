# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: 
# @Last Modified time: 
# @Title : Print function to print 2 Dimensional Array.
# '''

rows = int(input("Enter how many rows:"))
cols = int(input("Enter how many columns:"))

L = []

for i in range(rows):
    L.append([0]*cols)

print(L)

for i in range(rows):
    for j in range(cols):
        L[i][j] = int(input("Enter the value of row "+str(i+1)+" column "+str(j+1)+":"))

for i in range(rows):
    print(L[i])