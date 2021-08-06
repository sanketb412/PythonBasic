# ''""
# @Author: Sanket Bagde
# @Date: 2021-05-08
# @Last Modified by: Sanket
# @Last Modified time: 12:37pm
# @Title : Percentage of wining Head and tail
# '''

import random

total_heads = 0
total_tails = 0
count = 0
number = 0

number = int(input("Enter number of coin toss:- "))

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

print("\nFlipped heads by", (total_heads / number) * 100, "%" )
print("and Flipped tails", (total_tails / number) * 100, "%")
