# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by:
# @Last Modified time:Saket
# @Title : taken user input and display it
# '''

import random

total_heads = 0
total_tails = 0
count = 0
number = 0

raw_number = input("Enter number of coin toss:- \n")

number = int(raw_number)
while count < number:

    coin = random.randint(1, 2)

    if coin == 1:
        print("Heads!")
        total_heads += 1
        count += 1

    elif coin == 2:
        print("Tails!")
        total_tails += 1
        count += 1

head_percentage = (total_heads / number) * 100
tail_percentage = (total_tails / number) * 100

print("\nFlipped heads by", head_percentage, "%" )
print("and Flipped tails", tail_percentage, "%")
