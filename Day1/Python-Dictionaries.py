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

# The update method update() merges the keys and values of one dictionary into another, overwriting values of the same key


#Iterating over dictionaries

d6= {"TS":"TELANGANA","AP":"ANDHRA","TN":"CHENNAI","KL":"KERALA","KA":"KARNATAKA"}

# No method is required to iterate over dictionay keys
for key in d6:
    print(key)
    
# But it's possible to use method keys() and we will get the same result.

for key in d6.keys():
    print(key)
    
# We can use values() method to itterate over values

for value in d6.values():
    print(value)
    
    
# Python converts dictoinaries into list with two tuples.

# For instance

d9 = {"AP":"ANDHRA", "TS":"TELANGANA"}

item_views=d9.items() 
items=list(item_views)
print(items)
# Result is [('AP', 'ANDHRA'), ('TS', 'TELANGANA')]

# Similarly we can use method keys() and values() to create a list only with keys and values.

keys_values=d9.keys()
keys=list(keys_values)
print(keys)

# Result is ['AP', 'TS']

values_view=d9.values()
value=list(values_view)
print(value)

# Result is ['ANDHRA', 'TELANGANA']

print(values_view)

print(keys_values)

print(item_views)

# Turning lists into Dictionaries

bf=["Idly", "dosa", "upma"]

bf_days=["Mon","Tue","Wed","Thur","Fri"]

print(dict(zip(bf,bf_days)))

# Result will be {'Idly': 'Mon', 'dosa': 'Tue', 'upma': 'Wed'}

# Please check the topic converting list to dictionaries one more time.





