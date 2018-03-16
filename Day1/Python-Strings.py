# Python Strings

s1 = 'This is a single quote string in python3'

s2 = "This is a double quote string in python3"

s3 = """This is a multline
        line string
        in python3""" 

s7 = ''' Hello this's also
            a multiline
            string with 3 single
            quotes'''

print(s1)
print(s2)
print(s3)
print(s7)

# In case of single quotes if we need to escape a character we need to use a \ for example

s4 = 'It doesn\'t matter'
print(s4)


# But if we use double quotes there is no need to escape with backslach for example

s5 = "It doesn't matter"
print(s5) 

# But if we want to escape a double quote inside a double quoted string we need to use backslach(\)

s6 = "Hi There, \"Welcome to party\""
print(s6)

# Strings in python stores in series or sequence of character, for example
s8 = "HELLO PYTHON"

# 0 | 1 | 2 | 3 | 4 | 5| 6|  7|  8|  9|  10|  11|
#________________________________________________
# H | E | L | L | O |  | P|  Y|  T|  H |  O|  N |
#________________________________________________
#-12|-11|-10|-9 |-8 |-7|-6| -5| -4| -3 | -2| -1 | 

print(s8[6])
print(s8[-5])

#Strings in Python are Immutable

s9 = "welcome"
#s9[1] = '."
#print(s9) # results an error

a = "yes"
b = "yes"

print(a is b )
print ( a == b)


c = "un-lock!"
d = "un-lock!"

print(a is b)
print(a == b)

# String concatenation

a = "Hello"
b = "Python"
a+=b
print ( a )

# Repetetion

x = "A"
y = "W"
z = "!"
print ( x*2+y*3+z*4)



