a = "apple"
b = "banana"
c = "cherry"


basket_of_fruit_2 = ["apple","banana", "cherry"]
                        # 0,   1         ,2
                        #-3     -2        -1

















# Creating a list
fruits = ['apple', 'banana', 'cherry']

# Accessing elements
# print(fruits[0])  # Outputs 'apple'
# print(fruits[-1])  # Outputs 'cherry' (last item)

# Slicing a list
sublist = fruits[1:3]  # Includes index 1 and excludes index 3

minilist = fruits[1:2]

# print(sublist)  # Outputs ['banana', 'cherry']
# print(minilist)

# lists of different items

number_list = [1,23,42,1236, 21,23]
mixed_list = ["apples",23,231.1,True]
list_list = [[1,23,2],[31,56,0]]
            #    0       1

print(list_list[0][1])




# Modifying an element
fruits[0] = 'blueberry'
print(fruits)  # Outputs ['blueberry', 'banana', 'cherry']

# Adding elements
fruits.append('orange')  # Adds to the end
print(fruits)  # Outputs ['blueberry', 'banana', 'cherry', 'orange']

# Inserting at a specific position
fruits.insert(1, 'kiwi')  # Inserts 'kiwi' at index 1
print(fruits)  # Outputs ['blueberry', 'kiwi', 'banana', 'cherry', 'orange']


# Removing by value
fruits.remove('banana')  # Removes the first occurrence of 'banana'
print(fruits)  # Outputs ['blueberry', 'kiwi', 'cherry', 'orange']
                        #   0             1       2         3

# Removing by index with pop
popped_fruit = fruits.pop(1)  # Pops element at index 1
print(popped_fruit)  # Outputs 'kiwi'
print(fruits)  # Outputs ['blueberry', 'cherry', 'orange']

# Using del to remove an element
del fruits[1]  # Removes the element at index 1
print(fruits)  # Outputs ['blueberry', 'orange']








# ask the user the



# write a python program that asks