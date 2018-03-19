str="Python is fun to learn"

x=set(str)

print(x)

print(type(x))

print(type(str))


l1=["Python","Java","Perl","Ruby"]

x=set(l1)
print(type(x))

print(x)

t1=("Chirala", "Manuguru","Khammam", "Hyderabad", "Manuguru")

x=set(t1)
print(x)


# Immutable sets

cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
 
print(cities)

# Sets are implemented in a way, which doesn't allow mutable objects.
# The following example demonstrates that we cannot include for example lists as elements:

##cities = set((["Python","Perl"],["Paris", "Berlin"]))
##print(cities)

# Frozen sets
# Though sets can't contain mutable objects, set are mutable:

cities=set(["Frankfurt","Germany","Berlin"])
print(cities)

cities.add("Russia")
print(cities)


# Frozen sets are like sets except they are immutable

cities=frozenset(["Frankfurt","Germany","Russia"])

##cities.add("Berlin") # Throws an error AttributeError: 'frozenset' object has no attribute 'add'
##print(cities)

# Improved Notation

# Since python 2.6 we can use curly braces for defining sets, instead of built-in function set:

Expression = {'Good','Bad','Ugly','Fair'}
print(Expression)

print(type(Expression))



# Set Operations

# add(element)
##Only immutable elements can be addded to a set

colors = {"red","blue","green"}
colors.add("white")
print(colors)

##colors.add(["Yellow"]) # Results a TypeError: unhashable type: 'list'
##print(colors)

# clear() method

# All elements will be removed from a set

cities = {"Hyd","Chenn","Kera","Bang"}

cities.clear()
print(cities) # result will be set()

# copy() : - Creates a shallow copy which is returned

cities = {"Banglore","Hyderbad","Manglore"}

cities_backup=cities.copy()
print(cities_backup)
cities.clear()
print(cities)
print(cities_backup)


# If we think just assignment was enough for copying a set both will variables point to same address, so clearing one set element will effect both.

s1 = {1,2,3,4}
s1_backup=s1
print(id(s1))
print(id(s1_backup))

print(s1)
print(s1_backup)

s1.clear()

print(s1)

print(s1_backup)

# difference() :- This method return difference of two or more sets as a new set

x ={"a","b","c","d"}

y = {"c","v","b"}

print(x.difference(y))

# instead of using method difference(), we can use operator -

print(x-y)


# difference_update() :- the method difference_update() removes all elements of another set from this set. x.difference_update(y) is the same as x=x-y

w={"a","b","c","d"}
y={"c","b","z"}

#x.difference_update(y)

# print(x)

x = x-y


# Some methods were not included come back after some time.