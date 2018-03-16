# Shallow copy

lst1=["red","green"]

lst2=lst1
print("printing list1:",lst1)
print("printing list2:",lst2)

print("memory storage value of list1:", id(lst1))

print("memory storage value of list2:", id(lst2))

lst2=["white","black"]

print("memory location of list2:",id(lst2))

print("values in list2:", lst2)


# Now take two more lists and change the value of second list 1st element to different thing

lt1=["Yello","Voilet"]

lt2=lt1

print("Memory location of list1:",id(lt1))

print("Memory location of list2:", id(lt2))
 
print("values of list1:", lt1)

print("values of list2:", lt2)

# Now let's change the 1st element of lt2
#The explanation is that we didn't assign a new object to colours2.
#We changed colours2 inside or as it is usually called "in-place".
#Both variables "colours1" and "colours2" still point to the same list object. 


lt2[0]="Orange"

print("Memory Location of list1:",id(lt1))
print("Memory Location of list2:",id(lt2))

print("Values in list1:",lt1)
print("Values in list2:",lt2)



#It's possible to completely copy shallow list structures with the slice operator without having any of the side effects, which we have described above:

l1=["a","b","c","d"]
l2=l1[:]
print("Memory location of l1:",id(l1))
print("Memory location of l2:",id(l2))


print("Values in l1", l1)
print("values in l2", l2)

# Now let's create a nested list

c1=[1,2,[3,4]]
c2=c1[:]

print("Values of c1:",c1)
print("Values of c2:",c2)

print("Memory location of c1:",id(c1))
print("Memory location of c2:",id(c2))

# Now let's change the sublist
c2[0]=16
c2[2][0]=9
print("Memory location of c1[2][0]:",id(c1[2][0]))
print("Memory location of c2[2][0]:",id(c2[2][0]))

print("Values in c1:",c1)ex
print("Values in c2:",c2)

#A solution to the described problems provide the module "copy".
#This module provides the method "deepcopy", which allows a complete or deep copy of an arbitrary list, i.e. shallow and other lists.

from copy import deepcopy

d1=["a","b",["ab","bc"]]
d2=deepcopy(d1)

print("Memory location of d1:",id(d1))

print("Memory location of d2:",id(d2))

print("Values in d1:",d1)

print("Values in d2:",d2)


# Now let's change some elements in the list

d1[0]=92

d2[2][1]="XZ"

print("Memory location of d1:",id(d1))

print("Memory location of d2:",id(d2))

print("Values in d1 after changes:",d1)
print("Values in d2 after changes:",d2)





