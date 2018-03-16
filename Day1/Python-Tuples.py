##Python Tuples
##
##Tuple is an immutable list, i.e. a tuple cannot be changed once it has been created.
##
##Once a tuple is created we can't add or remove elements in the tuple
##
##benfits of tuples
##
##> Tuples are faster than lists.
##> If you know that some data doesn't have to be changed, we can use tuples instead of lists, because this protects your data against accidental changes.
##> The main advantage of tuples consist in fact that tuples can be used as keys in dictonories, while list can't.

tup1 = ("tuples", "are" ,"immutable")
print(tup1[1])

##tup[2] = "Mutable"
##print(tup[2])

print(tup1*3)
print(tup1+tup1)

print(tup1+("thanks", "welcome"))

##tup2 = ()
##tup2[0]="wel"
##print(tup2)
## Result is TypeError: 'tuple' object does not support item assignment
##
##