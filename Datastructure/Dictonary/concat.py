# ''""
# @Author: Sanket Bagde
# @Date: 2021-08-08
# @Last Modified by:
# @Last Modified time:
# @Title : Write a Python script to concatenate following dictionaries to create a new dict
# '''

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
    print(dic4)