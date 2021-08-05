# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: 2021-05-08
# @Last Modified time:Sanket
# @Title : taken user input and display it
# '''

import re

username = input("Enter User Name: ")

regex_name = re.compile(r'^([A-Z][a-zA-Z]{2,})$')
res = regex_name.search(username)

if res:
    print("Hello " + username + ", How are you?")
else:
    print("Please Enter Valid Name with first letter Capital and minimum 3 character")