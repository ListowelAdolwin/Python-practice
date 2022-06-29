# import list

# Lists in python are used to store a group of items, different or same type
# List can be modified(Add new values, remove values are others)
# The list module contains many methods which can be used to perform operations
# e.g
# 1. append(): Adds a new member to the list
# 2. remove(): Removes a member from the list
# 3. clear(): Clears the list
# 4. sort(): Sorts the list(in ascending order)
# and many others
# Lists are defined in square braces


numbers = [3, 5, 3, 6, 6, 21, "Hey"]
print("Numbers printed")
print(f"{numbers}\n")

numbers.append(34) # This appends 34 to the list
print("34 appended to numbers")
print(f"{numbers}\n")

numbers.remove(21) # Remove 21 from the list
print("21 removed from numbers")
print(f"{numbers}\n")

numbers.insert(2, 25) # Insert 25 at index 2
print("25 inserted at index 2 of numbers")
print(f"{numbers}\n")

numbers.sort() # Sorts the numbers in ascending order
print("Numbers sorted")
print(f"{numbers}\n")

numbers.reverse() # Reverses the order of the numbers
print("Numbers reversed")
print(numbers)
