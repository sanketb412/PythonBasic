# ''""
# @Author: Sanket Bagde
# @Date: 2021-06-08
# @Last Modified by: 
# @Last Modified time: 
# @Title : Print sum of 3 integer.
# '''

L = []

def findTriplets(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i],arr[j],arr[k])
                    found = True

    if (found == False):
        print("Triplet does not exits")


N = int(input("Enter number of elements to br entered: "))

for i in range(N):
    L.append([0]*N)

for i in range(N):
    L[i]  = int(input("Enter number of elements for array: "))

n = len(L)
findTriplets(L, n)