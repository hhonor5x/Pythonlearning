##Iterator based for loop : This kind of loop iterates over an enumerator of a set of items.
##
##Syntax of the for loop:
##    for <variable> in <sequence>:
##        <statements>
##    else:
##        <statements>
languages = ["Python","Ruby","Perl","c","c++"]

for x in languages:
    print(x)
    

# else in for loop

food=["eggs","ham","spam", "nuts"]


for x in food:
    if x == "spam":
        print("No more spam please")
        break
    print("Wow! it's ", x)
else:
    print("I'm so glad that there was no spam")
print("Finally i finished my food program")



    