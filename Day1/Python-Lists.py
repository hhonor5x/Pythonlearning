#Python Lists

# A list is an ordered group of elements or items, it's important to notice that these list elements don't have to be of same data type.

##For example
##
##1. [] --> empty list
##2. ["a","bc","cd"] --> A list of strings
##3. [1,2,3,4] --> A list of integers
##4. [1,"a","bcd",3.14] --> A list of mixed data types
##5. [1,2,[3,4,5],6] --> nested list


lst1 = [ 1,2,3,4,5 ]

print(len(lst1))

print( 1 in lst1)

print ( 6 not in lst1)

# Lists concatenation ( vibgyor)

colors1 = ["viloet", "indigo", "blue", "green"]
colors2 = ["yello", "orange","red"]

rainbow= colors1+colors2
print(rainbow)


# Repetetion

print(rainbow*3)