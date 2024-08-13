# Write a program that asks the user how many items
# they want to buy, and multiply that with a fixed price
# we want to get the total cost for all items

item_cost = 10
number_of_items = input("How many items do you want to buy? ")

total_cost = item_cost * number_of_items
print("Total cost is: $", total_cost)

# write a program that asks for the income speed of a car at a specific moment
# If the car is going more than 100km/h during
# they will get a speeding ticket check the speed from the input and let the user know
# if they will get a speeding ticket or not

speed = input("What is your current speed")

if speed >= 100:
    print("You will get a speeding ticket!")
else:
    print("Continue driving safe")