# Write a program that asks the user how many items
# they want to buy, and multiply that with a fixed price
# we want to get the total cost for all items


# number_of_items = int(input("How many items would you like to buy?")) # this reads a string
#
# item_cost = 11.23
#
# total = number_of_items * item_cost
#
# print(total)












# write a program that asks for the speed of a car at a specific moment
# If the car is going more than 100km/h
# they will get a speeding ticket check the speed from the input and let the user know
# if they will get a speeding ticket or not

speed = float(input("Input your current speed"))

# "100" text
# vs
# 100.0 number

if speed >= 100:
    print("you are going too fast, you will get a speeding ticket")
else:
    print("Keep driving safe, good job!")
