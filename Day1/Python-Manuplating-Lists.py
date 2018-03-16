##append will insert element at the end of the list

lst1=["a",'b','c','d']
lst1.append('e')
print(lst1)

##pop will remove an element from the list, if we are not giving any value in pop by default the last value will be removed

lst1.pop(0)
print(lst1)


##We saw that it is easy to append an object to a list. But what about adding more than one element to a list?
##Maybe, you want to add all the elements of another list to your list.
##If you use append, the other list will be appended as a sublist, as we can see in the following example

lst2=[44,45,56]
#lst1.append(lst2)
#print(lst1)

# Result will be ['b', 'c', 'd', 'e', [44, 45, 56]]

lst1.extend(lst2)
print(lst1)

str1="This is programming python"

lst2.extend(str1)
print(lst2)

tup1=("java", "php", "python")
lst2.extend(tup1)
print(lst2)


##+ is an alternative to append and extend

lst3=[1,2,3,4]

print(lst3+lst2)

##It is possible to remove with the method remove a certian value from a list without knowing the position

lst4=["red", "green","red","white","red"]
lst4.remove("red")
print(lst4)


print(lst4.index("red", 2))

##It is possible to add elements to list at an arbitary position, this can be done by insert
lst5=["we","you","are"]
lst5.insert(2, "yes")
print(lst5)



