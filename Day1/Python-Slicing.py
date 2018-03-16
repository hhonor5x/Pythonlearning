# Slicing in python can be done using slicing operator ( : )

# If s is a sequential data type, slicing works like below
# s[begin: end: step]

str = "Python is great"
print("Print first six characters of str:", str[0:6])

print("Print str starting from 5th character:", str[5:])

print("Print without last 5 characters:", str[0:-5])


str1= "Python under linux is great"

print(str1[::2]) # result will be str1[begin], str1[begin+1*step], str1[begin+2*step] ....str1[begin+i*step] <end.




