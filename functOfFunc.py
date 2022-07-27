#!/usr/bin/python3


my_list = range(3, 15)

def oddStatus(num):
    status = False
    if num % 2 != 0:
        status = True
    return status

def funcOfFunc(oddStatus, my_list):
    new_list = []
    for i in my_list:
        if oddStatus(i) == True:
            new_list.append(i)
    return new_list

oddNumbers = funcOfFunc(oddStatus, my_list)
print(oddNumbers)

