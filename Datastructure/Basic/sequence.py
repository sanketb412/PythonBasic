# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: Sanket
# @Last Modified time: 12:30pm
# @Title : Generate sequence in list and tuple
# '''

values = input("Input sequence of number seprated by comma: ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)