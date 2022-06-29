# Dictionaries are user defined data types that takes multiple variables
# Members of a dictionary are called keys
# A dictionary can contain keys of different datatypes
# Dictionary keys are separated by commas
# Dictionaries are like structures in C

# Defining a dictionary
Student = {
        "Name" : "Listowel",
        "Program" : "Computer Science",
        "Number" : "12345",
        "Age" : "31"
        }

# Printing keys of the dictionary
print(Student["Name"])
print(Student["Age"])
Student["Course"] = "Python" # Adding a new key to the dictionary
print(Student["Course"])
