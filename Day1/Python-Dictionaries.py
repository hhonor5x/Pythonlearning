# Like list dictionaries can be easily changed, can be shrunk and grown and libitium at run time.
# Dictionaries can be contained in lists and vice versa.
# Difference between lists and dictionaries
# A list is an orderd sequence of objects whereas dictionaies are unordered sets.
# The main difference is that items in dictionaries can be accessed via keys not via their positions.

# Example of a dictionary

city_population={"Mumbai":11978450, "Delhi":9879172 ,"Bangalore":8443675, "Hyderabad":6993262, "Ahmedabad":5577940, "Chennai":4646732}

# If we want to know the population of one of those sities, use city name as index

print(city_population["Chennai"])

city_population["Kolkata"]=4496694

print(city_population)

# It's possible to create a dictionary incrementally by starting with an empty dictionary.
# It can be done by using a empty pair of brackets.

food={}
print(food)

food["ham"]="yes"
food["Cheese"]="yes"
food["Spam"]="no"

print(food)

# We can use arbitary types as values in a dictionay, but there is restriction for the keys.
# Only immutable data types can be used as keys, i.e. No list or dictionaries can be used.
# We can use strings, numbers and tupes as keys in dictionaries.

dic1={(1,2,3): "abc"}

# Operators on Dictionaries

# len(d)
# del d[k]
# k in d
# k not in d

print("Length of dic1:",len(dic1))
print("Id of dic1:",id(dic1))

print(dic1[1,2,3])

del dic1[1,2,3]

print(dic1)

morse = {
"A" : ".-", 
"B" : "-...", 
"C" : "-.-.", 
"D" : "-..", 
"E" : ".", 
"F" : "..-.", 
"G" : "--.", 
"H" : "....", 
"I" : "..", 
"J" : ".---", 
"K" : "-.-", 
"L" : ".-..", 
"M" : "--", 
"N" : "-.", 
"O" : "---", 
"P" : ".--.", 
"Q" : "--.-", 
"R" : ".-.", 
"S" : "...", 
"T" : "-", 
"U" : "..-", 
"V" : "...-", 
"W" : ".--", 
"X" : "-..-", 
"Y" : "-.--", 
"Z" : "--..", 
"0" : "-----", 
"1" : ".----", 
"2" : "..---", 
"3" : "...--", 
"4" : "....-", 
"5" : ".....", 
"6" : "-....", 
"7" : "--...", 
"8" : "---..", 
"9" : "----.", 
"." : ".-.-.-", 
"," : "--..--"
}

print ("a" in morse)

print ("a" not in morse)

# pop() and popitem()

d1={"TS":"Telangana", "AP":"Andhra Pradesh","TN":"Tamil Nadu","KL":"Kerala"}

d2=d1.pop("KL")
print(d2) # It will print Kerala

##d2=d1.pop("AS")
##print(d2) # Will show keyerror

# To prevent keyerrors in dictionaries, there is an elegant way.
# pop() method has an optional second parameter, which can be used as a default value

d2=d1.pop("AS", "None")
print(d2) # This will print the message None

# popitem() is a method of dict, which doesn't take any parameter and removes and returns an arbitrary (key,value) pair as a 2-tuple. If popitem() is applied on an empty dictionary, a KeyError will be raised.

d3={"KA":"KARNATAKA","DL":"DELHI","PY":"PONDICHERY"}


print(d3.popitem())
print(d3.popitem())
print(d3.popitem())

#Accessing non Existing Keys

d5={"TS":"Telangana", "AP":"Andhra Pradesh","TN":"Tamil Nadu","KL":"Kerala"}

if "TS" in d5 : print(d5["TS"])

print(d5.get("AP"))
print(d5.get("HI","No value found"))



# Important Methods

# a Dictionary can be copied with the method copy()
# This copy is a shollow copy not a deep copy.
words={"C":"Cat","A":"Apple", "B":"Bat"}
w=words.copy()
words["D"]="Dog"
print(w)
print(words)

# The conents of a dictionary can be cleated using method clear()
# clear() will not delete, but set to an empty dictionary
print("Before clearing:",id(w))
w.clear()
print("After clearing:",id(w))
print(w)


# Concatenating Dictionaries

lst1=[1,2,3,4]
lst2=[2,3,4,5]

print(lst1+lst2)

lst2.extend(lst1)
print(lst2)






